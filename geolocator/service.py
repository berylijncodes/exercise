class Service:
    def __init__(self, database, geolocation_client,):
        self.database = database
        self.geolocation_client = geolocation_client

    def retrieve_cities(self, latitude, logitude,):
        cities = self.retrieve_cities_from_db( latitude, longitude, )

        if cities:
            return cities

        cities = self.retrieve_cities_from_api( latitude, longitude, )

        return cities

    def retrieve_cities_from_db(self, latitude, longitude,):
        cities = self.database.get( latitude, longitude, )

        print("Retrieved cities from database.", latitude, longitude, cities)

        return cities

    def retrieve_cities_from_api(self, latitude, longitude,):
        cities = self.geolocation_client.get( latitude, longitude, )

        print("Retrieved cities from api.", latitude, longitude, cities)

        for city in cities:
            self.database.write(latitude, longitude, city["name"], city["country"])

        return cities
