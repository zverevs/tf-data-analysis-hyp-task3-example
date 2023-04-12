import pandas as pd
import numpy as np


chat_id = 235789175 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    pval = stats.mannwhitneyu(x, y, alternative='greater')[1]
    # Не меняйте название функции и её аргументы
    alpha = 0.03

    if pval < alpha:
        return True
    else:
        return False
