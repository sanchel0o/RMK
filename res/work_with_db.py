import psycopg2

host = '127.0.0.1'
user = 'postgres'
password = '1111'
db_name = 'postgres'


def conn_to_db():
    # connect to db
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    # the cursor for performing db operations
    cursor = connection.cursor()
    return connection, cursor


def disconn_from_db(connection, cursor):
    cursor.close()
    connection.close()


def create_table():
    connection, cursor = conn_to_db()
    cursor.execute("""
        CREATE TABLE DATA (
        DATE TEXT NOT NULL,
        SPACE TEXT NOT NULL,
        VOLUME TEXT NOT NULL,
        VEHICLE TEXT NOT NULL,
        NUMBER TEXT NOT NULL);
        """)
    connection.commit()
    disconn_from_db(connection, cursor)


def insert_data_to_db(data):
    connection, cursor = conn_to_db()
    for row in data:
        insert = f"""INSERT INTO DATA (date, space, volume, vehicle, number) VALUES (
            '{row['Дата']}',
            '{row['Площадь']}',
            '{row['Объем']}',
            '{row['Техника']}',
            '{row['Номер']}');"""
        cursor.execute(insert)
    connection.commit()
    disconn_from_db(connection, cursor)


def extract_data():
    connection, cursor = conn_to_db()
    select = "SELECT date, space, volume, vehicle, number FROM DATA"
    cursor.execute(select)
    data = cursor.fetchall()
    disconn_from_db(connection, cursor)

    table = dict()
    table['Дата'] = [row[0] for row in data]
    table['Площадь'] = [row[1] for row in data]
    table['Объем'] = [row[2] for row in data]
    table['Техника'] = [row[3] for row in data]
    table['Номер техники'] = [row[4] for row in data]
    return table
