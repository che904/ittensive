import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Загрузка данных по посещаемости библиотек
data = pd.read_json('https://video.ittensive.com/python-advanced/data-7361-2019-11-28.utf.json')

# Группировка данных по районам и подсчет суммарной посещаемости
district_counts = data.groupby('District')['NumOfVisitors'].sum()

# Получение 20 наиболее популярных районов
top_districts = district_counts.nlargest(20)

# Построение круговой диаграммы
plt.figure(figsize=(10, 10))
top_districts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Суммарная посещаемость 20 наиболее популярных районов Москвы')
plt.ylabel('')
plt.legend(loc='upper left')

# Создание PDF отчета
pdf = canvas.Canvas('report.pdf', pagesize=letter)

# Добавление первой страницы из файла
pdf.drawInlineImage('https://video.ittensive.com/python-advanced/title.pdf', 0, 0, width=letter[0], height=letter[1])

# Добавление второй страницы с диаграммой и данными
pdf.showPage()
pdf.setFont("Helvetica", 12)
pdf.drawString(50, 750, 'Итоговая диаграмма посещаемости')
pdf.drawInlineImage('plot.png', 50, 400, width=500, height=500)
pdf.drawString(50, 350, f'Самый популярный район: {top_districts.index[0]}')
pdf.drawString(50, 320, f'Количество посетителей: {top_districts.iloc[0]}')

# Сохранение PDF отчета
pdf.save()
