import pandas as pd
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
data = pd.read_csv('https://video.ittensive.com/python-advanced/marathon-data.csv')

# Преобразование времени половины и полной дистанции к секундам
data['Half'] = pd.to_timedelta(data['Half']).dt.total_seconds()
data['Full'] = pd.to_timedelta(data['Full']).dt.total_seconds()

# Создание диаграммы pairplot для поиска коррелирующих серий данных
sns.pairplot(data)
plt.show()

# Нахождение коэффициента корреляции и построение графика jointplot для коррелирующих данных
correlation = data[['Half', 'Full']].corr().iloc[0, 1]
sns.jointplot(x='Half', y='Full', data=data, kind='scatter')
plt.title(f'Correlation: {correlation:.2f}')
plt.show()
