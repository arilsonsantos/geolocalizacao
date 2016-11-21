import requests


def getGeoLocation(inputString):
    google_api_key = 'YOUR_GOOGLE_API_KEY'

    locationString = inputString.replace(' ', '+')

    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' %
           (locationString, google_api_key))

    response = requests.get(url)

    location = (response.json()['results'][0]['geometry']['location'])
    latitude = location['lat']
    longitude = location['lng']

    return (latitude, longitude)


if __name__ == "__main__":
    print(getGeoLocation("Eunápoilis, Bahia"))
    print(getGeoLocation("Tokyo, Japan"))
    print(getGeoLocation("Sao Paulo, Sao Paulo"))
    print(getGeoLocation("Tacos, Jakarta, Indonesia"))
