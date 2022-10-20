import os
import pandas as pd
import numpy as np
s = 'https://archive.ics.uci.edu/ml/'\
    'machine-learning-databases/iris/iris.data'

try:
    df = pd.read_csv(s,
                    header=None,
                    encoding='utf-8')
    """print("attempting to print df=", df)"""

except HTTPError:
    print("HTTP Error. attempting to read locally. ")
    s = 'iris.data'
    """print('From local Iris path:', s)"""
    df = pd.read_csv(s,
                     header=None,
                     encoding='utf-8')

 
y = df.iloc[0:100, 4].values


y = np.where(y== 'Iris-setosa', 0, 1)

X = df.iloc[0:100, [0,2]].values

