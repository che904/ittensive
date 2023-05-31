import requests
from bs4 import BeautifulSoup
import sqlite3

# URL-адрес зеркала страницы с результатами для холодильников Саратов
url = 'https://video.ittensive.com/data/018-python-advanced/beru.ru/'

# Выполнение GET-запроса к указанному URL-адресу
response = requests.get(url)

# Создание объекта BeautifulSoup для парсинга HTML-кода
soup = BeautifulSoup(response.content, 'html.parser')

# Подключение к базе данных SQLite
conn = sqlite3.connect('beru.db')
cursor = conn.cursor()

# Создание таблицы в базе данных
cursor.execute('''
    CREATE TABLE IF NOT EXISTS beru_goods (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        name TEXT,
        price REAL,
        dimensions TEXT,
        total_volume REAL,
        fridge_volume REAL
    )
''')

# Поиск блоков с информацией о холодильниках Саратов
sar_blocks = soup.find_all('div', class_='ba-tile-block ba-tile-block_list ba-tile-block_list_2x2 ba-tile-block_type_models')

# Обход блоков и извлечение информации о каждом холодильнике
for sar_block in sar_blocks:
    # Извлечение URL
    url = sar_block.find('a', class_='ba-tile ba-tile_product').get('href')
    
    # Извлечение названия
    name = sar_block.find('div', class_='ba-tile__content').find('div', class_='ba-tile__title').text.strip()
    
    # Извлечение цены
    price = sar_block.find('div', class_='ba-tile__price-block').find('span', class_='ba-tile__price').text.strip()
    
    # Извлечение размеров
    dimensions = sar_block.find('div', class_='ba-tile__content').find('div', class_='ba-tile__dimensions').text.strip()
    
    # Извлечение общего объема
    total_volume = sar_block.find('div', class_='ba-tile__content').find('div', class_='ba-tile__volume').text.strip()
    
    # Извлечение объема холодильной камеры
    fridge_volume = sar_block.find('div', class_='ba-tile__content').find('div', class_='ba-tile__subtitle').text.strip()
    
    # Вставка данных в таблицу базы данных
    cursor.execute('''
        INSERT INTO beru_goods (url, name, price, dimensions, total_volume, fridge_volume)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (url, name, price, dimensions, total_volume, fridge_volume))

# Сохранение изменений в базе данных
conn.commit()

# Закрытие соединения с базой данных
conn.close()
