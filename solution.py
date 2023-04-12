import pandas as pd
import numpy as np


chat_id = 235789175 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    pval = MMD(compute_kernel="rbf", gamma=1).test(x, y)[1]
    alpha = 0.08 
    
    if pval < alpha:
        return True
    else:
        return False
