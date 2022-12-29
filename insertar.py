#importando el modulo
import psycopg2

#conexion a base de datos

conexion=psycopg2.connect(user='postgres',
                          password='postgres',
                          host='190.119.207.174',
                          port='5432',
                          database='db_personas')
#usando cursor
cursor= conexion.cursor()


sql='insert INTO personas (nombre,apellido,edad) VALUES (%s,%s,%s)'

nombre=input('ingrese nomnre')
apellido=input('ingrese apellido')
edad=input('ingrese edad')


datos=(nombre,apellido,edad)

cursor.execute(sql,datos)

conexion.commit()


registros = cursor.rowcount

print(f'registro insertado{registros}')


cursor.closed
conexion.closed