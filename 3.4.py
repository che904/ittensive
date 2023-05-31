import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Загрузка данных по объектам культурного наследия
data = pd.read_csv('https://video.ittensive.com/python-advanced/data-44-structure-4.csv.gz', compression='gzip')

# Группировка данных по регионам и подсчет количества объектов
counts = data.groupby('Регион')['Наименование'].count()

# Загрузка гео-данных России
map_data = gpd.read_file('https://video.ittensive.com/python-advanced/russia.json')

# Объединение данных по количеству объектов с гео-данными
merged_data = map_data.merge(counts, left_on='name', right_index=True, how='left')

# Вывод количества объектов для каждого региона
for index, row in merged_data.iterrows():
    print(f"{row['name']}: {row['Наименование']}")

# Построение фоновой картограммы
fig, ax = plt.subplots(figsize=(15, 10))
merged_data.plot(column='Наименование', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Настройка осей и заголовка
ax.set_title('Количество объектов культурного наследия в регионах России')
ax.set_axis_off()

# Отображение картограммы
plt.show()
