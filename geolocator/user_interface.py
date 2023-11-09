class UserInterface:
    def get_location(self):
        location_input = input("Fill in your Latitude and Longitude (comma-separated): ")
        latitude, longitude = map(float, location_input.split(','))

        return latitude, longitude
