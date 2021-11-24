import psycopg2
import connection
from view import Menu

# Catching errors
try:
    Menu.mainmenu()
except (Exception , psycopg2.Error) as error :
        print ("PostgreSQL Error: ",error)
finally:
    print("PostgreSQL connection is closed")