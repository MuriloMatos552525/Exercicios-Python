'''
modulos python______
cx-oracle (mac)/db_oracle - oracle database(win 11) - oracle database
pyodbc - Microsoft sql server
pymsql - MySQL
psycopg2 - PostgreSQL

1- importar driver 
2- estabelecer conexao entre py e bd
3- criar um cursor (obj para executar quaries e obter resultados)
'''

import cx_Oracle

#Create connection

conn = cx_Oracle.connect(user="rm552525", password= "120505", host="oracle.fiap.com.br", port="1521", service_name="orcl")
print(conn.version)

cursor = conn.cursor()

sql_create = """
CREATE TABLE CEO_DETAILS(
    FIRST_NAME VARCHAR2(50),
    LAST_NAME VARCHAR2(50),
    COMPANY VARCHAR2(50),
    AGE NUMBER
)
"""
cursor.execute(sql_create)
print('tabela criada')

conn.close()

cursor.close()