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


#sentecia sql

sql = 'delete from personas where  idpersona=%s'

idpersona=input('pon id a borrar')

cursor.execute(sql,idpersona)

#giuardando  modificacion
conexion.commit()


registros = cursor.rowcount

print(f'registro borrado{registros}')


cursor.closed
conexion.closed



