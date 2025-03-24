import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных из Excel файла
file_path = 'lab_07.xlsx'
data = pd.read_excel(file_path)


R = data.iloc[3:19, 2].astype(float)  # значения Rm, Ом из столбца с индексом 2
T = data.iloc[3:19, 1].astype(float)  # значения t, oC из столбца с индексом 1

# Линейная регрессия методом наименьших квадратов
coefficients = np.polyfit(R, T, 1)
polynomial = np.poly1d(coefficients)

# Предсказание значений R на основе T
R_lin = np.linspace(950, max(R), 100)  # Расширение диапазона
T_lin = polynomial(R_lin)

# Построение графика зависимости Rm = Rm(t)
plt.figure(figsize=(10, 6))
plt.plot(R_lin, T_lin, linestyle='-', color='b',)
plt.scatter(R, T, color='r', marker='o', )
plt.title('Rm = Rm(t)')
plt.xlabel('Rm')
plt.ylabel('t')
plt.ylim(bottom=-1)
plt.xlim(left=950)
plt.grid(True)
plt.legend()
plt.show()
