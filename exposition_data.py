import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from catboost import CatBoostClassifier

# Загрузка данных
train_data = pd.read_csv('https://video.ittensive.com/machine-learning/hacktherealty/E/exposition_train.tsv.gz', sep='\t')
test_data = pd.read_csv('https://video.ittensive.com/machine-learning/hacktherealty/E/exposition_test.tsv.gz', sep='\t')

# Просмотр данных
print(train_data.head())
print(test_data.head())

# Шаг 1: Формирование day_mean для тестовых данных

# Выделение признаков и целевой переменной
X = train_data[['count_day']]
y = train_data['day_mean']

# Разделение на обучающую и тестовую выборки
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

# Масштабирование данных
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_valid_scaled = scaler.transform(X_valid)
X_test_scaled = scaler.transform(test_data[['count_day']])

# Обучение линейной модели
lin_reg = LinearRegression()
lin_reg.fit(X_train_scaled, y_train)

# Прогнозирование day_mean для тестовых данных
test_data['day_mean'] = lin_reg.predict(X_test_scaled)

# Шаг 2: Применение кластеризации

# Объединение обучающих и тестовых данных для кластеризации
combined_data = pd.concat([train_data, test_data], ignore_index=True)

# Выделение признаков для кластеризации
features = ['count_day', 'day_mean']
combined_scaled = scaler.fit_transform(combined_data[features])

# Применение KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
combined_data['cluster'] = kmeans.fit_predict(combined_scaled)

# Разделение обратно на тренировочные и тестовые данные
train_data['cluster'] = combined_data.iloc[:len(train_data)]['cluster']
test_data['cluster'] = combined_data.iloc[len(train_data):]['cluster']

# Шаг 3: Использование модели классификации

# Выделение признаков и целевой переменной для классификации
X = train_data[['count_day', 'day_mean', 'cluster']]
y = train_data['exposition_class']

# Разделение на обучающую и тестовую выборки
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели CatBoost
model = CatBoostClassifier(iterations=1000, learning_rate=0.1, depth=6, eval_metric='Accuracy', verbose=200)
model.fit(X_train, y_train, eval_set=(X_valid, y_valid))

# Прогнозирование классов для тестовых данных
test_data['exposition_class'] = model.predict(test_data[['count_day', 'day_mean', 'cluster']])

# Экспорт результатов

# Сохранение результатов в файл
submission = test_data[['id', 'exposition_class']]
submission.to_csv('exposition_predictions.csv', index=False)

print("Результаты сохранены в файл exposition_predictions.csv")


# Описание шагов:
# Загрузка данных: Загружаем обучающие и тестовые данные.
# Формирование day_mean для тестовых данных: Строим линейную регрессионную модель для предсказания day_mean на основе count_day.
# Применение кластеризации: Применяем KMeans для кластеризации данных на основе признаков count_day и day_mean.
# Использование модели классификации: Используем CatBoostClassifier для классификации объявлений на основе признаков и кластеров.
# Экспорт результатов: Сохраняем результаты в файл exposition_predictions.csv.
