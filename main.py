import glob
from Connectors.PostgresConnector import PostgresConnector
from Queries import DDL_Queries


def loadTables(conn):
    path = './Resources/Dataset/*.csv'
    table_file_map = {}
    for file in glob.glob(path):
        table_name = file[20:-4].lower()
        table_file_map[table_name] = file

    load_table_order = [
        'authors',
        'series',
        'books',
        'ratings',
        'awards',
        'publishers',
        'editions',
        'checkouts',
        'orders',
        'items'
    ]

    for table_name in load_table_order:
        file = table_file_map[table_name]
        conn.loadCSVFiles(file, table_name)


def initializeDBObjects(conn):
    ddl_statements = DDL_Queries.ddl_statements

    for sql in ddl_statements:
        conn.executeSQL(sql)

    loadTables(conn)


if __name__ == '__main__':
    conn = PostgresConnector()
    initializeDBObjects(conn)
    # loadTables()
    conn.disconnect()
