# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 20:18:53 2019

@author: user
"""

from sklearn.neural_network import MLPClassifier
#from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import talib
from talib import abstract
'''
# 透過『get_functions』語法，查看 TA-Lib 提供的所有技術指標的代碼
all_ta_label = talib.get_functions()
# 看一下清單
all_ta_label
# 共有 158 個技術指標可以運算
len(all_ta_label)
'''
df = pd.read_csv('E:\畢業專題\TXF1-日-成交價_20years.csv')
data = df[['Date', 'Open', 'High', 'Low', 'Close', 'TotalVolume']]
data.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
data = data.set_index(['date'])
ta_list = ['MACD','RSI','MOM','STOCH']
# 快速計算與整理因子
for x in ta_list:
    output = eval('abstract.'+x+'(data)')
    output.name = x.lower() if type(output) == pd.core.series.Series else None
    data = pd.merge(data, pd.DataFrame(output), left_on = data.index, right_on = output.index)
    data = data.set_index('key_0')
    data.index.name = 'date'

#print(data)

# 一日後漲標記 1，反之標記 0
data['day_trend'] = np.where(data.close.shift(-1) > data.close, 1, 0)
#print(data['day_trend'])
# 檢查資料有無缺值
data.isnull().sum()
# 最簡單的作法是把有缺值的資料整列拿掉
data = data.dropna()

# 決定切割比例為 70%:30%
split_point = int(len(data)*0.8)
# 切割成學習樣本以及測試樣本
train = data.iloc[:split_point,:].copy()
test = data.iloc[split_point:-5,:].copy()
# 訓練樣本再分成目標序列 y 以及因子矩陣 X
train_X = train.drop('day_trend', axis = 1)
train_y = train.day_trend

# 測試樣本再分成目標序列 y 以及因子矩陣 X
test_X = test.drop('day_trend', axis = 1)
test_y = test.day_trend


mlp =MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
mlp.fit(train_X,train_y)

predict_train = mlp.predict(train_X)
predict_test = mlp.predict(test_X)

from sklearn.metrics import classification_report,confusion_matrix
score(test_X, test_y, sample_weight=None)
print(confusion_matrix(train_y,predict_train))
print(classification_report(train_y,predict_train))
print(confusion_matrix(test_y,predict_test))
print(classification_report(test_y,predict_test))


#mlp.fit(X_train, y_train)

'''
X = [[0., 0.,0.], [1., 1.,1.],[2., 2.,2.]]
y = [0, 1, 2]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,3), random_state=1)
clf.fit(X, y)    
clf.predict([[2., 2., 2.], [-1., -2.,0.],[1., 1.,0.]])
'''