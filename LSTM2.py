import numpy as np
import pandas as pd
from sklearn import metrics, preprocessing
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Bidirectional
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt
from tensorflow_core.python import keras


def mark(predictprice, lastprice):
    mark = (predictprice - lastprice) / lastprice
    trend = []
    if mark > 0.0025:
        trend.append(2)
    elif mark < -0.0025:
        trend.append(1)
    else:
        trend.append(0)

    return trend


def create_dataset(ds, look_back=1):
    X_data, Y_data = [], []
    for i in range(len(ds) - look_back):
        X_data.append(ds[i:(i + look_back), 0])
        Y_data.append(ds[i + look_back, 0])

    return np.array(X_data), np.array(Y_data)


def normalize(df):
    newdf = df.copy()
    min_max_scaler = preprocessing.MinMaxScaler()
    for field in df.columns:
        newdf['Open'] = min_max_scaler.fit_transform(df.Open.values.reshape(-1, 1))
        newdf['Low'] = min_max_scaler.fit_transform(df.Low.values.reshape(-1, 1))
        newdf['High'] = min_max_scaler.fit_transform(df.High.values.reshape(-1, 1))
        newdf['TotalVolume'] = min_max_scaler.fit_transform(df.TotalVolume.values.reshape(-1, 1))
        newdf['Close'] = min_max_scaler.fit_transform(df.Close.values.reshape(-1, 1))
    return newdf


def data_helper(df_train, df_trade, time_frame):
    # 資料維度: 開盤價、收盤價、最高價、最低價、成交量, 5維

    # 將dataframe 轉成 numpy array
    datavalue_train = df_train.values
    result = []
    for index in range(len(datavalue_train) - (time_frame + 1)):  # 從 datavalue 的第0個跑到倒數第 time_frame+1 個
        result.append(
            datavalue_train[index: index + (time_frame + 1)])  # 逐筆取出 time_frame+1 個K棒數值做為一筆 instancetime_frame

    result = np.array(result)
    # number_train = round(1 * result.shape[0])  # 取 result 的前100% instance做為訓練資料

    x_train = result[:, :-1, :]  # 訓練資料中, 只取每一個 time_frame 中除了最後一筆的所有資料做為feature
    y_train = result[:, -1, 0]  # 訓練資料中, 取每一個 time_frame 中最後一筆資料的最後一個數值(收盤價)做為答案
    # 測試資料
    tmp = np.concatenate((df_train[-time_frame:].values, df_trade[:-1].values))
    x_test = []
    y_test = []
    for index in range(len(tmp) - (time_frame + 1)):  # 從 datavalue 的第0個跑到倒數第 time_frame+1 個
        x_test.append(tmp[index: index + time_frame])
        y_test.append(tmp[index + time_frame][0])
    # 將資料組成變好看一點
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 5)) # OAO
    x_test = np.array(x_test)
    y_test = np.array(y_test)
    return [x_train, y_train, x_test, y_test]


def denormalize(df, col_name, norm_value):
    original_value = df[col_name].values.reshape(-1, 1)
    norm_value = norm_value.reshape(-1, 1)
    min_max_scaler = preprocessing.MinMaxScaler()
    min_max_scaler.fit_transform(original_value)
    denorm_value = min_max_scaler.inverse_transform(norm_value)
    return denorm_value


def look_back_day(look_back_day=30):
    return look_back_day


def train_data(path="traindata.csv"):
    df_train = pd.read_csv(path, index_col="Date", parse_dates=True)
    return df_train


def test_data(path="test_data.csv"):
    df_test = pd.read_csv(path, index_col="Date", parse_dates=True)
    return df_test


