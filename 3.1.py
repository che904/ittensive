import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
data = pd.read_csv('https://video.ittensive.com/python-advanced/data-9722-2019-10-14.utf.csv', delimiter=';')

# Фильтрация данных за 2018-2019 учебный год
data_1819 = data[(data['Год'] >= 2018) & (data['Год'] <= 2019)]

# Создание диаграммы для административного округа Москвы
moscow_districts = data_1819[data_1819['Регион'] == 'Москва']
moscow_districts_high_scores = moscow_districts[moscow_districts['Балл'] >= 220]

# Построение диаграммы для количества школьников, написавших ЕГЭ на 220 баллов и выше
moscow_districts_high_scores['Административный округ'].value_counts().plot(kind='bar')
plt.title('Количество школьников, набравших 220 баллов и выше в административных округах Москвы')
plt.xlabel('Административный округ')
plt.ylabel('Количество школьников')
plt.show()

# Создание диаграммы для районов Северо-Западного административного округа Москвы
severozapad_districts = moscow_districts[moscow_districts['Административный округ'] == 'Северо-Западный']
severozapad_districts_high_scores = severozapad_districts[severozapad_districts['Балл'] >= 220]

# Построение диаграммы для количества школьников, написавших ЕГЭ на 220 баллов и выше в районах Северо-Западного административного округа Москвы
severozapad_districts_high_scores['Район'].value_counts().plot(kind='bar')
plt.title('Количество школьников, набравших 220 баллов и выше в районах Северо-Западного округа Москвы')
plt.xlabel('Район')
plt.ylabel('Количество школьников')
plt.show()
