import mysql.connector
from mysql.connector import errorcode

DATABASE = 'clinicaDatabase'
USER = 'labdatabase'
PASSWORD = 'lab@Database2022'
HOST = 'localhost'
PORT = '3306'

def get_connection_string():
    return mysql.connector.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database=DATABASE
    )