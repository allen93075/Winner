# -*- coding: utf-8 -*-
"""
Created on Sun May 10 09:50:42 2020

@author: yujie
"""
import pickle
import pandas as pd
import talib

def loadFile(path):
    df = pd.read_csv(path)
    data = df[['Open', 'High', 'Low', 'Close', 'TotalVolume']]

    dataDate = pd.to_datetime(df['Date'])
    dataDate.to_csv('index_pred.csv', index=False, header=True)
    return data
# In[]
def mainPred(data):
    data = data.astype('float')
    
    data.rename(columns={"Open": "open", "High": "high", "Low":"low", "Close":"close", "TotalVolume":"volume"} , inplace=True)
    data['MA5'] = talib.MA(data['close'], timeperiod=5)  
    data['MA10'] = talib.MA(data['close'], timeperiod=10)
    data['MA20'] = talib.MA(data['close'], timeperiod=20)
    data['RSI5'] = talib.RSI(data['close'], timeperiod=5)
    data['RSI10'] = talib.RSI(data['close'], timeperiod=10)  
    data['RSI20'] = talib.RSI(data['close'], timeperiod=20)
    data['MACD'],data['MACDSIGNAL'],data['MACDHIST'] = talib.MACD(data['close'], fastperiod=5, slowperiod=10, signalperiod=4)
    data['k'], data['d'] = talib.STOCH(data['high'], data['low'], data['close'])
    data['OBV']= talib.OBV(data['close'], data['volume'])
    
    a = pd.read_csv('index_pred.csv')
    a = a.dropna()
    a['Datetime'] = pd.to_datetime(a['Date'])
    
    data = data.merge(a, left_index=True, right_index=True)
    data = data.set_index(['Datetime'])
    
    del data['Date']
    data.index.rename('date', inplace=True)
    data.isnull().sum()
    data = data.dropna()
    #print(data)
# In[]    
    # 呼叫模型
    pickle_in = open('randomforest.pickle', 'rb')
    rf = pickle.load(pickle_in)
    
    # 使用模型
    predict_result = rf.predict(data)
    
    # 儲存至csv   
    df=pd.DataFrame({'date': data.index, 'open': data['open'], 'high': data['high'],
                     'low': data['low'], 'close': data['close'], 'volume': data['volume'],
                     'predict': predict_result})
    df.to_csv("Outputcsv/predOut.csv", index=False)   
    #print(predict_result)
    
# mainPred(loadFile("C:/Users/Allen/Desktop/TXF1_JanToMay.csv"))