import pandas as pd

# Загрузка данных
url = "https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv"
data = pd.read_csv(url, delimiter=";")

# Преобразование столбца с датой в формат datetime
data['date'] = pd.to_datetime(data['date'], format="%Y-%m-%d %H:%M:%S")

# Создание нового столбца с месяцем вызова
data['month'] = data['date'].dt.month

# Группировка данных по округу и месяцу, подсчет числа вызовов
grouped_data = data.groupby(['district', 'month']).size().reset_index(name='call_count')

# Вычисление среднего значения вызовов в месяц в одном округе
average_calls_per_month = grouped_data.groupby('district')['call_count'].mean().round()

print(average_calls_per_month)
