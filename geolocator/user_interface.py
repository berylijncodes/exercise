class UserInterface:
    def hello(self):
        answer = input("Question?: ")
        print(answer)

    def get_location(self):
        latitude = input("Fill in your Latitude: ")
        longitude = input("Fill in your Longitude: ")

        return latitude, longitude
