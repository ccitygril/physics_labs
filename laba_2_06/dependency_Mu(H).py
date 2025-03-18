import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

file_path = 'лаб2.6.xlsx'
data = pd.read_excel(file_path)


Mu = data.iloc[1:19, 5].astype(float)  # значения Mu из столбца с индексом 5
H = data.iloc[1:19, 3].astype(float)  # значения H из столбца с индексом 3

def logistic_function(H, L, k, H0):
    return L / (1 + np.exp(-k * (H - H0)))

# Аппроксимация данных
params, _ = curve_fit(logistic_function, H, Mu, p0=[max(Mu), 1, np.median(H)])
L, k, H0 = params


H_fit = np.linspace(min(H), max(H), 100)
Mu_fit = logistic_function(H_fit, L, k, H0)

plt.figure(figsize=(10, 6))
plt.plot(H_fit, Mu_fit, linestyle='-', color='b',)
plt.scatter(H, Mu, color='r', marker='o',)
plt.xlabel('H')
plt.ylabel('μ')
plt.title('Зависимость μ(H)')
plt.grid(True)
plt.legend()
plt.show()