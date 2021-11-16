import psycopg2
import connection
from menu import Menu

# Catching errors
try:
    # Making connection
    connect = connection.connection()
    # Creating cursor to control DB
    cursor = connect.cursor()
    # Controller call
    Menu.mainmenu()

except (Exception , psycopg2.Error) as error :
        print ("PostgreSQL Error: ",error)
finally:
    # Closing connection and cursir
    cursor.close()
    connect.close()
    print("PostgreSQL connection is closed")