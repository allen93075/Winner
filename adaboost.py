#ADABOOST
import pandas as pd
import numpy as np
import talib
from talib import abstract
from sklearn import model_selection,ensemble, preprocessing, metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from datetime import datetime


#載入資料
def loadFile(path='E:\ProjectAI\TXF1 1 小時五年.csv'):
#    path='E:\ProjectAI\TXF1 1 日 10年.csv'
    df = pd.read_csv(path,engine='python')
    data = df[[' <Open>', ' <High>', ' <Low>', ' <Close>', ' <Volume>']]
        
    dataDate = pd.to_datetime(df['<Date>'])
    dataDate.to_csv('index_date.csv', index=False, header=True)
    return data

def ada_main(data):
    data = data.astype('float')
    data.rename(columns={" <Open>": "open", " <High>": "high", " <Low>":"low", " <Close>":"close", " <Volume>":"volume"} , inplace=True)
    
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
   
    a = pd.read_csv('index_copy.csv')
    a = a.dropna()
    a['Datetime'] = pd.to_datetime(a['<Date>'])

    data = data.merge(a, left_index=True, right_index=True)
    del data['<Date>']

    data = data.set_index(['Datetime'])
    data.index.rename('date', inplace=True)
    
    # 判斷漲跌1 -1 0
    s = (data.close - data.close.shift(1))/data.close.shift(1)  #漲跌幅 = 漲跌值 / 昨日收盤價
    data['s']=s
    trend=[]
    for i in range(len(data)):   
        if(data['s'][i] > 0.002):
            trend.append(2)
        #data['day_trend'][i] = 1,
        elif(data['s'][i]< -0.002):
            trend.append(1)
        #data['day_trend'][i] = -1
        else:
            trend.append(0)
        #data['day_trend'][i] = 0
    data['day_trend'] = trend

        # 檢查資料有無缺值，刪除空值
    
    data.isnull().sum()
    data = data.dropna()

    train = data.iloc[::].copy()
    test = data.iloc[:-5,:].copy()
    X_train = train.drop(['s', 'day_trend'], axis = 1)
    y_train = train.day_trend
    X_test = test.drop(['s', 'day_trend'], axis = 1)
    y_test = test.day_trend
            
    X_train,X_test,y_train,y_test=train_test_split(X_train,y_train,test_size=0.2,shuffle=False)
    ada_ai=AdaBoostClassifier(DecisionTreeClassifier(max_depth=2,min_samples_split=20, 
                                               min_samples_leaf=5),n_estimators=100)

    ada_ai.fit(X_train,y_train)
    ada_ai.score(X_test,y_test)
    predicts = ada_ai.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, predicts)
    print("acc:", accuracy)
    print("predicts:", predicts)

    
    c = len(data)-len(predicts)
    b = []
    for i in range(c):
        b.append(i)
        i+=1
    
    pdata = data.loc[:,["open","high","low","close","volume"]]
    pdata = pdata.reset_index(drop=True)
    pdata.insert(0,'date',a['Datetime'])
    pdata = pdata.drop(b)
    pdata.insert(6,'predicts',predicts)
    pdata.to_csv('adapredicts.csv', index=False, sep=',')





