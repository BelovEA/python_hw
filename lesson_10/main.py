import pandas as pd
import numpy as np
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


dummies = pd.get_dummies(data['whoAmI'])

data_onehot = pd.concat([data, dummies], axis=1)

data_onehot.drop('whoAmI', axis=1, inplace=True)
print(data_onehot.head())
