import csv
import time
import psycopg2
from psycopg2 import sql


class PostgresConnector:
    connector = None
    '''
        Initializes Postgres Connector.
        Throws exception in case of failures.
    '''
    def __init__(self):
        if PostgresConnector.connector is None:
            try:
                PostgresConnector.connector = psycopg2.connect(
                    database="online_bookstore",
                    user="postgres",
                    password="postgres",
                    host="localhost",
                    port="5432"
                )

                PostgresConnector.connector.autocommit = True
            except Exception as e:
                print('Error: DB connection not established :: {}'.format(e))
            else:
                print('DB connection success.')

    '''
        Executes sql passed to the function.
        Throws exception in case of failures.
    '''
    def executeSQL(self, sql):
        cursor = PostgresConnector.connector.cursor()
        try:
            cursor.execute(sql)
        except Exception as e:
            print("Error: Error while executing SQL :: {}".format(e))
        finally:
            cursor.close()

    '''
        Loads the CSV file into the table with table_name.
        Throws exception in case of failures.
    '''
    def loadCSVFiles(self, file, table_name):
        try:
            cursor = PostgresConnector.connector.cursor()
            print(f"Loading Table: {table_name}")
            start_time = time.time()
            with open(file, 'r') as f:
                reader = csv.reader(f)
                header = next(reader)
                columns = [sql.Identifier(column) for column in header]

                insert_statement = sql.SQL('INSERT INTO {} ({}) VALUES ({})').format(
                    sql.Identifier(table_name),
                    sql.SQL(', ').join(columns),
                    sql.SQL(', ').join(sql.Placeholder() * len(header))
                )
                for row in reader:
                    row_values = [int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value for value in row]
                    row_values = [value if value != '' else None for value in row_values]
                    cursor.execute(insert_statement, row_values)

            end_time = time.time()
            print(f"Table {table_name} loaded successfully. Time Taken : {end_time - start_time}")

        except Exception as e:
            print("Error: Error while loading table {} :: {}".format(table_name, e))
        finally:
            cursor.close()

    '''
        Disconnects the Postgres connector.
        Throws exception in case of failures.
    '''
    def disconnect(self):
        if PostgresConnector.connector is not None:
            try:
                PostgresConnector.connector.close()
            except Exception as e:
                print("Error: DB disconnection failed :: {}".format(e))
            else:
                print("DB disconnected.")
