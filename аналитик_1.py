import numpy as np
from scipy.stats import t

# Данные выборки
x = np.array([-2, 1, 2, 3, 4, 5])  # варианты
n_i = np.array([2, 1, 2, 2, 2, 1])  # частоты

# Объем выборки
n = n_i.sum()

# Выборочная средняя
x_mean = np.sum(x * n_i) / n

# Выборочная дисперсия
s_squared = np.sum(n_i * (x - x_mean)**2) / (n - 1)
s = np.sqrt(s_squared)

# Надежность
gamma = 0.95
alpha = 1 - gamma

# Критическое значение t
t_critical = t.ppf(1 - alpha / 2, df=n - 1)

# Полуширина доверительного интервала
margin_of_error = t_critical * (s / np.sqrt(n))

# Доверительный интервал
ci_lower = x_mean - margin_of_error
ci_upper = x_mean + margin_of_error

# Результат
print(f"Выборочная средняя: {x_mean:.4f}")
print(f"Доверительный интервал для математического ожидания с надежностью {gamma * 100}%: ({ci_lower:.4f}, {ci_upper:.4f})")
