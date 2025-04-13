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
# u = 7v
Il7_1 = data.iloc[2:10, 0].astype(float)
Ia7_1 = data.iloc[2:10, 1].astype(float)

# u = 8v
Il8 = data.iloc[2:13, 2].astype(float)
Ia8 = data.iloc[2:13, 3].astype(float)

# u = 9v
Il9 = data.iloc[2:13, 4].astype(float)
Ia9 = data.iloc[2:13, 5].astype(float)

# u = 6v
Il6 = data.iloc[2:11, 6].astype(float)
Ia6 = data.iloc[2:11, 7].astype(float)

# Аппроксимация данных
def approximate_and_plot(Il, Ia, title):
    params, _ = curve_fit(logistic_function, Il, Ia, p0=[1, np.mean(Il), 1])
    plt.figure(figsize=(6, 4))
    plt.plot(Il, Ia, 'bo', label='Data')
    plt.plot(Il, logistic_function(Il, *params), 'r-', label='Fitted Logistic Function')
    plt.xlabel('Il')
    plt.ylabel('Ia')
    plt.title(title)
    plt.legend()
    plt.show()

# Построение графиков с аппроксимацией
approximate_and_plot(Il7_1, Ia7_1, 'u = 7v')
approximate_and_plot(Il8, Ia8, 'u = 8v')
approximate_and_plot(Il9, Ia9, 'u = 9v')
approximate_and_plot(Il6, Ia6, 'u = 6v')
