import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, SimpleDocTemplate

# Загрузка данных по активностям в парках Москвы
data = pd.read_json('https://video.ittensive.com/python-advanced/data-107235-2019-12-02.utf.json')

# Построение диаграммы распределения числа активностей по паркам (топ 10)
top_10_parks = data['Park'].value_counts().nlargest(10)
plt.figure(figsize=(10, 6))
plt.bar(top_10_parks.index, top_10_parks.values)
plt.xlabel('Парк')
plt.ylabel('Количество активностей')
plt.title('Распределение числа активностей по паркам (Топ 10)')
plt.xticks(rotation=45)
plt.tight_layout()

# Сохранение диаграммы в PDF
plt.savefig('activity_distribution.pdf')

# Создание таблицы активностей по всем паркам
table_data = [['Активность', 'Расписание', 'Парк']]
for _, row in data.iterrows():
    activity = row['Activity']
    schedule = row['Schedule']
    park = row['Park']
    table_data.append([activity, schedule, park])

# Создание PDF отчета
pdf = SimpleDocTemplate('activity_report.pdf', pagesize=letter)
story = []

# Добавление заголовка
title_page = plt.imread('https://video.ittensive.com/python-advanced/title.pdf')
story.append(title_page)

# Добавление диаграммы
activity_distribution_page = plt.imread('activity_distribution.pdf')
story.append(activity_distribution_page)

# Добавление таблицы
table = Table(table_data)
story.append(table)

# Генерация PDF отчета
pdf.build(story)

