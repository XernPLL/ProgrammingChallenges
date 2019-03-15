import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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
predict_days = int(math.ceil(0.04*len(data)))

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

iksy = np.array(original["Date"])
for _ in range(predict_days):
    before = iksy[-1]
    year, month, day = (int(x) for x in before.split('-'))
    answer = datetime.date(year, month, day).weekday()
    before = datetime.datetime.strptime(before, "%Y-%m-%d").timestamp()

    if answer == 4:
        now = before + 86400 * 4
    else:
        now = before + 86400 * 2

    now = datetime.datetime.utcfromtimestamp(now).strftime('%Y-%m-%d')
    iksy = np.append(iksy, np.array(now))


igreki= np.append(np.array(original["Adj Close"]), np.array(predict_done))


#plt.plot(iksy[:-predict_days],igreki[:-predict_days])
#plt.plot(iksy[-predict_days:],igreki[-predict_days:])
#plt.show()
print(iksy)
fig, ax = plt.subplots()
ax.plot_date(iksy[:-predict_days], igreki[:-predict_days],"-")
ax.plot_date(iksy[-predict_days:], igreki[-predict_days:],"-")

every_nth = 21
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
plt.xticks(rotation = "vertical")


# format the ticks
plt.show()


print(predict_done, confidence, predict_days)
