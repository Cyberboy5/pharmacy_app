import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Disconnected from MySQL database")

    def create_user(self, username, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            self.connection.commit()
            print("User created successfully")
        except Error as e:
            print(f"Error: {e}")

    def find_user(self, username, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            user = cursor.fetchone()
            return user
        except Error as e:
            print(f"Error: {e}")
            return None

    def update_user(self, user_id, new_username, new_password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE users SET username=%s, password=%s WHERE id=%s", (new_username, new_password, user_id))
            self.connection.commit()
            success = cursor.rowcount > 0
            return success
        except Error as e:
            print(f"Error: {e}")
            return False

    def delete_user(self, user_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
            self.connection.commit()
            success = cursor.rowcount > 0
            return success
        except Error as e:
            print(f"Error: {e}")
            return False
