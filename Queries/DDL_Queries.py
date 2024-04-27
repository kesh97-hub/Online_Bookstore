ddl_statements = [
    '''DROP TABLE authors CASCADE;''',

    '''DROP TABLE series CASCADE''',

    '''DROP TABLE books CASCADE''',

    '''DROP TABLE publishers CASCADE''',

    '''DROP TABLE ratings CASCADE''',

    '''DROP TABLE awards CASCADE''',

    '''DROP TABLE editions CASCADE''',

    '''DROP TABLE checkouts CASCADE''',

    '''DROP TABLE orders CASCADE''',

    '''DROP TABLE items CASCADE''',

    '''
        CREATE TABLE IF NOT EXISTS authors (
            author_id VARCHAR(30) NOT NULL,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            birthday DATE,
            country_of_residence VARCHAR(50),
            hours_writing_per_day DECIMAL,
            CONSTRAINT authors_pk 
                PRIMARY KEY (author_id)
        );
    ''',

    '''
        CREATE TABLE IF NOT EXISTS series (
            series_id VARCHAR(20) NOT NULL,
            series_name VARCHAR(50),
            planned_volumes INT,
            book_tour_events INT,
            CONSTRAINT series_pk 
                PRIMARY KEY (series_id)
        );
    ''',

    '''
        CREATE TABLE IF NOT EXISTS books (
            book_id VARCHAR(30) NOT NULL,
            title VARCHAR(100) NOT NULL,
            author_id VARCHAR(30) NOT NULL,
            series_id VARCHAR(20) NULL,
            genre VARCHAR(50),
            volume_number INT,
            comments VARCHAR(1000),
            CONSTRAINT books_pk 
                PRIMARY KEY (book_id),
            CONSTRAINT books_fk1 
                FOREIGN KEY (author_id) REFERENCES authors(author_id)
        );
    ''',

    '''
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id VARCHAR(20) NOT NULL,
            publishing_house VARCHAR(50),
            city VARCHAR(50),
            state VARCHAR(50),
            country VARCHAR(50),
            year_established INT,
            marketing_spend DECIMAL,
            CONSTRAINT publishers_pk 
                PRIMARY KEY (publisher_id)
        );
    ''',

    '''
        CREATE TABLE IF NOT EXISTS ratings (
            review_id INT NOT NULL,
            reviewer_id INT,
            book_id VARCHAR(30) NOT NULL,
            rating INT,
            CONSTRAINT ratings_pk 
                PRIMARY KEY (review_id),
            CONSTRAINT ratings_fk1 
                FOREIGN KEY (book_id) REFERENCES books(book_id)
        );
    ''',

    '''
        CREATE TABLE IF NOT EXISTS awards (
            book_id VARCHAR(30) NOT NULL,
            award_name VARCHAR(100) NOT NULL,
            year_won INT NOT NULL,
            CONSTRAINT awards_pk 
                PRIMARY KEY (book_id, award_name, year_won),
            CONSTRAINT awards_fk1
                FOREIGN KEY (book_id) REFERENCES books(book_id)
        );
    ''',

    '''
        CREATE TABLE IF NOT EXISTS editions (
            isbn VARCHAR(30) NOT NULL,
            book_id VARCHAR(30) NOT NULL,
            publisher_id VARCHAR(20) NOT NULL,
            publication_date DATE,
            format VARCHAR(50),
            print_run_size INT,
            pages INT,
            price DECIMAL,
            CONSTRAINT editions_pk 
                PRIMARY KEY (isbn),
            CONSTRAINT editions_fk1 
                FOREIGN KEY (book_id) REFERENCES books(book_id),
            CONSTRAINT edition_fk2 
                FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
        );
    ''',

    '''
        CREATE TABLE IF NOT EXISTS checkouts (
            checkout_id INT NOT NULL,
            book_id VARCHAR(30) NOT NULL,
            checkout_month INT NOT NULL,
            checkout_count INT,
            CONSTRAINT checkouts_pk
                PRIMARY KEY (checkout_id),
            CONSTRAINT checkouts_fk
                FOREIGN KEY (book_id) REFERENCES books(book_id)
        );
    ''',

    '''
        CREATE TABLE IF NOT EXISTS orders (
            order_id VARCHAR(30) NOT NULL,
            order_date DATE,
            CONSTRAINT orders_pk 
                PRIMARY KEY (order_id)
        );
    ''',

    '''
        CREATE TABLE IF NOT EXISTS items (
            item_id VARCHAR(30) NOT NULL,
            order_id VARCHAR(30) NOT NULL,
            isbn VARCHAR(30) NOT NULL,
            discount DECIMAL,
            CONSTRAINT items_pk 
                PRIMARY KEY (item_id, order_id),
            CONSTRAINT items_fk1
                FOREIGN KEY (isbn) REFERENCES editions(isbn),
            CONSTRAINT items_fk2
                FOREIGN KEY (order_id) REFERENCES orders(order_id)
        );
    '''
]
