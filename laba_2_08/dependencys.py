import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

# Логистическая функция
def logistic_function(x, L, x0, k):
    return L / (1 + np.exp(-k * (x - x0)))

# Загрузка данных из Excel файла
file_path = 'data_2_08.xlsx'
data = pd.read_excel(file_path)

# Данные из Excel файла
datasets = [
    (data.iloc[2:10, 0].astype(float), data.iloc[2:10, 1].astype(float), 'u = 7v'),
    (data.iloc[2:13, 2].astype(float), data.iloc[2:13, 3].astype(float), 'u = 8v'),
    (data.iloc[2:13, 4].astype(float), data.iloc[2:13, 5].astype(float), 'u = 9v'),
    (data.iloc[2:11, 6].astype(float), data.iloc[2:11, 7].astype(float), 'u = 6v')
]

# Аппроксимация данных и построение графиков
def approximate_and_plot(Il, Ia, title, start_points, additional_lines=None):
    # Логистическая аппроксимация
    params, _ = curve_fit(logistic_function, Il, Ia, p0=[1, np.mean(Il), 1])
    plt.figure(figsize=(6, 4))
    plt.plot(Il, Ia, 'bo', label='Data')
    plt.plot(Il, logistic_function(Il, *params), 'r-', label='Fitted Logistic Function')
    plt.xlabel('Il')
    plt.ylabel('Ia')

    # Линейная аппроксимация для начальной части (почти горизонтальная линия)
    config1 = np.polyfit(Il[:start_points], Ia[:start_points], 1)
    y1 = np.poly1d(config1)

    # Построение линейной аппроксимации
    Il_extended = np.linspace(Il.min(), Il.max(), 100)
    plt.plot(Il_extended, y1(Il_extended), 'g--', label='Linear Start Approximation')

    # Добавление дополнительных линий, если они предоставлены
    if additional_lines:
        for (x_vals, y_vals) in additional_lines:
            # Продолжение линии за пределы отрезка
            line1 = np.poly1d(np.polyfit(x_vals, y_vals, 1))
            x_extended = np.linspace(Il.min(), Il.max(), 100)
            plt.plot(x_extended, line1(x_extended), 'm--', label='Additional Line')

            # Нахождение точки пересечения
            Icr = (line1(0) - y1(0)) / (y1.coef[0] - line1.coef[0])
            plt.plot(Icr, line1(Icr), 'ko', label=f'Intersection: ({Icr:.2f}, {line1(Icr):.2f})')

            # Перпендикуляр на ось X
            plt.plot([Icr, Icr], [line1(Icr), 0], 'k--')

    plt.title(title)
    plt.legend()
    plt.show()

# Построение графиков с аппроксимацией
approximate_and_plot(datasets[0][0], datasets[0][1], datasets[0][2], start_points=4, additional_lines=[([0.505, 0.973], [0.781, 0.768])])
approximate_and_plot(datasets[1][0], datasets[1][1], datasets[1][2], start_points=4, additional_lines=[([0.24, 0.672], [0.870, 0.862])])
approximate_and_plot(datasets[2][0], datasets[2][1], datasets[2][2], start_points=4, additional_lines=[([0.484, 1.156], [0.935, 0.860])])
approximate_and_plot(datasets[3][0], datasets[3][1], datasets[3][2], start_points=2, additional_lines=[([0.535, 0.731], [0.722, 0.714])])
