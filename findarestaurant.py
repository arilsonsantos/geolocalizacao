from geocode import getGeoLocation
import requests


CLIENT_ID = 'YOUR_FOURSQUARE_CLIENT_ID'
CLIENT_SECRET = 'YOUR_FOURSQUARE_CLIENT_SECRET'


def findARestaurant(mealType, location):

    latitude, longitude = getGeoLocation(location)

    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' %
           (CLIENT_ID, CLIENT_SECRET, latitude, longitude, mealType))

    response = requests.get(url)

    if response.json()['response']['venues']:

        restaurante = response.json()['response']['venues'][0]
        restaurante_id = restaurante['id']
        enderecos_restaurante = restaurante['location']['formattedAddress']
        enderecos_alinhados = ''

        for address in enderecos_restaurante:
            enderecos_alinhados += address + ' '

        url_photo = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' %
                     (restaurante_id, CLIENT_ID, CLIENT_SECRET))

        response = requests.get(url_photo)

        photo = response.json()['response']['photos']['items']

        image = ''

        if photo:
            prefix = photo[0]['prefix']
            sufix = photo[0]['suffix']
            size = '300x300'

            image = prefix + size + sufix
        else:
            image = 'http://www.guiarestauranteseleto.com.br/img/upload/novidades/restaurante(3).jpg'

        PrintRestaurants(restaurante['name'], enderecos_alinhados, image)

    else:
        resultado = 'Nenhum resultado encontrado'
        print(resultado)
        return resultado


def PrintRestaurants(restauranteName, restaruanteAddress, imageRestaurant):
    print('Restaurant Name: ', restauranteName)
    print('Restaurant Address', restaruanteAddress)
    print('Image: ', imageRestaurant)
    print('')


if __name__ == '__main__':
    findARestaurant("Pizza", "Tokyo, Japan")
    findARestaurant("Tacos", "Jakarta, Indonesia")
    findARestaurant("Tapas", "Maputo, Mozambique")
    findARestaurant("Falafel", "Cairo, Egypt")
    findARestaurant("Spaghetti", "New Delhi, India")
    findARestaurant("Cappuccino", "Geneva, Switzerland")
    findARestaurant("Sushi", "Los Angeles, California")
    findARestaurant("Steak", "La Paz, Bolivia")
    findARestaurant("Gyros", "Sydney Australia")
