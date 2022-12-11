"""
ეს ფაილი განკუთვნილია გრაფიკების დასახაზად
"""
import random

import matplotlib.pyplot as plt
import numpy as np


def PlotSolutions(solutions, title):  # წრფის მეშვეობით დახაზვა
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    x = [i[0] for i in solutions]
    y = [i[1] for i in solutions]
    z = [i[2] for i in solutions]
    ax.plot(x, y, z, color='blue')
    ax.set_title(title)
    return plt.show()


def ScatterSolutions(solutions, title):  # წერტილების დასმა
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    x = [i[0] for i in solutions]
    y = [i[1] for i in solutions]
    z = [i[2] for i in solutions]
    x1 = []
    y1 = []
    z1 = []
    for i, v in enumerate(y):
        if v < 40000:
            y1.append(v)
            x1.append(x[i])
            z1.append(z[i])
    ax.scatter(x1, y1, z1, color='blue')
    ax.set_title(title)
    return plt.show()


def ScatterSolutions2d(solutions, title, X, Y):  # წერტილების დასმა
    x = [i[0] for i in solutions]
    y = [i[1] for i in solutions]
    y1 = []
    x1 = []
    y2 = []
    x2 = []
    for index, value in enumerate(y):
        if value < 4000:
            y1.append(value)
            x1.append(x[index])

    for index, value in enumerate(Y):
        if value < 4000:
            y2.append(value)
            x2.append(x[index])
    plt.scatter(x1, y1, color='blue')
    plt.plot(x1,y1, color="red")
    plt.title(title)
    return plt.show()


def PlotSolutions2d(solutions, title):  # წერტილების დასმა
    fig = plt.figure()
    ax = fig.add_subplot(projection='2d')
    x = [i[0] for i in solutions]
    y = [i[1] for i in solutions]
    ax.plot(x, y, color='blue')
    ax.set_title(title)
    return plt.show()


def ErrorGraph(vector, title):  # ცდომილების გრაფიკი
    plt.title(title)
    vector = np.array(vector)[vector <2000]
    vector = vector[vector > 0]
    plt.plot([i for i in range(len(vector))], vector, color='red')
    plt.scatter([i for i in range(len(vector))], vector, color='blue')
    return plt.show()


def ScatterClusters3D(dictionary, title):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for key in dictionary.keys():
        distances = [Distance(key[0] - i[0], key[1] - i[1], key[2] - i[2]) for i in dictionary[key]]
        radius = max(distances, default=0)
        print("Centroid: " + str(key) + " | Number of clusters: " + str(len(dictionary[key])) + " | Radius: "
              + str(radius))
        x = [i[0] for i in dictionary[key]]
        y = [i[1] for i in dictionary[key]]
        z = [i[2] for i in dictionary[key]]
        color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        ax.scatter(x, y, z, color=color)
        ax.scatter([key[0]], [key[1]], [key[2]], marker='+', color=color)

    ax.set_title(title)
    return plt.show()


def Distance(x, y, z):
    return np.sqrt(x * x + y * y + z * z)


def Distance2(x, y):
    return np.sqrt(x * x + y * y)


def ScatterClusters2D(dictionary, title):
    plt.title(title)
    for key in dictionary.keys():
        distances = [Distance2(key[0] - i[0], key[1] - i[1]) for i in dictionary[key]]
        radius = max(distances, default=0)
        print("Centroid: " + str(key) + " | Number of clusters: " + str(len(dictionary[key])) + " | Radius: "
              + str(radius))
        x = [i[0] for i in dictionary[key]]
        y = [i[1] for i in dictionary[key]]
        color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        plt.scatter(x, y, color=color)
        plt.scatter([key[0]], [key[1]], marker='+', color=color)
        circle = plt.Circle((key[0], key[1]), radius, color=color, fill=False)
        plt.gca().add_patch(circle)

    return plt.show()


