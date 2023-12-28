import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.get_dummies((pd.DataFrame({'whoAmI':lst})))
data.head()

""" С использованием функции pd.get_dummies()"""