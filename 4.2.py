import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import requests

# Загрузка данных по гербам и флагам районов Москвы
data = pd.read_csv('https://video.ittensive.com/python-advanced/data-102743-2019-11-13.utf.csv', delimiter=';')

# Создание PDF документа
pdf = canvas.Canvas('heraldry.pdf', pagesize=letter)

# Настройка SSL/TLS
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'

# Итерация по данным и добавление информации на каждую страницу
for index, row in data.iterrows():
    name = row['Name']
    description = row['Description']
    picture_url = f"https://op.mos.ru/MEDIA/showFile?id={row['Picture']}"

    # Загрузка изображения
    response = requests.get(picture_url)
    image_data = response.content

    # Добавление страницы
    pdf.showPage()

    # Добавление информации
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 750, 'Название: ' + name)
    pdf.drawString(50, 730, 'Описание: ' + description)
    pdf.drawImage(image_data, 50, 400, width=300, height=300)

# Сохранение PDF документа
pdf.save()
