import requests

# Задайте ваш ключ API
api_key = '3f355b88-81e9-4bbf-a0a4-eb687fdea256'

# URL-адрес для выполнения запроса
url = f'https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&format=json&geocode=Самара'

# Выполнение запроса к API
response = requests.get(url)

# Парсинг JSON-ответа
data = response.json()

# Получение долготы точки на карте
longitude = float(data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()[0])

print(longitude)
