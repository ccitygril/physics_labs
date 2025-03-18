import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных из Excel файла
file_path = 'лаб2.6.xlsx'
data = pd.read_excel(file_path)

# Извлечение данных из столбцов с индексами 3 и 4
B = data.iloc[1:19, 4].astype(float)  # значения B из столбца с индексом 4
H = data.iloc[1:19, 3].astype(float)  # значения H из столбца с индексом 3

# Линейная регрессия методом наименьших квадратов
coefficients = np.polyfit(B, H, 1)
polynomial = np.poly1d(coefficients)

# Предсказание значений H на основе B
B_lin = np.linspace(min(B), max(B), 100)
H_lin = polynomial(B_lin)

# Построение графика зависимости H(B)
plt.figure(figsize=(10, 6))
plt.plot(B_lin, H_lin, linestyle='-', color='b',)
plt.scatter(B, H, color='r', marker='o', )
plt.title('Зависимость H(B)')
plt.xlabel('B')
plt.ylabel('H')
plt.grid(True)
plt.legend()
plt.show()
