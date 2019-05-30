import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="ProyectoDB")

    cursor = connection.cursor()

    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error :
    print ("Error al conectarse a PostgreSQL!", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("La conexión a PostgreSQL fue cerrada")