from scipy.stats import t
import numpy as np

# Данные
x_mean = 30
s = 6
n = 7
gamma = 0.99

# Критическое значение t
alpha = 1 - gamma
t_critical = t.ppf(1 - alpha / 2, df=n - 1)

# Полуширина доверительного интервала
margin_of_error = t_critical * (s / np.sqrt(n))

# Доверительный интервал
ci_lower = x_mean - margin_of_error
ci_upper = x_mean + margin_of_error

# Результат
print(f"Доверительный интервал: ({ci_lower:.4f}, {ci_upper:.4f})")
