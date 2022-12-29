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