import pandas as pd
import numpy as np


chat_id = 388568881 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    if 1.04 * np.median(x) > 500:
      return False
    else:
      return True
