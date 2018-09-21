import mysql.connector


class Database:
    """Database class"""
    def __init__(self):
        self.db = mysql.connector.connect(
             host="localhost",
             user="root",
             passwd="",
             database='sis_db'
             )
        self.cursor = self.db.cursor(buffered=True)

    def cursor_execute(self, sql, val=None):
        self.cursor.execute(sql, val)
        self.db.commit()
