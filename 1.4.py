import pandas as pd
from sklearn.linear_model import LinearRegression

# Загрузка данных по безработице в городе Москва
unemployment_url = "https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv"
unemployment_data = pd.read_csv(unemployment_url, delimiter=";")

# Преобразование столбца с датой в формат datetime
unemployment_data['Месяц/Год'] = pd.to_datetime(unemployment_data['Месяц/Год'], format="%Y-%m")

# Группировка данных по годам и подсчет числа значений в каждом году
grouped_data = unemployment_data.groupby(unemployment_data['Месяц/Год'].dt.year).size()

# Отбрасывание годов, в которых меньше 6 значений
filtered_data = unemployment_data[unemployment_data['Месяц/Год'].dt.year.isin(grouped_data[grouped_data >= 6].index)]

# Группировка отфильтрованных данных по годам и вычисление среднего значения отношения UnemployedDisabled к UnemployedTotal
grouped_data_mean = filtered_data.groupby(filtered_data['Месяц/Год'].dt.year).mean()
X = grouped_data_mean.index.values.reshape(-1, 1)
y = grouped_data_mean['UnemployedDisabled'] / grouped_data_mean['UnemployedTotal']

# Построение модели линейной регрессии
regression_model = LinearRegression()
regression_model.fit(X, y)

# Предсказание значения процента безработных инвалидов в 2020 году
predicted_value = regression_model.predict([[2020]])

# Округление предсказанного значения до сотых
predicted_value_rounded = round(predicted_value[0], 2)

print(predicted_value_rounded)
