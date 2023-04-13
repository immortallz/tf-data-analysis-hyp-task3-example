import pandas as pd
import numpy as np

from statsmodels.stats.weightstats import ztest

chat_id = 388568881 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    if ztest(x, value = 500, alternative = 'larger')[1] > 0.04:
        return False
    else:
        return True
