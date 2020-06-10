# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:25:57 2020

@author: yujie
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from datetime import datetime
import talib
from talib import abstract

# In[1]
#載入資料
def loadFile(path):
    df = pd.read_csv(path)
    data = df[[' <Open>', ' <High>', ' <Low>', ' <Close>', ' <Volume>']]

    dataDate = pd.to_datetime(df['<Date>'])
    dataDate.to_csv('index_copy.csv', index=False, header=True)
    return data
# In[2]
import pickle
def run_randomForests(DataType, X_train, X_test, y_train, y_test):
    # RF
    rf = RandomForestClassifier(n_estimators=100, random_state=39, max_depth = 5, min_samples_split=10, min_samples_leaf=5, n_jobs=-1)
    
    # Train
    rf.fit(X_train, y_train)
    pred = rf.predict(X_train)
    TrainAccuracy = accuracy_score(y_train, pred)
    
    # Test
    pred2 = rf.predict(X_test)
    TestAccuracy = accuracy_score(y_test, pred2)
    
    accuracy = accuracy_score(y_true=y_test, y_pred=pred2)
    print('RF accuracy: {0:1.2f}'.format(accuracy))
    
    with open('randomforest.pickle','wb') as f:
        pickle.dump(rf, f)
    return DataType, TrainAccuracy, TestAccuracy, pred2, X_test.index, X_test['open'], X_test['high'], X_test['low'], X_test['close'], X_test['volume']
# In[3]
def rf_main(data):
    data = data.astype('float')
    
    # 技術面資料
    # 改成 TA-Lib 可以辨識的欄位名稱
    
    data.rename(columns={" <Open>": "open", " <High>": "high", " <Low>":"low", " <Close>":"close", " <Volume>":"volume"} , inplace=True)
    # 短期設3、5日
    data['MA5'] = talib.MA(data['close'], timeperiod=5)  
    data['MA10'] = talib.MA(data['close'], timeperiod=10)
    data['MA20'] = talib.MA(data['close'], timeperiod=20)
    data['RSI5'] = talib.RSI(data['close'], timeperiod=5)
    data['RSI10'] = talib.RSI(data['close'], timeperiod=10)  
    data['RSI20'] = talib.RSI(data['close'], timeperiod=20)
    data['MACD'],data['MACDSIGNAL'],data['MACDHIST'] = talib.MACD(data['close'], fastperiod=5, slowperiod=10, signalperiod=4)
    data['k'], data['d'] = talib.STOCH(data['high'], data['low'], data['close'])
    data['OBV']= talib.OBV(data['close'], data['volume'])
# In[4]   
    # 將時間跟原資料合併
    
    a = pd.read_csv('index_copy.csv')
    a = a.dropna()
    a['Datetime'] = pd.to_datetime(a['<Date>'])
    
    data = data.merge(a, left_index=True, right_index=True)
    data = data.set_index(['Datetime'])
    
    del data['<Date>']
    data.index.rename('date', inplace=True)
    
# In[5]
    
    # data['week_trend'] = np.where(data.close.shift(-5) > data.close, 1, 0)
    # 判斷漲跌 2, 0, 1
    # 漲跌幅 = 漲跌值 / 昨日收盤價
    s = (data.close.shift(-5) - data.close)/data.close # 一日後漲跌幅
    data['s']=s
    trend=[]
    for i in range(len(data)): 
        if(data['s'][i] > 0.002):
            trend.append(2)
        elif(data['s'][i]< -0.002):
            trend.append(1)
        else:
            trend.append(0)
    data['day_trend'] = trend
    
    # 檢查資料有無缺值，刪除空值
    data.isnull().sum()
    data = data.dropna()
    #print(data)
# In[6]
    ####### 處理資料 #######
    # 將樣本分類
    start_year = 2000
    end_year = 2019
    interval = 3  # 訓練週期
    months=['01','02','03','04','05','06','07','08','09','10','11','12']
    k = 0
    for y in range(start_year, end_year-interval+1):
        for month in months:
            print('#' * 50)
            ####
            begin_time = str(start_year+k)+'-'+month
            end_time = str(y+interval)+'-'+months[int(month)-1]
            
            print('DataStart:', begin_time,'DataEnd:', end_time)
    
            # 產生區間年度資料集
            data_split = data['%s'%(begin_time):'%s'%(end_time)].copy()
            #print(data['%s'%(begin_time):'%s'%(end_time)])
            ###########################################################
    
            # 訓練樣本再分成目標序列 y 以及因子矩陣 X
            X = data_split.drop(['s', 'day_trend'], axis = 1)
            Y = data_split.day_trend
            
            X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size =0.3
                                                                ,random_state = 0)
    
            X_train= pd.DataFrame(X_train)
            X_test= pd.DataFrame(X_test)
            
            X_train_original = pd.DataFrame(X_train.copy())
            X_test_original = pd.DataFrame(X_test.copy())
            print('完全未處理：',X_train_original.shape, X_test_original.shape)
            # a5是predict測試集的結果
            # a6是test的index
            a1, a2, a3, a4, a5, a10, a11, a12, a13, a14= run_randomForests('original',X_train_original,
                             X_test_original,
                             y_train, y_test)
            print('RF train: {0:1.2f}, test: {1:1.2f}'.format(a2, a3))
        k+=1
        print('#' * 50)
    return a2, a3
# In[11]
    # 將結果寫入csv
    '''
    df=pd.DataFrame({'date': a6, 'open': a10, 'high': a11, 'low': a12, 'close': a13, 'volume': a14, 'predict': a5})
    df.to_csv("ouo.csv", index=False)
    '''
#rf_main(loadFile('TXF1_日.csv'))