import os
import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self,):
        self.connection = None

    def connect(self, db_path):
        try:
            self.connection = sqlite3.connect(db_path)
            self._create_table()
        except Error as error:
            print(error)
        finally:
            if self.connection:
                self.connection.close()

    def write(self, latitude, longitude, city, country):
        pass

    def _create_table(self):
        pass
