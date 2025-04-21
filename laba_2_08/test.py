import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

# Логистическая функция
def logistic_function(x, L, x0, k):
    return L / (1 + np.exp(-k * (x - x0)))

# Линейная функция
def linear_function(x, a, b):
    return a * x + b

# Загрузка данных из Excel файла
file_path = '../laba_2_08/data_2_08.xlsx'
data = pd.read_excel(file_path)

# Данные из Excel файла
datasets = [
    (data.iloc[2:10, 0].astype(float), data.iloc[2:10, 1].astype(float), 'u = 7v'),
    (data.iloc[2:13, 2].astype(float), data.iloc[2:13, 3].astype(float), 'u = 8v'),
    (data.iloc[2:13, 4].astype(float), data.iloc[2:13, 5].astype(float), 'u = 9v'),
    (data.iloc[2:11, 6].astype(float), data.iloc[2:11, 7].astype(float), 'u = 6v')
]

# Аппроксимация данных и построение графиков
def approximate_and_plot(Il, Ia, title):
    # Логистическая аппроксимация
    params_log, _ = curve_fit(logistic_function, Il, Ia, p0=[1, np.mean(Il), 1])

    # Линейная аппроксимация для первых трех точек
    params_linear_start, _ = curve_fit(linear_function, Il[:3], Ia[:3])

    # Линейная аппроксимация для остальных точек
    params_linear_end, _ = curve_fit(linear_function, Il[3:], Ia[3:])

    # Построение графика
    plt.figure(figsize=(6, 4))
    plt.plot(Il, Ia, 'bo', label='Data')
    plt.plot(Il, logistic_function(Il, *params_log), 'r-', label='Fitted Logistic Function')

    # Построение линейных аппроксимаций
    Il_extended = np.linspace(Il.min(), Il.max(), 500)
    plt.plot(Il_extended, linear_function(Il_extended, *params_linear_start), 'g--', label='Linear Start Approximation')
    plt.plot(Il_extended, linear_function(Il_extended, *params_linear_end), 'b--', label='Linear End Approximation')

    # Нахождение точки пересечения
    Icr = (params_linear_end[1] - params_linear_start[1]) / (params_linear_start[0] - params_linear_end[0])
    plt.axvline(x=Icr, color='k', linestyle='--', label=f'Icr: {Icr:.2f}')

    plt.xlabel('Il')
    plt.ylabel('Ia')
    plt.title(title)
    plt.legend()
    plt.show()

# Построение графиков с аппроксимацией
for Il, Ia, title in datasets:
    approximate_and_plot(Il, Ia, title)
