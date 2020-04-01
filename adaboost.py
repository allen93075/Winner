#ADABOOST
import pandas as pd
import numpy as np
from sklearn import model_selection,ensemble, preprocessing, metrics
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from talib import abstract

#載入資料
df = pd.read_csv('E:\ProjectAI\TXF1-日-成交價_20years.csv')
data = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
data.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
data = data.set_index(['date'])

data = data.astype('float')
#計算技術指標
ta_list = ['RSI']
for x in ta_list:
    output = eval('abstract.'+x+'(data)')
    output.name = x.lower() if type(output) == pd.core.series.Series else None
    data = pd.merge(data, pd.DataFrame(output), left_on = data.index, right_on = output.index)
    data = data.set_index('key_0')
    data.index.name = 'date'

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

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X_train,y_train,test_size=0.2)
abc=AdaBoostClassifier(DecisionTreeClassifier(max_depth=2,min_samples_split=20, 
                                               min_samples_leaf=5),n_estimators=100)

abc.fit(X_train,y_train)
abc.score(X_test,y_test)
predicts = abc.predict(X_test)
accuracy = metrics.accuracy_score(y_test, predicts)
print("acc:", accuracy)
print("predicts:", predicts)
'''
#save to csv file
from numpy import savetxt
savetxt('mlppredict.csv', predicts, delimiter=',')
'''