def DrawErrors(data):
    CO = [(i[1].CO - i[0].CO, i[1].CO) for i in data]
    NO = [(i[1].NO - i[0].NO, i[1].NO) for i in data]
    NO2 = [(i[1].NO2 - i[0].NO2, i[1].NO2) for i in data]
    O3 = [(i[1].O3 - i[0].O3, i[1].O3) for i in data]
    O3NO2 = [(i[1].O3NO2 - i[0].O3NO2, i[1].O3NO2) for i in data]
    CO_X = np.array([i[0] for i in CO])
    CO_X = CO_X[CO_X < 2]
    CO_X = CO_X[CO_X >= 0]
    # plt.title("CO errors, nea sensor - low cost sensor, chronological order")
    # plt.plot([i for i in range(len(CO_X))], CO_X)
    # plt.show()

    # plt.title("NO errors nea sensor - low cost sensor, chronological order")
    # plt.plot([i for i in range(len(NO))], [i[0] for i in NO])
    # plt.show()
    #
    # plt.title("NO2")
    # plt.plot([i for i in range(len(NO2))], [i[0] for i in NO2])
    # plt.show()
    #
    # plt.title("O3")
    # plt.plot([i for i in range(len(O3))], [i[0] for i in O3])
    # plt.show()
    #
    # plt.title("O3NO2")
    # plt.plot([i for i in range(len(O3NO2))], [i[0] for i in O3NO2])
    # plt.show()


    # #----
    # plt.title("CO Measurements Zoomed")
    # plt.plot([i for i in range(len(data))], [i[0].CO for i in data], label="one minute average low cost sensor")
    # plt.plot([i for i in range(len(data))], [i[1].CO for i in data], label="NEA")
    # plt.legend()
    # plt.show()

    # n = np.array( [i[0].NO for i in data])
    # n = n[n > 0.2]
    # plt.title("NO Measurements")
    # plt.plot([i for i in range(len(n))], n, label="one minute average low cost sensor")
    # plt.plot([i for i in range(len(data))], [i[1].NO for i in data], label="NEA")
    # plt.legend()
    # plt.show()
    #
    # plt.title("NO Measurements Zoomed")
    # plt.plot([i for i in range(len(n))], n, label="one minute average low cost sensor")
    # plt.plot([i for i in range(len(data))], [i[1].NO for i in data], label="NEA")
    # plt.legend()
    # plt.show()

    # plt.title("NO2")
    # plt.plot([i for i in range(len(data))], [i[0].NO2 for i in data], label="Mean")
    # plt.plot([i for i in range(len(data))], [i[1].NO2 for i in data], label="NEA")
    # plt.legend()
    # plt.show()
    #
    #
    # plt.title("O3")
    # plt.plot([i for i in range(len(data))], [i[0].O3 for i in data], label="Mean")
    # plt.plot([i for i in range(len(data))], [i[1].O3 for i in data], label="NEA")
    # plt.legend()
    # plt.show()
    #
    # plt.title("O3NO2")
    # plt.plot([i for i in range(len(data))], [i[0].O3NO2 for i in data], label="Mean")
    # plt.plot([i for i in range(len(data))], [i[1].O3NO2 for i in data], label="NEA")
    # plt.legend()
    # plt.show()

    co_5_10 = [i for i in CO if fivePer((i[1])) <= abs(i[0]) < tenPer(i[1])]
    co_10_20 = [i for i in CO if tenPer((i[1])) <= abs(i[0]) < twentyPer(i[1])]
    co_20_50 = [i for i in CO if twentyPer((i[1])) <= abs(i[0]) < fivetyPer(i[1])]
    co_50_75 = [i for i in CO if fivetyPer((i[1])) <= abs(i[0]) < SeventyfivePer(i[1])]
    co_75 = [i for i in CO if abs(i[0]) >= SeventyfivePer(i[1])]


    no_5_10 = [i for i in NO if fivePer((i[1])) <= abs(i[0]) < tenPer(i[1])]
    no_10_20 = [i for i in NO if tenPer((i[1])) <= abs(i[0]) < twentyPer(i[1])]
    no_20_50 = [i for i in NO if twentyPer((i[1])) <= abs(i[0]) < fivetyPer(i[1])]
    no_50_75 = [i for i in NO if fivetyPer((i[1])) <= abs(i[0]) < SeventyfivePer(i[1])]
    no_75 = [i for i in NO if abs(i[0]) >= SeventyfivePer(i[1])]

    no2_5_10 = [i for i in NO2 if fivePer((i[1])) <= abs(i[0]) < tenPer(i[1])]
    no2_10_20 = [i for i in NO2 if tenPer((i[1])) <= abs(i[0]) < twentyPer(i[1])]
    no2_20_50 = [i for i in NO2 if twentyPer((i[1])) <= abs(i[0]) < fivetyPer(i[1])]
    no2_50_75 = [i for i in NO2 if fivetyPer((i[1])) <= abs(i[0]) < SeventyfivePer(i[1])]
    no2_75 = [i for i in NO2 if abs(i[0]) >= SeventyfivePer(i[1])]

    o3_5_10 = [i for i in O3 if fivePer((i[1])) <= abs(i[0]) < tenPer(i[1])]
    o3_10_20 = [i for i in O3 if tenPer((i[1])) <= abs(i[0]) < twentyPer(i[1])]
    o3_20_50 = [i for i in O3 if twentyPer((i[1])) <= abs(i[0]) < fivetyPer(i[1])]
    o3_50_75 = [i for i in O3 if fivetyPer((i[1])) <= abs(i[0]) < SeventyfivePer(i[1])]
    o3_75 = [i for i in O3 if abs(i[0]) >= SeventyfivePer(i[1])]

    o3no2_5_10 = [i for i in O3NO2 if fivePer((i[1])) <= abs(i[0]) < tenPer(i[1])]
    o3no2_10_20 = [i for i in O3NO2 if tenPer((i[1])) <= abs(i[0]) < twentyPer(i[1])]
    o3no2_20_50 = [i for i in O3NO2 if twentyPer((i[1])) <= abs(i[0]) < fivetyPer(i[1])]
    o3no2_50_75 = [i for i in O3NO2 if fivetyPer((i[1])) <= abs(i[0]) < SeventyfivePer(i[1])]
    o3no2_75 = [i for i in O3NO2 if abs(i[0]) >= SeventyfivePer(i[1])]

    # #  CO drawing
    # plt.title("CO Measurements")
    # plt.plot([i for i in range(len(co_5_10))], [i[0] for i in co_5_10], label="5%-10% count: " + str(len(co_5_10)))
    # plt.plot([i for i in range(len(co_5_10), len(co_5_10) + len(co_10_20))], [i[0] for i in co_10_20], label="10%-20% count: " + str(len(co_10_20)))
    # plt.plot([i for i in range(len(co_5_10) + len(co_10_20), len(co_5_10) + len(co_10_20) + len(co_20_50))], [i[0] for i in co_20_50], label="20%-50% count: " + str(len(co_20_50)))
    # plt.plot([i for i in range(len(co_5_10) + len(co_10_20) + len(co_20_50) , len(co_5_10) + len(co_10_20) + len(co_20_50) + len(co_50_75) )], [i[0] for i in co_50_75], label="50%-75% count: " + str(len(co_50_75)))
    # plt.plot([i for i in range(len(co_5_10) + len(co_10_20) + len(co_20_50) + len(co_50_75) , len(co_5_10) + len(co_10_20) + len(co_20_50) + len(co_50_75) + len(co_75))], [i[0] for i in co_75], label="75% count: " + str(len(co_75)))
    # plt.legend()
    # plt.show()
    #
    #
    #
    # plt.title("NO Measurements")
    # plt.plot([i for i in range(len(no_5_10))], [i[0] for i in no_5_10], label="5%-10% count: " + str(len(no_5_10)))
    # plt.plot([i for i in range(len(no_5_10), len(no_5_10) + len(no_10_20))], [i[0] for i in no_10_20], label="10%-20% count: " + str(len(no_10_20)))
    # plt.plot([i for i in range(len(no_5_10) + len(no_10_20), len(no_5_10) + len(no_10_20) + len(no_20_50))], [i[0] for i in no_20_50], label="20%-50% count: " + str(len(no_20_50)))
    # plt.plot([i for i in range(len(no_5_10) + len(no_10_20) + len(no_20_50), len(no_5_10) + len(no_10_20) + len(no_20_50) + len(no_50_75))], [i[0] for i in no_50_75], label="50%-75% count: " + str(len(no_50_75)))
    # plt.plot([i for i in range(len(no_5_10) + len(no_10_20) + len(no_20_50) + len(no_50_75), len(no_5_10) + len(no_10_20) + len(no_20_50) + len(no_50_75) + len(no_75))], [i[0] for i in no_75], label="75% count: " + str(len(no_75)))
    # plt.legend()
    # plt.show()
    #
    # plt.title("NO2")
    # plt.plot([i for i in range(len(no2_5_10))], [i[0] for i in no2_5_10], label="5%-10% count: " + str(len(no2_5_10)))
    # plt.plot([i for i in range(len(no2_5_10), len(no2_5_10) + len(no2_10_20))], [i[0] for i in no2_10_20], label="10%-20% count: " + str(len(no2_10_20)))
    # plt.plot([i for i in range(len(no2_5_10) + len(no2_10_20), len(no2_5_10) + len(no2_10_20) + len(no2_20_50))], [i[0] for i in no2_20_50], label="20%-50% count: " + str(len(no2_20_50)))
    # plt.plot([i for i in range(len(no2_5_10) + len(no2_10_20) + len(no2_20_50), len(no2_5_10) + len(no2_10_20) + len(no2_20_50) + len(no2_50_75))], [i[0] for i in no2_50_75], label="50%-75% count: " + str(len(no2_50_75)))
    # plt.plot([i for i in range(len(no2_5_10) + len(no2_10_20) + len(no2_20_50) + len(no2_50_75), len(no2_5_10) + len(no2_10_20) + len(no2_20_50) + len(no2_50_75) + len(no2_75))], [i[0] for i in no2_75], label="75% count: " + str(len(no2_75)))
    # plt.legend()
    # plt.show()
    #
    #
    # plt.title("O3")
    # plt.plot([i for i in range(len(o3_5_10))], [i[0] for i in o3_5_10], label="5%-10% count: " + str(len(o3_5_10)))
    # plt.plot([i for i in range(len(o3_5_10), len(o3_5_10) + len(o3_10_20))], [i[0] for i in o3_10_20],
    #          label="10%-20% count: " + str(len(o3_10_20)))
    # plt.plot([i for i in range(len(o3_5_10) + len(o3_10_20), len(o3_5_10) + len(o3_10_20) + len(o3_20_50))],
    #          [i[0] for i in o3_20_50], label="20%-50% count: " + str(len(o3_20_50)))
    # plt.plot([i for i in range(len(o3_5_10) + len(o3_10_20) + len(o3_20_50),
    #                            len(o3_5_10) + len(o3_10_20) + len(o3_20_50) + len(o3_50_75))], [i[0] for i in o3_50_75],
    #          label="50%-75% count: " + str(len(o3_50_75)))
    # plt.plot([i for i in range(len(o3_5_10) + len(o3_10_20) + len(o3_20_50) + len(o3_50_75),
    #                            len(o3_5_10) + len(o3_10_20) + len(o3_20_50) + len(o3_50_75) + len(o3_75))],
    #          [i[0] for i in o3_75], label="75% count: " + str(len(o3_75)))
    # plt.legend()
    # plt.show()
    #
    # plt.title("O3NO2")
    # plt.plot([i for i in range(len(o3no2_5_10))], [i[0] for i in o3no2_5_10], label="5%-10% count: " + str(len(o3no2_5_10)))
    # plt.plot([i for i in range(len(o3no2_5_10), len(o3no2_5_10) + len(o3no2_10_20))], [i[0] for i in o3no2_10_20],
    #          label="10%-20% count: " + str(len(o3no2_10_20)))
    # plt.plot([i for i in range(len(o3no2_5_10) + len(o3no2_10_20), len(o3no2_5_10) + len(o3no2_10_20) + len(o3no2_20_50))],
    #          [i[0] for i in o3no2_20_50], label="20%-50% count: " + str(len(o3no2_20_50)))
    # plt.plot([i for i in range(len(o3no2_5_10) + len(o3no2_10_20) + len(o3no2_20_50),
    #                            len(o3no2_5_10) + len(o3no2_10_20) + len(o3no2_20_50) + len(o3no2_50_75))], [i[0] for i in o3no2_50_75],
    #          label="50%-75% count: " + str(len(o3no2_50_75)))
    # plt.plot([i for i in range(len(o3no2_5_10) + len(o3no2_10_20) + len(o3no2_20_50) + len(o3no2_50_75),
    #                            len(o3no2_5_10) + len(o3no2_10_20) + len(o3no2_20_50) + len(o3no2_50_75) + len(o3no2_75))],
    #          [i[0] for i in o3no2_75], label="75% count: " + str(len(o3no2_75)))
    # plt.legend()
    # plt.show()
    # CO_X = CO_X[CO_X > 0.15]
    # plt.title("CO sensor data, 1 minute average")
    # plt.plot([i for i in range(len(CO_X))], CO_X)
    # plt.xlabel("Minutes")
    # plt.ylabel("Measurements")
    # plt.show()
    n = np.array([i[0].NO for i in data])
    n = n[n > 0.2]

    plt.title("NO sensor data, 1 minute average")
    plt.plot([i for i in range(len(n))], n)
    plt.show()

    # plt.title("NO2 Chronological order")
    # plt.plot([i for i in range(len(data))], [i[0].NO2 for i in data])
    # plt.show()
    #
    # plt.title("O3 Chronological order")
    # plt.plot([i for i in range(len(data))], [i[0].O3 for i in data])
    # plt.show()
    #
    # plt.title("O3NO2 Chronological order")
    # plt.plot([i for i in range(len(data))], [i[0].O3NO2 for i in data])
    # plt.show()
    #
    # plt.title("CO")
    # plt.scatter([i for i in range(len(co_5_10))], [i[0] for i in co_5_10], label="5%-10% count: " + str(len(co_5_10)))
    # plt.scatter([i for i in range(len(co_5_10), len(co_5_10) + len(co_10_20))], [i[0] for i in co_10_20],
    #          label="10%-20% count: " + str(len(co_10_20)))
    # plt.scatter([i for i in range(len(co_5_10) + len(co_10_20), len(co_5_10) + len(co_10_20) + len(co_20_50))],
    #          [i[0] for i in co_20_50], label="20%-50% count: " + str(len(co_20_50)))
    # plt.scatter([i for i in range(len(co_5_10) + len(co_10_20) + len(co_20_50),
    #                            len(co_5_10) + len(co_10_20) + len(co_20_50) + len(co_50_75))], [i[0] for i in co_50_75],
    #          label="50%-75% count: " + str(len(co_50_75)))
    # plt.scatter([i for i in range(len(co_5_10) + len(co_10_20) + len(co_20_50) + len(co_50_75),
    #                            len(co_5_10) + len(co_10_20) + len(co_20_50) + len(co_50_75) + len(co_75))],
    #          [i[0] for i in co_75], label="75% count: " + str(len(co_75)))
    # plt.legend()
    # plt.show()
    #
    # plt.title("NO")
    # plt.scatter([i for i in range(len(no_5_10))], [i[0] for i in no_5_10], label="5%-10% count: " + str(len(no_5_10)))
    # plt.scatter([i for i in range(len(no_5_10), len(no_5_10) + len(no_10_20))], [i[0] for i in no_10_20],
    #          label="10%-20% count: " + str(len(no_10_20)))
    # plt.scatter([i for i in range(len(no_5_10) + len(no_10_20), len(no_5_10) + len(no_10_20) + len(no_20_50))],
    #          [i[0] for i in no_20_50], label="20%-50% count: " + str(len(no_20_50)))
    # plt.scatter([i for i in range(len(no_5_10) + len(no_10_20) + len(no_20_50),
    #                            len(no_5_10) + len(no_10_20) + len(no_20_50) + len(no_50_75))], [i[0] for i in no_50_75],
    #          label="50%-75% count: " + str(len(no_50_75)))
    # plt.scatter([i for i in range(len(no_5_10) + len(no_10_20) + len(no_20_50) + len(no_50_75),
    #                            len(no_5_10) + len(no_10_20) + len(no_20_50) + len(no_50_75) + len(no_75))],
    #          [i[0] for i in no_75], label="75% count: " + str(len(no_75)))
    # plt.legend()
    # plt.show()
    #
    # plt.title("NO2")
    # plt.scatter([i for i in range(len(no2_5_10))], [i[0] for i in no2_5_10], label="5%-10% count: " + str(len(no2_5_10)))
    # plt.scatter([i for i in range(len(no2_5_10), len(no2_5_10) + len(no2_10_20))], [i[0] for i in no2_10_20],
    #          label="10%-20% count: " + str(len(no2_10_20)))
    # plt.scatter([i for i in range(len(no2_5_10) + len(no2_10_20), len(no2_5_10) + len(no2_10_20) + len(no2_20_50))],
    #          [i[0] for i in no2_20_50], label="20%-50% count: " + str(len(no2_20_50)))
    # plt.scatter([i for i in range(len(no2_5_10) + len(no2_10_20) + len(no2_20_50),
    #                            len(no2_5_10) + len(no2_10_20) + len(no2_20_50) + len(no2_50_75))],
    #          [i[0] for i in no2_50_75], label="50%-75% count: " + str(len(no2_50_75)))
    # plt.scatter([i for i in range(len(no2_5_10) + len(no2_10_20) + len(no2_20_50) + len(no2_50_75),
    #                            len(no2_5_10) + len(no2_10_20) + len(no2_20_50) + len(no2_50_75) + len(no2_75))],
    #          [i[0] for i in no2_75], label="75% count: " + str(len(no2_75)))
    # plt.legend()
    # plt.show()
    #
    # plt.title("O3")
    # plt.scatter([i for i in range(len(o3_5_10))], [i[0] for i in o3_5_10], label="5%-10% count: " + str(len(o3_5_10)))
    # plt.scatter([i for i in range(len(o3_5_10), len(o3_5_10) + len(o3_10_20))], [i[0] for i in o3_10_20],
    #          label="10%-20% count: " + str(len(o3_10_20)))
    # plt.scatter([i for i in range(len(o3_5_10) + len(o3_10_20), len(o3_5_10) + len(o3_10_20) + len(o3_20_50))],
    #          [i[0] for i in o3_20_50], label="20%-50% count: " + str(len(o3_20_50)))
    # plt.scatter([i for i in range(len(o3_5_10) + len(o3_10_20) + len(o3_20_50),
    #                            len(o3_5_10) + len(o3_10_20) + len(o3_20_50) + len(o3_50_75))], [i[0] for i in o3_50_75],
    #          label="50%-75% count: " + str(len(o3_50_75)))
    # plt.scatter([i for i in range(len(o3_5_10) + len(o3_10_20) + len(o3_20_50) + len(o3_50_75),
    #                            len(o3_5_10) + len(o3_10_20) + len(o3_20_50) + len(o3_50_75) + len(o3_75))],
    #          [i[0] for i in o3_75], label="75% count: " + str(len(o3_75)))
    # plt.legend()
    # plt.show()
    #
    # plt.title("O3NO2")
    # plt.scatter([i for i in range(len(o3no2_5_10))], [i[0] for i in o3no2_5_10],
    #          label="5%-10% count: " + str(len(o3no2_5_10)))
    # plt.scatter([i for i in range(len(o3no2_5_10), len(o3no2_5_10) + len(o3no2_10_20))], [i[0] for i in o3no2_10_20],
    #          label="10%-20% count: " + str(len(o3no2_10_20)))
    # plt.scatter(
    #     [i for i in range(len(o3no2_5_10) + len(o3no2_10_20), len(o3no2_5_10) + len(o3no2_10_20) + len(o3no2_20_50))],
    #     [i[0] for i in o3no2_20_50], label="20%-50% count: " + str(len(o3no2_20_50)))
    # plt.scatter([i for i in range(len(o3no2_5_10) + len(o3no2_10_20) + len(o3no2_20_50),
    #                            len(o3no2_5_10) + len(o3no2_10_20) + len(o3no2_20_50) + len(o3no2_50_75))],
    #          [i[0] for i in o3no2_50_75],
    #          label="50%-75% count: " + str(len(o3no2_50_75)))
    # plt.scatter([i for i in range(len(o3no2_5_10) + len(o3no2_10_20) + len(o3no2_20_50) + len(o3no2_50_75),
    #                            len(o3no2_5_10) + len(o3no2_10_20) + len(o3no2_20_50) + len(o3no2_50_75) + len(
    #                                o3no2_75))],
    #          [i[0] for i in o3no2_75], label="75% count: " + str(len(o3no2_75)))
    # plt.legend()
    # plt.show()

def fivePer(num):
    return abs(num / 20)


def tenPer(num):
    return abs(num / 10)


def twentyPer(num):
    return abs(num / 5)


def fivetyPer(num):
    return abs(num / 2)


def SeventyfivePer(num):
    return abs(num * 3 / 4)


