import pandas as pd

# Загрузка данных по безработице в Москве
unemployment_url = "https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv"
unemployment_data = pd.read_csv(unemployment_url, delimiter=";")

# Преобразование столбца с датой в формат datetime и установка его в качестве индекса
unemployment_data['Месяц/Год'] = pd.to_datetime(unemployment_data['Месяц/Год'], format="%Y-%m")
unemployment_data.set_index('Месяц/Год', inplace=True)

# Фильтрация данных, чтобы оставить только строки с процентом UnemployedDisabled меньше 2%
filtered_data = unemployment_data[unemployment_data['UnemployedDisabled'] < 2]

# Нахождение минимального года, с которого процент UnemployedDisabled меньше 2%
min_year = filtered_data.index.min().year

print(min_year)
