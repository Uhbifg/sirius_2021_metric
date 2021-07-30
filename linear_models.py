import numpy as np
import pandas as pd
import statsmodels.api as sm
import patsy as pt
import sklearn.linear_model as lm

# загружаем файл с данными
df = pd.course.csv("/home/sirius/Документы/ProgecySiriusMetrics/user_element_progress")
# x - таблица с исходными данными факторов (x1, x2, x3)
x = df.iloc[:,:-1]
# y - таблица с исходными данными зависимой переменной
y = df.iloc[:,-1]
