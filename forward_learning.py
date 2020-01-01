# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 19:20:34 2019

@author: USER
"""
import pandas as pd
import numpy as np
import graphviz
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from talib import abstract

df = pd.read_csv('C:/Users/USER/Desktop/TXF1-日-成交價_20years.csv')
data = df[['Date', 'Open', 'High', 'Low', 'Close', 'TotalVolume']]
data.columns = ['date', 'open', 'high', 'low', 'close', 'totalvolume']
data = data.set_index(['date'])
'''
TIME = data['date'] + ' ' + data['time']
TIME = pd.to_datetime(TIME)
#data = data.drop(['date','time'], axis=1)
'''
#data = data.astype('float')
# 隨意試試看這幾個因子好了
ta_list = ['MACD','RSI','MOM','STOCH']
# 快速計算與整理因子
for x in ta_list:
    output = eval('abstract.'+x+'(data)')
    output.name = x.lower() if type(output) == pd.core.series.Series else None
    data = pd.merge(data, pd.DataFrame(output), left_on = data.index, right_on = output.index)
    data = data.set_index('key_0')
    data.index.name = 'date'
# 一日後漲標記 1，反之標記 0
data['day_trend'] = np.where(data.close.shift(-1) > data.close, 1, 0)
#print(data['day_trend'])
# 檢查資料有無缺值
data.isnull().sum()
# 最簡單的作法是把有缺值的資料整列拿掉

data = data.dropna()
'''
# 決定切割比例為 70%:30%
split_point = int(len(data)*0.7)
# 切割成學習樣本以及測試樣本
train = data.iloc[:split_point,:].copy()
test = data.iloc[split_point:-1,:].copy()
'''
n_train = 500
n_records = int(len(data))
for i in range(n_train, n_records, 200):
	train, test = data[0:i], data[i:i+200]
# 訓練樣本再分成目標序列 y 以及因子矩陣 X
train_X = train.drop('day_trend', axis = 1)
train_y = train.day_trend
# 測試樣本再分成目標序列 y 以及因子矩陣 X
test_X = test.drop('day_trend', axis = 1)
test_y = test.day_trend

# 叫出一棵決策樹
model = DecisionTreeClassifier(max_depth = 3)

# 讓 A.I. 學習
model.fit(train_X, train_y)
 
# 讓 A.I. 測驗，prediction 存放了 A.I. 根據測試集做出的預測
prediction = model.predict(test_X)

dot_data = export_graphviz(model, out_file = None,
                           feature_names = train_X.columns,
                           filled = True, rounded = True,
                           class_names = True,
                           special_characters = True)
#graph = graphviz.Source(dot_data)
#graph.render("dt_test_wf", view = True)
'''
# 儲存模型
filename = 'Decision_Tree_model_WF.sav'
pickle.dump(model, open(filename, 'wb'))
'''

print("準確率:", model.score(test_X, test_y))
#print('========')
#print(data)