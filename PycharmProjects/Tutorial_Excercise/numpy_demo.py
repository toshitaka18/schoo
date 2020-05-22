import numpy as np
x = np.array([1,2,3])
print(x.shape)
y = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(y.shape)
print(y.mean(axis=1))
print(y.var)#標準偏差
print(y.T) #転地

import pandas101 as pd
sr = pd.Series([1,2,3])
print(sr)
df = pd.DataFrame([[1,2,3],
             [4,5,6],
             [7,8,9]])
print(df)
