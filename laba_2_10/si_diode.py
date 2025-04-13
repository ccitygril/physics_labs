import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из Excel файла
file_path = 'data.xlsx'
data = pd.read_excel(file_path)

# Извлечение данных для Ge и Si диодов
data_ge_forward = data.iloc[2:5, [0, 1]].astype(float)
data_ge_reverse = data.iloc[2:5, [2, 3]].astype(float)
data_si_forward = data.iloc[2:5, [4, 5]].astype(float)
data_si_reverse = data.iloc[2:5, [6, 7]].astype(float)

# Построение графиков
plt.figure(figsize=(12, 8))

# График для Ge диода
plt.subplot(2, 1, 1)
plt.plot(data_ge_forward.iloc[:, 0], data_ge_forward.iloc[:, 1], label='Ge Forward', marker='o')
plt.plot(data_ge_reverse.iloc[:, 0], data_ge_reverse.iloc[:, 1], label='Ge Reverse', marker='o')
plt.title('Вольт-Амперная Характеристика (ВАХ) Ge Диода')
plt.xlabel('Напряжение (В)')
plt.ylabel('Ток (мА)')
plt.legend()
plt.grid(True)

# График для Si диода
plt.subplot(2, 1, 2)
plt.plot(data_si_forward.iloc[:, 0], data_si_forward.iloc[:, 1], label='Si Forward', marker='o')
plt.plot(data_si_reverse.iloc[:, 0], data_si_reverse.iloc[:, 1], label='Si Reverse', marker='o')
plt.title('Вольт-Амперная Характеристика (ВАХ) Si Диода')
plt.xlabel('Напряжение (В)')
plt.ylabel('Ток (мА)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()