# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:25:57 2020

@author: yujie
"""
# In[1]
import numpy as np
import pandas as pd
from sklearn import ensemble, preprocessing, metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from datetime import datetime

# 載入資料
df = pd.read_csv('C:/Users/yujie/.spyder-py3/spyder_workplace/winnerProject/TXF1_日.csv')
data = df[[' <Open>', ' <High>', ' <Low>', ' <Close>', ' <Volume>']]

dataDate = pd.to_datetime(df['<Date>'])
dataDate.to_csv('index_copy.csv', index=False, header=True)
#print(data)
# In[2]

import pandas as pd
import talib
from talib import abstract

data = data.astype('float')

# 技術面資料
# 改成 TA-Lib 可以辨識的欄位名稱

data.rename(columns={" <Open>": "open", " <High>": "high", " <Low>":"low", " <Close>":"close", " <Volume>":"volume"} , inplace=True)
# 短期設3、5日
data['MA5'] = talib.MA(data['close'], timeperiod=3)  
data['MA10'] = talib.MA(data['close'], timeperiod=5)
#data['MA20'] = talib.MA(data['close'], timeperiod=20)
data['RSI5'] = talib.RSI(data['close'], timeperiod=3) #RSI的天数一般是6、12、24
data['RSI10'] = talib.RSI(data['close'], timeperiod=5)
#data['RSI20'] = talib.RSI(data['close'], timeperiod=20)  
data['MOM5'] = talib.MOM(data['close'], timeperiod=3)
data['MOM10'] = talib.MOM(data['close'], timeperiod=5)
#data['MOM20'] = talib.MOM(data['close'], timeperiod=20)
data['MACD'],data['MACDSIGNAL'],data['MACDHIST'] = talib.MACD(data['close'], fastperiod=3, slowperiod=6, signalperiod=4)
#data["upperband"], data["middleband"], data["lowerband"] = talib.BBANDS(data['close'], timeperiod=5, nbdevup=2, nbdevdn=2,matype=0)
data['k'], data['d'] = talib.STOCH(data['high'], data['low'], data['close'])
#data['WILLR5'] = talib.WILLR(data['high'], data['low'], data['close'], timeperiod=3)
#data['WILLR10'] = talib.WILLR(data['high'], data['low'], data['close'], timeperiod=5)
#data['OBV']= talib.OBV(data['close'], data['volume'])
# In[3]

# 將時間跟原資料合併(?

a = pd.read_csv('index_copy.csv')
a = a.dropna()
a['Datetime'] = pd.to_datetime(a['<Date>'])

data = data.merge(a, left_index=True, right_index=True)
data = data.set_index(['Datetime'])

del data['<Date>']
data.index.rename('date', inplace=True)

# In[4]

# 判斷漲跌 2, 0, 1
#s = (data.close - data.close.shift(5))/data.close.shift(5)  #漲跌幅 = 漲跌值 / 昨日收盤價
s = (data.close.shift(-1) - data.close)/data.close #一日後漲跌幅
data['s']=s
trend=[]
for i in range(len(data)): 
    if(data['s'][i] > 0.001):
        trend.append(2)
        #data['day_trend'][i] = 1
    elif(data['s'][i]< -0.0027):
        trend.append(1)
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
def run_randomForests(DataType, X_train, X_test, y_train, y_test, X_pred, y_pred):
    # RF
    rf = RandomForestClassifier(n_estimators=100, random_state=39 ,max_depth = 5,min_samples_split=10, min_samples_leaf=5, n_jobs=-1)
    
    # Train
    rf.fit(X_train, y_train)
    #pred = rf.predict_proba(X_train)
    pred = rf.predict(X_train)
    TrainAccuracy = accuracy_score(y_train, pred)
    
    # Test
    #pred = rf.predict_proba(X_test)
    pred2 = rf.predict(X_test)
    TestAccuracy = accuracy_score(y_test, pred2)
    
    #confusion = confusion_matrix(y_true=y_test, y_pred=pred2)# 混淆矩陣
    accuracy = accuracy_score(y_true=y_test, y_pred=pred2)
    print('RF accuracy: {0:1.2f}'.format(accuracy))
    #print(confusion)
    
    # predict
    
    #pred = rf.predict_proba(X_pred)
    pred3 = rf.predict(X_pred)
    PredTestAccuracy = accuracy_score(y_pred, pred3)
    #confusion = confusion_matrix(y_true=y_pred, y_pred=pred3)# 混淆矩陣
    accuracy = accuracy_score(y_true=y_pred, y_pred=pred3)
    print('RF pred accuracy: {0:1.2f}'.format(accuracy))
    #print(confusion)
    return DataType, TrainAccuracy, TestAccuracy, PredTestAccuracy, pred2, X_test.index, X_test['open'], X_test['high'], X_test['low'], X_test['close'], X_test['volume']
# In[6]
####### 處理資料 #######
# 將樣本分類
data = data[data.index > '1998-07-22']
data = data[data.index < '2019-12-31']
inv=[]
start_year = 2000
end_year = 2019
interval = 7
months=['01','02','03','04','05','06','07','08','09','10','11','12']
k = 0
for y in range(start_year, end_year-interval+1):
    for month in months:
        print('#' * 50)
        ####
        begin_time = str(start_year+k)+'-'+month
        end_time = str(y+interval)+'-'+months[int(month)-1]
        if int(months[int(month)-1]) == 12:
            if y+interval == end_year:
                pred_time = str(y+interval)+'-12'
            else:
                pred_time = str(y+interval+1)+'-01'
        else:
            pred_time = str(y+interval)+'-'+months[int(month)]
        print('DataStart:',begin_time,'DataEnd:', end_time,'PredData:', pred_time)

        # 產生區間年度資料集
        #print(begin_time, end_time)
        data_split = data['%s'%(begin_time):'%s'%(end_time)].copy()
        data_pred = data['%s'%(pred_time)].copy()
        ###########################################################

        # 訓練樣本再分成目標序列 y 以及因子矩陣 X
        X = data_split.drop(['s', 'day_trend'], axis = 1)
        Y = data_split.day_trend
        X_pred = data_pred.drop(['s', 'day_trend'], axis = 1)
        y_pred = data_pred.day_trend
        X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size =0.9
                                                            ,shuffle=False) # 2*len(X) // 3 

        X_train= pd.DataFrame(X_train)
        X_test= pd.DataFrame(X_test)
        
        X_train_original = pd.DataFrame(X_train.copy())
        X_test_original = pd.DataFrame(X_test.copy())
        print('完全未處理：',X_train_original.shape, X_test_original.shape)
        # a5是predict測試集的結果
        # a6是test的index
        a1, a2, a3, a4, a5, a6, a10, a11, a12, a13, a14= run_randomForests('original',X_train_original,
                         X_test_original,
                         y_train, y_test, X_pred, y_pred)
        print('RF train: {0:1.2f}, test: {1:1.2f}'.format(a2, a3))
        print('RF Pred:', a4)
        #inv.append([X_test.index[0].strftime('%Y'),X_train.index[0].strftime('%Y%m%d'), X_test.index[0].strftime('%Y%m%d'),X_pred.index[0].strftime('%Y%m%d'),a1,a2,a3,a4])
        
    k+=1
    print('#' * 50)
#######################
'''
# In[7]
## 分析
analyics=pd.DataFrame(inv)
analyics.columns=['Year', 'TrainStart', 'TestStart','PredStart','AlogType',
                  'TrainAccuracy', 'TestAccuracy', 'PredTestAccuracy']

# In[8]
mask1 = analyics['AlogType']=='original'
mask2 = analyics['Year'] >='2000'
mask3 = analyics['Year'] <'2020'
analyics = analyics[mask1 & mask2 & mask3]
analyics

# In[9]
analyics.to_csv()
'''
# In[10]

# In[11]
# 將結果寫入csv
df=pd.DataFrame({'date': a6, 'open': a10, 'high': a11, 'low': a12, 'close': a13, 'volume': a14, 'predict': a5})
df.to_csv("ouo.csv", index=False)
