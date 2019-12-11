# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:52:25 2019

@author: USER
"""

import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
import graphviz 
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from talib import abstract
# 要計算混淆矩陣的話，要從 metrics 裡匯入 confusion_matrix
from sklearn.metrics import confusion_matrix
# 要計算 AUC 的話，要從 metrics 裡匯入 roc_curve 以及 auc
from sklearn.metrics import roc_curve, auc

#start = dt.datetime(2019, 10, 5, 3, 40, 0)
#end = dt.datetime(2019, 10, 5, 5, 0, 0)
df = pd.read_csv('C:/Users/USER/Desktop/TXF1_1_min.csv')
data = df[['<Open>', '<High>', '<Low>', '<Close>', 'Volume']]
data.columns = ['open','high','low','close','volume']
data = data.astype('float')
# 隨意試試看這幾個因子好了
ta_list = ['MACD','RSI','MOM','STOCH']
# 快速計算與整理因子
for x in ta_list:
    output = eval('abstract.'+x+'(data)')
    output.name = x.lower() if type(output) == pd.core.series.Series else None
    data = pd.merge(data, pd.DataFrame(output), left_on = data.index, right_on = output.index)
    data = data.set_index('key_0')
#print(data)
    
# 五日後漲標記 1，反之標記 0
data['min_trend'] = np.where(data.close.shift(-1) > data.close, 1, 0)

# 檢查資料有無缺值
data.isnull().sum()
# 最簡單的作法是把有缺值的資料整列拿掉
data = data.dropna()

# 決定切割比例為 70%:30%
split_point = int(len(data)*0.7)
# 切割成學習樣本以及測試樣本
train = data.iloc[:split_point,:].copy()
test = data.iloc[split_point:-1,:].copy()

# 訓練樣本再分成目標序列 y 以及因子矩陣 X
train_X = train.drop('min_trend', axis = 1)
train_y = train.min_trend
# 測試樣本再分成目標序列 y 以及因子矩陣 X
test_X = test.drop('min_trend', axis = 1)
test_y = test.min_trend

# 叫出一棵決策樹
model = DecisionTreeClassifier(max_depth = 7)

# 讓 A.I. 學習
model.fit(train_X, train_y)

# 讓 A.I. 測驗，prediction 存放了 A.I. 根據測試集做出的預測
prediction = model.predict(test_X)

dot_data = export_graphviz(model, out_file = None,
                           feature_names = train_X.columns,
                           filled = True, rounded = True,
                           class_names = True,
                           special_characters = True)
graph = graphviz.Source(dot_data)
graph.render("dt_test", view = True)


# 混淆矩陣
print(confusion_matrix(test_y, prediction))
print('========')

# 準確率
print(model.score(test_X, test_y))
print('========')

# 計算 ROC 曲線
false_positive_rate, true_positive_rate, thresholds = roc_curve(test_y, prediction)

# 計算 AUC 面積
print(auc(false_positive_rate, true_positive_rate))
