import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot = pd.concat([pd.Series(data['whoAmI'] == 'robot').astype(int), pd.Series(data['whoAmI'] == 'human').astype(int)], axis=1)
one_hot.columns = ['is_robot', 'is_human']
data = pd.concat([data, one_hot], axis=1)
data.head(10)
""" Без использования функции pd.get_dummies() """