import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv('mtcars.csv')

col_imp = ['cyl',
            'disp', 'hp', 'drat',
            'wt', 'qsec', 'vs',
            'am', 'gear', 'carb']

X = data.iloc[:, 2:]
Y = data.iloc[:, 1]


lin_model = LinearRegression().fit(X, Y)

def predict(dict_values, col_imp = col_imp, linear_mod = lin_model):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1,-1)
    y_pred = linear_mod.predict(x)[0]
    return y_pred

