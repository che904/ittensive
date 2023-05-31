import pandas as pd

# Загрузка данных по безработице в Москве
unemployment_url = "https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv"
unemployment_data = pd.read_csv(unemployment_url, delimiter=";")

# Преобразование столбца с датой в формат datetime и установка его в качестве индекса
unemployment_data['Месяц/Год'] = pd.to_datetime(unemployment_data['Месяц/Год'], format="%Y-%m")
unemployment_data.set_index('Месяц/Год', inplace=True)

# Загрузка данных по вызовам пожарных в Центральном административном округе
calls_url = "https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv"
calls_data = pd.read_csv(calls_url, delimiter=";")

# Преобразование столбца с датой в формат datetime и установка его в качестве индекса
calls_data['date'] = pd.to_datetime(calls_data['date'], format="%Y-%m-%d %H:%M:%S")
calls_data.set_index('date', inplace=True)

# Фильтрация данных по Центральному административному округу
central_district_calls = calls_data[calls_data['district'] == 'Центральный административный округ']

# Объединение данных по индексам месяца и года
merged_data = central_district_calls.merge(unemployment_data, how='inner', left_index=True, right_index=True)

# Нахождение месяца с наименьшим количеством вызовов в Центральном административном округе
min_calls_month = merged_data['call_count'].idxmin()

# Получение значения поля UnemployedMen в этом месяце
unemployed_men_value = merged_data.loc[min_calls_month, 'UnemployedMen']

print(unemployed_men_value)
