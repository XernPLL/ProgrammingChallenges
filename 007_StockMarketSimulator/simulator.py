import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import math
import datetime

data = pd.read_csv("NFLX.csv")
original = data
data["DayChange"] = ((data["Adj Close"] - data["Open"])/data["Open"])*100.0
data["HighLowChange"] = ((data["High"] - data["Low"])/data["Adj Close"])*100.0
data = data[["Adj Close", "HighLowChange", "DayChange", "Volume"]]
#plt.plot(data["Date"], data["Open"])
#plt.show()
predict_col = "Adj Close"
predict_days = int(math.ceil(0.01*len(data)))

data["label"] = data[predict_col].shift(-predict_days)
X = np.array(data.drop(["label"], 1))
X = preprocessing.scale(X)
X_actually = X[-predict_days:]
X = X[:-predict_days]

data.dropna(inplace=True)

y = np.array(data["label"])

[X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.1)

classifier = LinearRegression(n_jobs=1)
classifier.fit(X_train,y_train)
confidence = classifier.score(X_test, y_test)

predict_done = classifier.predict(X_actually)



style.use("ggplot")

data["Predykcja"] = np.nan
czas= np.array(original["Date"])
spec = czas[-1].split("-")
last = datetime.datetime(int(spec[0]), int(spec[1]), int(spec[2])).timestamp()
if datetime.datetime(int(spec[0]), int(spec[1]), int(spec[2])).weekday() == 4:
    next = last + 86400*3
else:
    next = last + 86400
for i in predict_done:
    next_date = datetime.datetime.fromtimestamp(next)
    if next_date.timetuple().tm_wday == 4:
        next = last + 86400 * 3
    else:
        next += 86400
    data.loc[next_date] = [np.nan for _ in range(len(data.columns)-1)]+[i]
plt.plot(original["Date"], data["Adj Close"])
data['Predykcja'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

print(predict_done, confidence, predict_days)
