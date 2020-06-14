# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:25:49 2020

@author: user
"""

# ADABOOST
import pandas as pd
import numpy as np
import talib
from talib import abstract
from sklearn import model_selection, ensemble, preprocessing, metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from datetime import datetime
import pickle

# 載入資料
def loadFile(path='E:\ProjectAI\TXF1 1 日 10年.csv'):
    #    path='E:\ProjectAI\TXF1 1 日 10年.csv' 'TXF1_日.csv'TXF1 1 日 五年.csv'
    df = pd.read_csv(path, engine='python')
    data = df[['Open', 'High', 'Low', 'Close', 'TotalVolume']]

    dataDate = pd.to_datetime(df['Date'])
    dataDate.to_csv('index_date.csv', index=False, header=True)
    return data


# 資料處理
def ada_main(data):
    data = data.astype('float')
    data.rename(
        columns={"Open": "open", "High": "high", "Low": "low", "Close": "close", "TotalVolume": "volume"},
        inplace=True)

    # 加入指標
    data['MA3'] = talib.MA(data['close'], timeperiod=3)
    data['MA5'] = talib.MA(data['close'], timeperiod=5)
    data['MA10'] = talib.MA(data['close'], timeperiod=10)
    data['MA20'] = talib.MA(data['close'], timeperiod=20)
    data['RSI3'] = talib.RSI(data['close'], timeperiod=3)
    data['RSI5'] = talib.RSI(data['close'], timeperiod=5)  # RSI的天数一般是6、12、24
    data['RSI10'] = talib.RSI(data['close'], timeperiod=10)
    data['RSI20'] = talib.RSI(data['close'], timeperiod=20)
    data['MOM3'] = talib.MOM(data['close'], timeperiod=3)
    data['MOM5'] = talib.MOM(data['close'], timeperiod=5)
    data['MOM10'] = talib.MOM(data['close'], timeperiod=10)
    data['MOM20'] = talib.MOM(data['close'], timeperiod=20)
    data['MACD'], data['MACDSIGNAL'], data['MACDHIST'] = talib.MACD(data['close'], fastperiod=5, slowperiod=10,
                                                                    signalperiod=4)
    data["upperband"], data["middleband"], data["lowerband"] = talib.BBANDS(data['close'], timeperiod=5,
                                                                            nbdevup=2, nbdevdn=2, matype=0)
    data['k'], data['d'] = talib.STOCH(data['high'], data['low'], data['close'])
    data['WILLR5'] = talib.WILLR(data['high'], data['low'], data['close'], timeperiod=5)
    data['WILLR10'] = talib.WILLR(data['high'], data['low'], data['close'], timeperiod=10)
    data['OBV'] = talib.OBV(data['close'], data['volume'])

    a = pd.read_csv('index_date.csv')
    a = a.dropna()
    a['Datetime'] = pd.to_datetime(a['Date'])

    data = data.merge(a, left_index=True, right_index=True)
    data = data.set_index(['Datetime'])

    del data['Date']
    data.index.rename('date', inplace=True)

    # 判斷漲跌1 -1 0      #.shift是將資料數據往下移
    s = (data.close.shift(1) - data.close) / data.close
    # 漲跌幅 = 今日收盤價-昨日收盤價 / 今日收盤價
    data['s'] = s
    trend = []
    for i in range(len(data)):
        if (data['s'][i] > 0.005):
            trend.append(2)
            # data['day_trend'][i] = 1 漲
        elif (data['s'][i] < -0.002):
            trend.append(1)
            # data['day_trend'][i] = -1 跌
        else:
            trend.append(0)
            # data['day_trend'][i] = 0 不漲不跌
    data['day_trend'] = trend

    # 檢查資料有無缺值，刪除空值
    data.isnull().sum()
    data = data.dropna()

    # .iloc取固定行列值
    # train = data.iloc[::].copy()
    # test = data.iloc[:-5,:].copy()
    # 將資料分成訓練資料和測試資料
    # count = int(round(len(data) * 0.4))
    # train, test = data[:count], data[count:]
    X_data = data.drop(['s', 'day_trend'], axis=1)
    y_data = data.day_trend
    # X_test = test.drop(['s', 'day_trend'], axis=1)
    # y_test = test.day_trend

    # 將資料切割成訓練資料與驗證資料
    # X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2)

    # 讀取訓練好得模型
    # ada_ai = joblib.load('adaboost_train_model.pkl')
    with open('save/adaboost_train_model.pickle', 'rb') as f:
        ada_ai = pickle.load(f)
    # 測試讀取後的Model
    predicts = ada_ai.predict(X_data)
    accuracy = metrics.accuracy_score(y_data, predicts)
    print("acc:", accuracy)
    print("predicts:", predicts)

    # 匯出時間和開高收低以及預測結果
    c = len(data) - len(predicts)
    b = []
    for i in range(c):
        b.append(i)
        i += 1
    pdata = data.loc[:, ["open", "high", "low", "close", "volume"]]
    pdata = pdata.reset_index(drop=True)
    pdata.insert(0, 'date', a['Datetime'])
    pdata = pdata.drop(b)
    pdata.insert(6, 'predicts', predicts)
    pdata.to_csv('Outputcsv/2.csv', index=False, sep=',')


# ada_main(loadFile('C:/Users/Allen/Desktop/TXF1_JanToMay.csv'))
