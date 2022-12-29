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

#sentencia sql
sql= 'update personas set nombre=%s,apellido=%s,edad=%s where idpersona=%s'


idpersona= input('ingrese el id de la persona: ')
nombre=input('ingrese nomnre')
apellido=input('ingrese apellido')
edad=input('ingrese edad')


datos=(nombre,apellido,edad,idpersona)

cursor.execute(sql,datos)

#giuardando  modificacion
conexion.commit()


registros = cursor.rowcount

print(f'registro actualizado{registros}')


cursor.closed
conexion.closed


