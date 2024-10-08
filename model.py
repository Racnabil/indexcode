import pymysql

class Database:
    def __init__(self):
        # Koneksi ke MySQL di XAMPP
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',  # default MySQL password (kosong)
            database='abel'  # nama database Anda
        )
        self.cursor = self.connection.cursor()
    def fetch_food(self):
        query = "SELECT * FROM food"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_stationery(self):
        query = "SELECT * FROM stationery"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()