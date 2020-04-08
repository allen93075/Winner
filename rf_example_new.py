# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:25:57 2020

@author: yujie
"""
# In[1]
import numpy as np
import pandas as pd
from sklearn import ensemble, preprocessing, metrics
from datetime import datetime

# 載入資料
df = pd.read_csv('TXF1-日-成交價_20years.csv')
data = df[['Open', 'High', 'Low', 'Close', 'TotalVolume']]
#print(data)
# In[2]

import pandas as pd
import talib
from talib import abstract

data = data.astype('float')

# 技術面資料
# 改成 TA-Lib 可以辨識的欄位名稱

data.rename(columns={"Open": "open", "High": "high", "Low":"low", "Close":"close", "TotalVolume":"volume"} , inplace=True)

data['MA5'] = talib.MA(data['close'], timeperiod=5)  
data['MA10'] = talib.MA(data['close'], timeperiod=10)
data['MA20'] = talib.MA(data['close'], timeperiod=20)
data['RSI5'] = talib.RSI(data['close'], timeperiod=5) #RSI的天数一般是6、12、24
data['RSI10'] = talib.RSI(data['close'], timeperiod=10)  
data['RSI20'] = talib.RSI(data['close'], timeperiod=20)  
data['MOM5'] = talib.MOM(data['close'], timeperiod=5)
data['MOM10'] = talib.MOM(data['close'], timeperiod=10)
data['MOM20'] = talib.MOM(data['close'], timeperiod=20)
data['MACD'],data['MACDSIGNAL'],data['MACDHIST'] = talib.MACD(data['close'], fastperiod=5, slowperiod=10, signalperiod=4)
data["upperband"], data["middleband"], data["lowerband"] = talib.BBANDS(data['close'], timeperiod=5, nbdevup=2, nbdevdn=2,matype=0)
data['k'], data['d'] = talib.STOCH(data['high'], data['low'], data['close'])
data['WILLR5'] = talib.WILLR(data['high'], data['low'], data['close'], timeperiod=5)
data['WILLR10'] = talib.WILLR(data['high'], data['low'], data['close'], timeperiod=10)
data['OBV']= talib.OBV(data['close'], data['volume'])
# In[3]

# 將時間跟原資料合併(?

a = pd.read_csv('indexs.csv')
a = a.dropna()
a['Datetime'] = pd.to_datetime(a['Date'])

data = data.merge(a, left_index=True, right_index=True)
data = data.set_index(['Datetime'])

del data['Date']
data.index.rename('Date', inplace=True)

# In[4]

# 判斷漲跌 1, 0, -1
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
#print(data)

# In[5]

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


# In[6]
# 建立 random forest 模型
forest = ensemble.RandomForestClassifier(n_estimators = 100)
forest_fit = forest.fit(train_X, train_y)

# 預測
test_y_predicted = forest.predict(test_X)
#print(test_y_predicted)

# In[7]
# 績效
accuracy = metrics.accuracy_score(test_y, test_y_predicted)
print("準確率:", accuracy)
'''
from sklearn.metrics import roc_curve, auc
# 計算 ROC 曲線
false_positive_rate, true_positive_rate, thresholds = roc_curve(test_y, test_y_predicted)
# 計算 AUC 面積
print(auc(false_positive_rate, true_positive_rate))
'''
# In[8]
# 將結果寫入csv

df=pd.DataFrame({'predict': test_y_predicted})
df.to_csv('ou.csv',index=False)
