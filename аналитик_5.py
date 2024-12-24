import numpy as np
from scipy.stats import norm

# Данные
milk_consumption = np.array([8.3, 8.6, 8.7, 8.8, 9.1, 9.3, 9.4, 13.4, 13.5, 13.8, 13.9, 14.1, 14.3])

# Вычисление выборочной средней и стандартного отклонения
x_mean = np.mean(milk_consumption)
s = np.std(milk_consumption, ddof=1)  # Выборочное стандартное отклонение
n = len(milk_consumption)

# Уровень надежности
gamma = 0.95
alpha = 1 - gamma

# Критическое значение z для нормального распределения
z_critical = norm.ppf(1 - alpha / 2)

# Полуширина доверительного интервала
margin_of_error = z_critical * (s / np.sqrt(n))

# Доверительный интервал
ci_lower = x_mean - margin_of_error
ci_upper = x_mean + margin_of_error

# Результат
print(f"Доверительный интервал для математического ожидания: ({ci_lower:.4f}, {ci_upper:.4f})")
