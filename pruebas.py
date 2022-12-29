#importando el modulo
import psycopg2

#conexion a base de datos

conexion=psycopg2.connect(user='postgres',
                          password='postgres',
                          host='190.119.207.174',
                          port='5432',
                          database='negocios')
#usando cursor
cursor= conexion.cursor()

#secuencia sql

sql='SELECT * FROM ventas.clientes'
# poniendo el sql
cursor.execute(sql)

#mostrar resultado

registro = cursor.fetchall()

print(registro)


cursor.closed
conexion.closed