import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных из CSV-файла
data = pd.read_csv('https://video.ittensive.com/python-advanced/rts-index.csv')

# Преобразование столбца Date в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# Отбор данных за 2017, 2018 и 2019 годы
data_2017 = data[data['Date'].dt.year == 2017]
data_2018 = data[data['Date'].dt.year == 2018]
data_2019 = data[data['Date'].dt.year == 2019]

# Создание графика закрытия индекса по дням за 2017, 2018 и 2019 годы
plt.plot(data_2017['Date'], data_2017['Close'], label='2017')
plt.plot(data_2018['Date'], data_2018['Close'], label='2018')
plt.plot(data_2019['Date'], data_2019['Close'], label='2019')

# Расчет экспоненциального среднего за 20 дней для значения Max в 2017 году
rolling_max = data_2017['Max'].rolling(window=20).mean()

# Добавление экспоненциального среднего на график
plt.plot(data_2017['Date'], rolling_max, label='Exponential Mean')

# Поиск последней даты, когда экспоненциальное среднее Max в 2017 году больше значения Close в 2019 году
last_crossing_date = data_2017['Date'][rolling_max.gt(data_2019['Close'].values[-1])].max()

# Добавление вертикальной линии на график в последней дате пересечения
plt.axvline(last_crossing_date, color='red', linestyle='--')

# Настройка осей и легенды
plt.xlabel('Date')
plt.ylabel('Close')
plt.legend()

# Отображение графика
plt.show()
