# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 03:07:48 2020

@author: user
"""
import pandas as pd
import numpy as np
from sklearn import model_selection,ensemble, preprocessing, metrics
from sklearn.neural_network import MLPClassifier
from talib import abstract
from sklearn.preprocessing import StandardScaler

#載入資料
df = pd.read_csv('E:\ProjectAI\TXF1-日-成交價_20years.csv')
data = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
data.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
data = data.set_index(['date'])

'''
data = data.astype('float')
#計算技術指標
ta_list = ['RSI']
for x in ta_list:
    output = eval('abstract.'+x+'(data)')
    output.name = x.lower() if type(output) == pd.core.series.Series else None
    data = pd.merge(data, pd.DataFrame(output), left_on = data.index, right_on = output.index)
    data = data.set_index('key_0')
    data.index.name = 'date'
'''
# 判斷漲跌1 -1 0
s = (data.close - data.close.shift(1))/data.close.shift(1)  #漲跌幅 = 漲跌值 / 昨日收盤價
data['s']=s
trend=[]
for i in range(len(data)):   
    if(data['s'][i] > 0.0025):
        trend.append(1)
        #data['day_trend'][i] = 1,
    elif(data['s'][i]< -0.0025):
        trend.append(-1)
        #data['day_trend'][i] = -1
    else:
        trend.append(0)
        #data['day_trend'][i] = 0
data['day_trend'] = trend

#data['day_trend'] = np.where(data.close-data.close.shift(-1) > data.close*0.0015, 1, 0)
# 檢查資料有無缺值，刪除空值
print(data['day_trend'])
data.isnull().sum()
data = data.dropna()

#split_point = int(len(data)*0.9)
train = data.iloc[::].copy()
test = data.iloc[:-5,:].copy()
X_train = train.drop(['s', 'day_trend'], axis = 1)
y_train = train.day_trend
X_test = test.drop(['s', 'day_trend'], axis = 1)
y_test = test.day_trend

#正規化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X_train,y_train,test_size=0.33)
clf = MLPClassifier(hidden_layer_sizes=(1,100), max_iter=500, alpha=1e-4,
                    solver='lbfgs', verbose=2, tol=1e-4, random_state=32,
                    learning_rate_init=0.5)
clf.fit(X_train,y_train)


#mlp=MLPClassifier(solver='lbfgs',#solver:'lbfgs','sgd','adam',
#                    hidden_layer_sizes=(2,20),random_state=42,
#                    learning_rate_init=0.001,max_iter=100)
#mlp.fit(X_train,y_train)\n",

predicts = clf.predict(X_test)
#print('acc：%s' % clf.score(X_test, y_test))
accuracy = metrics.accuracy_score(y_test, predicts)
print("acc:", accuracy)
print("predicts:", predicts)

#save to csv file
from numpy import savetxt
savetxt('mlppredict.csv', predicts, delimiter=',')

