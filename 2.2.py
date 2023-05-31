import requests
from bs4 import BeautifulSoup

# URL-адрес для получения данных по котировкам акций
url = 'https://mfd.ru/marketdata/?id=5&group=16&mode=3&sortHeader=name&sortOrder=1&selectedDate=01.11.2019'

# Выполнение GET-запроса к указанному URL-адресу
response = requests.get(url)

# Создание объекта BeautifulSoup для парсинга HTML-страницы
soup = BeautifulSoup(response.content, 'html.parser')

# Поиск таблицы с данными по котировкам акций
table = soup.find('table', class_='js-table-sorter mfd-table')

# Инициализация переменных для хранения информации о максимальном росте числа сделок
max_growth = 0
max_growth_ticker = ''

# Перебор строк таблицы с данными по котировкам акций
for row in table.find_all('tr'):
    # Проверка наличия данных в строке
    if len(row.find_all('td')) > 1:
        # Извлечение тикера и процентного изменения числа сделок
        ticker = row.find_all('td')[0].text.strip()
        growth = row.find_all('td')[10].text.strip()

        # Проверка, является ли текущий рост числа сделок максимальным
        if growth and float(growth) > max_growth:
            max_growth = float(growth)
            max_growth_ticker = ticker

print(max_growth_ticker)
