import webbrowser

def find_city (city_name):
    google_search_url = f'https://earth.google.com/web/search/{city_name}'

    webbrowser.open(google_search_url)


city = input("Enter a city name: ")

find_city(city)