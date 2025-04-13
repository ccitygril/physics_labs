import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных из Excel файла
file_path = 'data.xlsx'
data = pd.read_excel(file_path)

# Прямое измерение
B1 = data.iloc[3:22, 0].astype(float)
A1 = data.iloc[3:22, 1].astype(float)

# Обратное измерение
B2 = data.iloc[3:18, 2].astype(float)
A2 = data.iloc[3:18, 3].astype(float) * 100

# Аппроксимация квадратичной функцией
coefficients = np.polyfit(B2, A2, 2)  # 2 - степень полинома
a, b, c = coefficients
# Построение графика
x_fit = np.linspace(min(B2), max(B2), 100)
y_fit = np.polyval(coefficients, x_fit)


plt.figure(figsize=(10, 6))
plt.plot(B1, A1, label='Ge Forward', marker='o')
plt.plot(B2, A2, label='Ge Reverse', marker='o')
plt.title('Вольт-Амперная Характеристика (ВАХ) Ge Диода')
plt.xlabel('Напряжение (В)')
plt.ylabel('Ток (мА)')
plt.legend()
plt.grid(True)
plt.show()
