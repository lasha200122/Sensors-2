"""
ამ ფაილში წერია წრფივი რეგრესიის ლოგიკა. ცდომილება მინიმუმამდე რომ დამეყვანა
პითონის არსებული ბიბლიოთეკა გამოვიყენე რომელიც ფუნქციას გვიქმნის რისი მეშვეობითაც
ვპოულობთ განტოლებას
"""

from sklearn.linear_model import LinearRegression
import numpy as np

"""
რადგან მესამე განზომილებაში განვიხილავთ რეგრესიას ჩვენს x კოორინატს
ექნება ასეთი სახე [[x1, y1], [x2, y2]...] და y კი ასეთი [z1, z2, ...]
"""


def Predict(solutions):
    x = []
    y = []
    for solution in solutions:
        x.append(np.array([solution[0], solution[1]]))
        y.append(solution[2])
    x = np.array(x)
    y = np.array(y)

    model = LinearRegression().fit(x, y)

    y_pred = model.predict(x)
    error = abs(y_pred - y)
    count = 0
    for i in error:
        if i < 0.001:
            count += 1
    print("რაოდენობა:")
    print(count)
    print()
    return error


def Predict2d(solutions):
    x = []
    y = []
    for solution in solutions:
        x.append(solution[0])
        y.append(solution[1])
    x = np.array(x).reshape((-1, 1))
    y = np.array(y)

    model = LinearRegression().fit(x, y)

    y_pred = model.predict(x)



    error = abs(y_pred - y)
    count = 0
    for i in error:
        if i < 0.001:
            count += 1
    print("რაოდენობა:")
    print(count)
    print()
    return error, x, y_pred
