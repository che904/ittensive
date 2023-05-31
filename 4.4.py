import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Загрузка данных по результатам ЕГЭ
data = pd.read_csv('https://video.ittensive.com/python-advanced/data-9722-2019-10-14.utf.csv', delimiter=';')

# Общее число отличников (более 220 баллов)
total_excellent_students = len(data[data['Балл'] > 220])

# Распределение отличников по округам Москвы
districts_excellent_counts = data[data['Балл'] > 220]['Район'].value_counts()

# Название школы с лучшими результатами
best_school = data.loc[data['Балл'].idxmax()]['Наименование учреждения']

# Построение диаграммы распределения отличников
plt.figure(figsize=(8, 6))
districts_excellent_counts.plot(kind='bar')
plt.xlabel('Округ')
plt.ylabel('Количество отличников')
plt.title('Распределение отличников по округам Москвы')
plt.xticks(rotation=45)
plt.tight_layout()

# Сохранение диаграммы в формате base64
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_base64 = base64.b64encode(buffer.getvalue()).decode()

# Создание HTML отчета
html_report = f'''
<html>
<head>
<style>
table, th, td {{
  border: 1px solid black;
  border-collapse: collapse;
}}
th, td {{
  padding: 5px;
  text-align: left;
}}
</style>
</head>
<body>
<h2>Отчет по результатам ЕГЭ в Москве</h2>
<p>Общее число отличников (более 220 баллов): {total_excellent_students}</p>
<h3>Распределение отличников по округам Москвы:</h3>
<img src="data:image/png;base64,{image_base64}">
<h3>Название школы с лучшими результатами:</h3>
<p>{best_school}</p>
</body>
</html>
'''

# Создание PDF отчета
pdf_report = BytesIO()
doc = SimpleDocTemplate(pdf_report, pagesize=letter)
styles = getSampleStyleSheet()
story = [Paragraph(html_report, styles["Normal"])]
doc.build(story)

# Отправка отчета по электронной почте
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

sender_email = 'your_email@example.com'
receiver_email = 'support@ittensive.com'
subject = 'Отчет по результатам ЕГЭ'
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Вложение HTML отчета
html_part = MIMEText(html_report, 'html')
message.attach(html_part)

# Вложение PDF отчета
pdf_part = MIMEApplication(pdf_report.getvalue(), Name='report.pdf')
pdf_part['Content-Disposition'] = 'attachment; filename="report.pdf"'
message.attach(pdf_part)

# Отправка письма
with smtplib.SMTP('smtp.example.com', 587) as server:
    server.login('your_email@example.com', 'your_password')
    server.sendmail(sender_email, receiver_email, message.as_string())
