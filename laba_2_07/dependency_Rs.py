import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных из Excel файла
file_path = 'lab_07.xlsx'
data = pd.read_excel(file_path)


R = data.iloc[3:19, 3].astype(float)  # значения Rs, Ом из столбца с индексом 3
T = data.iloc[3:19, 5].astype(float)  # значения t, oC из столбца с индексом 5

# Линейная регрессия методом наименьших квадратов
coefficients = np.polyfit(R, T, 1)
polynomial = np.poly1d(coefficients)

# Предсказание значений R на основе T
R_lin = np.linspace(min(T), max(R), 100)  # Расширение диапазона
T_lin = polynomial(R_lin)

# Построение графика зависимостиln Rs = ln Rs (1/Т)
plt.figure(figsize=(10, 6))
plt.plot(R_lin, T_lin, linestyle='-', color='b',)
plt.scatter(R, T, color='r', marker='o', )
plt.title('ln Rs = ln Rs (1/Т)')
plt.xlabel('Rs')
plt.ylabel('1/Т')
plt.grid(True)
plt.legend()
plt.show()
