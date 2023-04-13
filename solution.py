import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import mannwhitneyu

chat_id = 235789175 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    pval = stats.mannwhitneyu(x, y, alternative='two-sided')[1]
    # Не меняйте название функции и её аргументы
    alpha = 0.03

    if pval < alpha:
        return True
    else:
        return False
