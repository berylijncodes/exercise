import os
import sqlite3
from sqlite3 import Error

from .models import City

class Database:
    def __init__(self,):
        self.connection = None

    def connect(self, db_path):
        try:
            self.connection = sqlite3.connect(db_path)
            self._create_table()
        except Error as error:
            print(error)
        # finally:
        #     if self.connection:
        #         self.connection.close()

    def _serialize(self, row) -> City:
        return {
            "latitude": row[0],
            "longitude": row[1],
            "name": row[2],
            "country": row[3]
        }

    def get(self, latitude, longitude):
        cursor = self.connection.cursor()

        threshold = 0.03

        res = cursor.execute(
            """
            SELECT latitude, longitude, city, country_code
            FROM geolocation
            WHERE latitude BETWEEN ? AND ? AND longitude BETWEEN ? AND ?;
            """,
            (latitude - threshold, latitude + threshold, longitude - threshold, longitude + threshold)
        )

        cities = res.fetchall()

        return [self._serialize(city) for city in cities]

    def write(self, latitude, longitude, city, country):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO geolocation (latitude, longitude, city, country_code)
            VALUES (?, ?, ?, ?);
            """,
            (latitude, longitude, city, country)
        )

        self.connection.commit()

    def _create_table(self):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS geolocation(
                latitude REAL NOT NULL,
                longitude REAL NOT NULL,
                city TEXT NOT NULL,
                country_code TEXT NOT NULL
            );
            """
        )
