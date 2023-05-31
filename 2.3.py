import requests
from bs4 import BeautifulSoup

# URL-адрес зеркала страницы с результатами для холодильников Саратов
url = 'https://video.ittensive.com/data/018-python-advanced/beru.ru/'

# Выполнение GET-запроса к указанному URL-адресу
response = requests.get(url)

# Создание объекта BeautifulSoup для парсинга HTML-кода
soup = BeautifulSoup(response.content, 'html.parser')

# Поиск блока с информацией о холодильнике Саратов 263
sar_263_block = soup.find('div', class_='ba-tile-block ba-tile-block_list ba-tile-block_list_2x2 ba-tile-block_type_models')

# Извлечение информации о холодильнике Саратов 263
sar_263_volume = sar_263_block.find('div', class_='ba-tile__content').find('div', class_='ba-tile__subtitle').text

# Поиск блока с информацией о холодильнике Саратов 452
sar_452_block = sar_263_block.find_next_sibling('div', class_='ba-tile-block ba-tile-block_list ba-tile-block_list_2x2 ba-tile-block_type_models')

# Извлечение информации о холодильнике Саратов 452
sar_452_volume = sar_452_block.find('div', class_='ba-tile__content').find('div', class_='ba-tile__subtitle').text

# Извлечение числовых значений объемов холодильников
sar_263_volume = float(sar_263_volume.split()[0])
sar_452_volume = float(sar_452_volume.split()[0])

# Разница в объеме холодильников
volume_difference = abs(sar_263_volume - sar_452_volume)

print(volume_difference)