# 定義模型
def build_model(Dropoutrate, look_back, df_train, df_test):
    # look_back = look_back_day(lookback)
    sc = MinMaxScaler()
    # df_train = train_data()
    # df_test = test_data()
    df_train_nor = normalize(df_train)
    df_test_nor = normalize(df_test)
    X_train, Y_train, X_test, Y_test = data_helper(df_train_nor, df_test_nor, look_back)

    # X_train_set = df_train.iloc[:, 3:4].values
    number_features = len(df_train.columns)
    # 特徵標準化 - 正規化
    result = []

    # print(X_train)
    # 轉換成(樣本數, 時步, 特徵)張量
    # print("X_train.shape: ", X_train.shape)
    # print("Y_train.shape: ", Y_train.shape)
    # X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    # print("X_train.shape: ", X_train.shape)
    # print("Y_train.shape: ", Y_train.shape)
    model = Sequential()
    model.add(Bidirectional(LSTM(X_train.shape[1], return_sequences=False), input_shape=(X_train.shape[1:])))
    model.add(Dense(X_train.shape[1]))
    model.add(Dropout(Dropoutrate))
    model.add(Dense(1, activation="tanh"))
    optimizer = RMSprop(lr=0.001)
    model.compile(loss='mean_squared_error', optimizer=optimizer)
    model.compile(loss="mse", optimizer="adam")
    ES = EarlyStopping(monitor='loss', patience=2, verbose=0)
    # 訓練模型
    model.fit(X_train, Y_train, batch_size=32, epochs=100, validation_split=0.1, verbose=1)
    model.save("LSTM_model")
    predict_index = df_test.index.values
    X_test_pred = model.predict(X_test)
    # 將預測值轉換回價格
    X_test_pred_price = denormalize(df_test, "Close", X_test_pred)
    answer = denormalize(df_test, "Close", Y_test)
    # 繪圖
    plt.plot(answer, color="red", label="Real Price")
    plt.plot(X_test_pred_price, color="blue", label="Predicted")
    plt.title(" Price Prediction")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

    task = len(X_test_pred_price) - 1
    predic_price_mark = []
    true_price_mark = []
    for i in range(task):
        predic_price_mark.append(mark(X_test_pred_price[i + 1], X_test_pred_price[i]))
        true_price_mark.append(mark(answer[i + 1], answer[i]))

    accuracy = metrics.accuracy_score(true_price_mark, predic_price_mark)
    print("正確率:", accuracy)
    output = mark(X_test_pred_price[-1], X_test_pred_price[-2])
    print(predict_index)
    print(len(predict_index))
    print("預測結果", predic_price_mark)
    print("預測筆數", len(predic_price_mark))
    output2 = np.squeeze(np.asarray(predic_price_mark))
    predict_index = predict_index[3:]
    a = df_test["Open"].values
    a = a[3:]
    b = df_test["High"].values
    b = b[3:]
    c = df_test["Low"].values
    c = c[3:]
    d = df_test["Close"].values
    d = d[3:]
    e = df_test['TotalVolume'].values
    e = e[3:]

    print("比數", len(a))
    print("測試:", a)
    dataframe = pd.DataFrame({'date': predict_index,
                              'open': a,
                              'high': b,
                              'low': c,
                              'close': d,
                              'volume': e,
                              'predict': output2})
    dataframe.to_csv('1.csv', index=False, sep=',')


def predict(model, time_frame, df_test, df_train=train_data()):
    df_train_nor = normalize(df_train)
    df_test_nor = normalize(df_test)
    X_train, Y_train, X_test, Y_test = data_helper(df_train_nor, df_test_nor, time_frame)

    X_test_pred = model.predict(X_test)
    X_test_pred_price = denormalize(df_test, "Close", X_test_pred)
    answer = denormalize(df_test, "Close", Y_test)
    predict_index = df_test.index.values
    task = len(X_test_pred_price) - 1
    predic_price_mark = []
    true_price_mark = []
    for i in range(task):
        predic_price_mark.append(mark(X_test_pred_price[i + 1], X_test_pred_price[i]))
        true_price_mark.append(mark(answer[i + 1], answer[i]))

    accuracy = metrics.accuracy_score(true_price_mark, predic_price_mark)
    print("正確率:", accuracy)
    output = mark(X_test_pred_price[-1], X_test_pred_price[-2])
    # print(predict_index)
    # print(len(predict_index))
    # print("預測結果", predic_price_mark)
    # print("預測筆數", len(predic_price_mark))
    output2 = np.squeeze(np.asarray(predic_price_mark))
    predict_index = predict_index[2:-1]
    #寫入CSV
    a = df_test["Open"].values
    a = a[3:]
    b = df_test["High"].values
    b = b[3:]
    c = df_test["Low"].values
    c = c[3:]
    d = df_test["Close"].values
    d = d[3:]
    e = df_test['TotalVolume'].values
    e = e[3:]

    # print("比數", len(a))
    # print("測試:", a)
    dataframe = pd.DataFrame({'date': predict_index,
                              'open': a,
                              'high': b,
                              'low': c,
                              'close': d,
                              'volume': e,
                              'predict': output2})
    dataframe.to_csv('Outputcsv/2.csv', index=False, sep=',')


# model = keras.models.load_model('LSTM_model')
# predict(model,60,test_data())
# build_model(0.2, 60, train_data("C:/Users/Allen/Desktop/traindata.csv"), test_data())

# model = build_model()
# model = Sequential()
# model.add(Bidirectional(LSTM(X_train.shape[1], return_sequences=False), input_shape=(X_train.shape[1:])))
# model.add(Dense(X_train.shape[1]))
# model.add(Dropout(0.20))
# model.add(Dense(1, activation='tanh'))
# optimizer = RMSprop(lr=0.001)
# model.compile(loss='mean_squared_error', optimizer=optimizer)
# 編譯模型
