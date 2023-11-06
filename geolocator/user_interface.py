class UserInterface:
    def hello(self):
        answer = input("Question?: ")
        print(answer)

    def get_location(self):
        latitude = float(input("Fill in your Latitude: "))
        longitude = float(input("Fill in your Longitude: "))

        return latitude, longitude
