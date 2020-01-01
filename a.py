# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:36:11 2019

@author: USER
"""
import pickle
import numpy as np
import pandas as pd
from talib import abstract
#import csv

# 取出模型
filename = 'Decision_Tree_model_WF.sav'
model = pickle.load(open(filename, 'rb'))

df = pd.read_csv('C:/Users/USER/Desktop/TXF1-日-成交價_20years.csv')
data = df[['Open', 'High', 'Low', 'Close', 'TotalVolume']]
data.columns = ['open', 'high', 'low', 'close', 'totalvolume']
data = data.astype('float')


ta_list = ['MACD','RSI','MOM','STOCH']

for x in ta_list:
    output = eval('abstract.'+x+'(data)')
    output.name = x.lower() if type(output) == pd.core.series.Series else None
    data = pd.merge(data, pd.DataFrame(output), left_on = data.index, right_on = output.index)
    data = data.set_index('key_0')
#print(data)

#for n in data.index:
#    if(data.loc[n].isnull):
#        print(data.loc[n].index)


data.isnull().sum()
data = data.dropna()

#pd.DataFrame(model.predict(data)).to_csv("C:/Users/USER/Desktop/write_in_test.csv")
np.savetxt('C:/Users/USER/Desktop/write_in_test.csv', model.predict(data), delimiter=' ')
print(model.predict(data)[-1:])
