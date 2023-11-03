from geopy.geocoders import OpenCage
from opencage.geocoder import OpenCageGeocode

def geocode_address(address):
    try:
        geolocator = OpenCageGeocode('4afa469015a84fe89a338b74d009a9aa')
        location = geolocator.geocode(address)

        if location:
            latitude = location[0]['geometry']['lat']
            longitude = location[0]['geometry']['lng']
            print("Address: ", address)
            print("Latitude: ", latitude)
            print("Longitude: " ,longitude)
        else:
            print("Location not found for the given address.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    user_address = input("Enter an address to geocode: ")
    geocode_address(user_address)
