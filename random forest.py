# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
from sklearn import ensemble, preprocessing, metrics
from talib import abstract

# 載入資料
df = pd.read_csv('C:/Users/yujie/OneDrive/桌面/TXF_data/TXF1-日-成交價_20years.csv')
data = df[['Date', 'Open', 'High', 'Low', 'Close', 'TotalVolume']]
data.columns = ['date', 'open', 'high', 'low', 'close', 'totalvolume']
data = data.set_index(['date'])
#print(data.head())

ta_list = ['MACD','RSI','MOM','STOCH']
for x in ta_list:
    output = eval('abstract.'+x+'(data)')
    output.name = x.lower() if type(output) == pd.core.series.Series else None
    data = pd.merge(data, pd.DataFrame(output), left_on = data.index, right_on = output.index)
    data = data.set_index('key_0')
    data.index.name = 'date'
#print(data.head())
    
# 判斷漲跌
s = (data.close - data.close.shift(1))/data.close.shift(1)  #漲跌幅 = 漲跌值 / 昨日收盤價
data['s']=s
trend=[]
for i in range(len(data)):   
    if(data['s'][i] > 0.0025):
        trend.append(1)
        #data['day_trend'][i] = 1
    elif(data['s'][i]< -0.0025):
        trend.append(-1)
        #data['day_trend'][i] = -1
    else:
        trend.append(0)
        #data['day_trend'][i] = 0
data['day_trend'] = trend

#print(data['day_trend'].head())

# 檢查資料有無缺值，刪除空值
data.isnull().sum()
data = data.dropna()

# 將樣本分類
n_train = 500
n_records = int(len(data))
for n in range(n_train, n_records, 200):
	train, test = data[0:n], data[n:n+200]
# 訓練樣本再分成目標序列 y 以及因子矩陣 X
train_X = train.drop(['s', 'day_trend'], axis = 1)
train_y = train.day_trend
# 測試樣本再分成目標序列 y 以及因子矩陣 X
test_X = test.drop(['s', 'day_trend'], axis = 1)
test_y = test.day_trend

# 建立 random forest 模型
forest = ensemble.RandomForestClassifier(n_estimators = 100)
forest_fit = forest.fit(train_X, train_y)

# 預測
test_y_predicted = forest.predict(test_X)
#print(test_y_predicted)

# 績效
accuracy = metrics.accuracy_score(test_y, test_y_predicted)
print("準確率:", accuracy)
#print("準確率:", forest.score(test_X, test_y))