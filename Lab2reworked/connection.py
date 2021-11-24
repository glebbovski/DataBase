import psycopg2

#connection to DB
def connection():
    return psycopg2.connect(
        user="postgres",
        password="qwerty",
        host="localhost",
        port="5432",
        database="postgres"
    )

#closing conection to DB
def connectionlost(connect):
    connect.commit()
    connect.close()

