import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'chat_db'
        )

        
    def insert_user(self, user: dict):
        try:
            with self.connection.cursor() as cursor:
            # cursor =  self.connection.cursor()
                cursor.execute(f'''
                    INSERT INTO users (name, username, password) 
                    VALUES ('{user['name']}','{user['login']}','{user['password']}')
                ''')
                self.connection.commit()
                return False
        except Error as err:
            return str(err)
        
    def get_user_id(self, user: dict):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f'''
                    SELECT id FROM users WHERE username = '{user['login']}' AND password = '{user['password']}'
                ''')
                _id = cursor.fetchone()[0]
                return _id
        except Error as err:
            return str(err)
        
    
