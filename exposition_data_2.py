import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from catboost import CatBoostClassifier
import lightgbm as lgb
import xgboost as xgb
from sklearn.metrics import accuracy_score

# Загрузка данных
train_data = pd.read_csv('https://video.ittensive.com/machine-learning/hacktherealty/E/exposition_train.tsv.gz', sep='\t')
test_data = pd.read_csv('https://video.ittensive.com/machine-learning/hacktherealty/E/exposition_test.tsv.gz', sep='\t')

# Обработка пропусков
train_data.fillna(train_data.mean(), inplace=True)
test_data.fillna(test_data.mean(), inplace=True)

# Формирование дополнительных признаков (например, агрегированные по дням, неделям)
train_data['day_mean'] = train_data.groupby('count_day')['day_mean'].transform('mean')
test_data['day_mean'] = test_data.groupby('count_day')['day_mean'].transform('mean')

# Преобразование категориальных признаков в числовые
train_data = pd.get_dummies(train_data, drop_first=True)
test_data = pd.get_dummies(test_data, drop_first=True)

# Разделение на признаки и целевые переменные
X_train = train_data.drop(['target_column'], axis=1)
y_train = train_data['target_column']
X_test = test_data

# Масштабирование данных
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Кластеризация с использованием KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
train_data['cluster'] = kmeans.fit_predict(X_train_scaled)

# Добавление информации о кластерах в тестовые данные
test_data['cluster'] = kmeans.predict(X_test_scaled)

# Обучение нескольких моделей
catboost_model = CatBoostClassifier(iterations=100, learning_rate=0.1, depth=5, cat_features=['categorical_feature1'])
catboost_model.fit(X_train, y_train)

lightgbm_model = lgb.LGBMClassifier(n_estimators=100, learning_rate=0.05)
lightgbm_model.fit(X_train, y_train)

xgboost_model = xgb.XGBClassifier(n_estimators=100, learning_rate=0.05)
xgboost_model.fit(X_train, y_train)

rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)

# Ансамблирование предсказаний
catboost_pred = catboost_model.predict_proba(X_test)[:, 1]
lightgbm_pred = lightgbm_model.predict_proba(X_test)[:, 1]
xgboost_pred = xgboost_model.predict_proba(X_test)[:, 1]
rf_pred = rf_model.predict_proba(X_test)[:, 1]

# Взвешенное среднее предсказаний
final_pred = (catboost_pred * 0.3 + lightgbm_pred * 0.3 + xgboost_pred * 0.2 + rf_pred * 0.2)

# Создание итогового предсказания
final_class = (final_pred > 0.5).astype(int)

# Подготовка файла для сабмишн
submission = test_data[['id']]
submission['predicted_class'] = final_class
submission.to_csv('submission.tsv', sep='\t', index=False)

print("Предсказание завершено и сохранено в submission.tsv.")
