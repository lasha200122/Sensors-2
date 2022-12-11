import random
import numpy as np


def Clustering3d(x, y, z, n, p):
    if n <= 1:
        return None
    length = len(x)
    if length != len(y):
        return None
    indexes = []
    for i in range(n):
        indexes.append(RandomNumber(length, indexes))

    clusters = [(x[i], y[i], z[i]) for i in indexes]
    newClusters, dictionary = Grouping(clusters, x, y, z, p)  # dictionary -> Key: [(x,y, z)...]

    return newClusters, dictionary, indexes


def Grouping(clusters, x, y, z, p, count=0):
    dictionary = {}
    print("Grouping Clusters step: " + str(count))
    for index, dot in enumerate(x):
        distances = []  # [(key, distance)]
        for key, cluster in enumerate(clusters):
            if key not in dictionary:
                dictionary[key] = []
            vector = [cluster[0] - dot, cluster[1] - y[index], cluster[2] - z[index]]
            distance = NormP(vector, p)
            distances.append((key, distance))
        key = min(distances, key=lambda tup: tup[1])[0]  # Getting Key
        dictionary[key].append((dot, y[index], z[index]))

    result = []
    for key, cluster in enumerate(clusters):
        if len(dictionary[key]) == 0:
            result.append(cluster)
        else:
            cluster_x = sum([i[0] for i in dictionary[key]]) / len(dictionary[key])
            cluster_y = sum([i[1] for i in dictionary[key]]) / len(dictionary[key])
            cluster_z = sum([i[2] for i in dictionary[key]]) / len(dictionary[key])
            result.append((cluster_x, cluster_y, cluster_z))

    if Stop(clusters, result) < 0.000001:
        return result, dictionary
    return Grouping(result, x, y, z, p, count+1)


def RandomNumber(n, indexes, count=0):
    if count == 10:
        return None
    number = random.randint(0, n-1)
    if number in indexes:
        return RandomNumber(n, indexes, count+1)
    return number


def Stop(clusters, newClusters):
    error = 0
    for index, cluster in enumerate(clusters):
        vector = [cluster[0] - newClusters[index][0], cluster[1] - newClusters[index][1],  cluster[2] - newClusters[index][2]]
        distance = NormP(vector, 2)
        error += distance
    return error


def NormInf(x):
    return max([abs(i) for i in x])


def NormP(x, p):
    if p == "inf":
        return NormInf(x)
    return np.power(sum([np.power(abs(i), p) for i in x]), 1/p)


def UniqueClustering(x, y, z, n, p):
    if n <= 1:
        return None
    if len(x) != len(y) != len(z):
        return None

    points = [[i, j, k] for i, j, k in zip(x, y, z)]  # --> [x, y, z]
    length = len(points)
    if len(points) <= 1:
        return None
    if n == 2:
        indexes = [0, len(points) // 2]
    else:
        indexes = []
        for i in range(n):
            indexes.append(RandomNumber(length, indexes))

    centroids = [points[i] for i in indexes]

    result = UniqueGrouping(centroids, points, p)

    return result


def UniqueGrouping(centroids, points, p, step=0):
    print("Step: " + str(step))
    dictionary = {}
    for point in points:
        distances = []
        for key, centroid in enumerate(centroids):
            if key not in dictionary.keys():
                dictionary[key] = []
            vector = [centroid[0] - point[0], centroid[1] - point[1], centroid[2] - point[2]]
            distance = NormP(vector, p)
            distances.append((key, distance))
        key = min(distances, key=lambda tup: tup[1])[0]
        dictionary[key].append(point)

    newCentroids = []
    for key in dictionary.keys():
        if len(dictionary[key]) == 0:
            newCentroid = [centroids[key][0], centroids[key][1], centroids[key][2]]
            newCentroids.append(newCentroid)
        else:
            length = len(dictionary[key])
            new_x = sum([i[0] for i in dictionary[key]]) / length
            new_y = sum([i[1] for i in dictionary[key]]) / length
            new_z = sum([i[2] for i in dictionary[key]]) / length
            newCentroid = [new_x, new_y, new_z]
            newCentroids.append(newCentroid)

    if UniqueStop(centroids, newCentroids) < 0.000001:
        result = {}
        for i in range(len(newCentroids)):
            newCentroids[i] = (newCentroids[i][0], newCentroids[i][1], newCentroids[i][2])
        for key, centroid in enumerate(newCentroids):
            if centroid not in result.keys():
                result[centroid] = []
            for c in dictionary[key]:
                result[centroid].append(c)
        return result

    return UniqueGrouping(newCentroids, points, p, step+1)


def UniqueStop(centroids, newCentroids):
    error = 0
    for centroid, newCentroid in zip(centroids, newCentroids):
        vector = [centroid[0] - newCentroid[0], centroid[1] - newCentroid[1], centroid[2] - newCentroid[2]]
        distance = NormP(vector, 2)
        error += distance
    return error


def ClusterIntersections(dictionary, n, p, step=0):
    if step >= 100:
        return dictionary
    print(step)
    key = any(dictionary)
    if key is not None:
        x = [i[0] for i in dictionary[key]]
        y = [i[1] for i in dictionary[key]]
        z = [i[2] for i in dictionary[key]]
        del dictionary[key]
        newCentroids = UniqueClustering(x, y, z, n, p)
        if newCentroids is None:
            return ClusterIntersections(dictionary, 2, 2, step+1)

        for k in newCentroids.keys():
            dictionary[k] = []
            for i in newCentroids[k]:
                dictionary[k].append(i)

        return ClusterIntersections(dictionary, n, p, step+1)
    return dictionary


def any(dictionary):
    keys = list(dictionary.keys())
    for i in range(len(keys)-1):
        for j in range(i+1, len(keys)):
            c1 = keys[i]
            c2 = keys[j]
            c1d = [NormP([i[0] - c1[0], i[1] - c1[1], i[2] - c1[2]], 2) for i in dictionary[c1]]
            c2d = [NormP([i[0] - c2[0], i[1] - c2[1], i[2] - c2[2]], 2) for i in dictionary[c2]]
            c1R = max(c1d, default=0)
            c2R = max(c2d, default=0)
            if Intersection(c1[0], c1[1], c1[2], c2[0], c2[1], c2[2], c1R, c2R):
                return c1
    return None


def Intersection(x1, y1, z1, x2, y2, z2, r1, r2):
    o = np.sqrt(np.power(x1-x2, 2) + np.power(y1 - y2, 2) + np.power(z1 - z2, 2))
    if o <= r1 - r2:
        return True
    if o <= r2 - r1:
        return True
    if o < r1 + r2:
        return True
    if o == r1 + r2:
        return True
    return False


def ShrinkClusters(dictionary, n, p, step=0):
    if step >= 100:
        return dictionary
    print(step)
    key = CheckRadius(dictionary)
    if key is not None:
        x = [i[0] for i in dictionary[key]]
        y = [i[1] for i in dictionary[key]]
        z = [i[2] for i in dictionary[key]]
        del dictionary[key]
        newCentroids = UniqueClustering(x, y, z, n, p)
        if newCentroids is None:
            return ShrinkClusters(dictionary, 2, 2, step+1)

        for k in newCentroids.keys():
            dictionary[k] = []
            for i in newCentroids[k]:
                dictionary[k].append(i)

        return ShrinkClusters(dictionary, n, p, step+1)
    return dictionary


def CheckRadius(dictionary):
    for key in dictionary.keys():
        vector = [NormP([i[0] - key[0], i[1] - key[1], i[2] - key[2]], 2) for i in dictionary[key]]
        radius = max(vector, default=0)
        if radius >= 0.000001:
            return key
    return None


def Clean(dictionary):
    keys = list(dictionary.keys())
    for key in keys:
        vector = [NormP([i[0] - key[0], i[1] - key[1], i[2] - key[2]], 2) for i in dictionary[key]]
        radius = max(vector, default=0)
        if radius == 0:
            del dictionary[key]
    return dictionary


def UniqueClustering2D(x, y, n, p):
    if n <= 1:
        return None
    if len(x) != len(y):
        return None

    points = [[i, j] for i, j in zip(x, y)]
    length = len(points)
    if len(points) <= 1:
        return None
    if n == 2:
        indexes = [0, len(points) // 2]
    else:
        indexes = []
        for i in range(n):
            indexes.append(RandomNumber(length, indexes))

    centroids = [points[i] for i in indexes]

    result = UniqueGrouping2D(centroids, points, p)

    return result


def UniqueGrouping2D(centroids, points, p, step=0):
    print("Step: " + str(step))
    dictionary = {}
    for point in points:
        distances = []
        for key, centroid in enumerate(centroids):
            if key not in dictionary.keys():
                dictionary[key] = []
            vector = [centroid[0] - point[0], centroid[1] - point[1]]
            distance = NormP(vector, p)
            distances.append((key, distance))
        key = min(distances, key=lambda tup: tup[1])[0]
        dictionary[key].append(point)

    newCentroids = []
    for key in dictionary.keys():
        if len(dictionary[key]) == 0:
            newCentroid = [centroids[key][0], centroids[key][1]]
            newCentroids.append(newCentroid)
        else:
            length = len(dictionary[key])
            new_x = sum([i[0] for i in dictionary[key]]) / length
            new_y = sum([i[1] for i in dictionary[key]]) / length
            newCentroid = [new_x, new_y]
            newCentroids.append(newCentroid)

    if UniqueStop2D(centroids, newCentroids) < 0.000001:
        result = {}
        for i in range(len(newCentroids)):
            newCentroids[i] = (newCentroids[i][0], newCentroids[i][1])
        for key, centroid in enumerate(newCentroids):
            if centroid not in result.keys():
                result[centroid] = []
            for c in dictionary[key]:
                result[centroid].append(c)
        return result

    return UniqueGrouping2D(newCentroids, points, p, step+1)


def UniqueStop2D(centroids, newCentroids):
    error = 0
    for centroid, newCentroid in zip(centroids, newCentroids):
        vector = [centroid[0] - newCentroid[0], centroid[1] - newCentroid[1]]
        distance = NormP(vector, 2)
        error += distance
    return error


def Intersection2D(x1, y1, x2, y2, r1, r2):
    o = np.sqrt(np.power(x1-x2, 2) + np.power(y1 - y2, 2))
    if o <= r1 - r2:
        return True
    if o <= r2 - r1:
        return True
    if o < r1 + r2:
        return True
    if o == r1 + r2:
        return True
    return False


def any2D(dictionary):
    keys = list(dictionary.keys())
    for i in range(len(keys)-1):
        for j in range(i+1, len(keys)):
            c1 = keys[i]
            c2 = keys[j]
            c1d = [NormP([i[0] - c1[0], i[1] - c1[1]], 2) for i in dictionary[c1]]
            c2d = [NormP([i[0] - c2[0], i[1] - c2[1]], 2) for i in dictionary[c2]]
            c1R = max(c1d, default=0)
            c2R = max(c2d, default=0)
            if Intersection2D(c1[0], c1[1], c2[0], c2[1], c1R, c2R):
                return c1
    return None


def ClusterIntersections2D(dictionary, n, p, step=0):
    if step >= 100:
        return dictionary
    print(step)
    key = any2D(dictionary)
    if key is not None:
        x = [i[0] for i in dictionary[key]]
        y = [i[1] for i in dictionary[key]]
        del dictionary[key]
        newCentroids = UniqueClustering2D(x, y, n, p)
        if newCentroids is None:
            return ClusterIntersections2D(dictionary, 2, 2, step+1)

        for k in newCentroids.keys():
            dictionary[k] = []
            for i in newCentroids[k]:
                dictionary[k].append(i)

        return ClusterIntersections2D(dictionary, n, p, step+1)
    return dictionary


def ShrinkClusters2D(dictionary, n, p, step=0):
    if step >= 100:
        return dictionary
    print(step)
    key = CheckRadius2D(dictionary)
    if key is not None:
        x = [i[0] for i in dictionary[key]]
        y = [i[1] for i in dictionary[key]]
        del dictionary[key]
        newCentroids = UniqueClustering2D(x, y, n, p)
        if newCentroids is None:
            return ShrinkClusters2D(dictionary, 2, 2, step+1)

        for k in newCentroids.keys():
            dictionary[k] = []
            for i in newCentroids[k]:
                dictionary[k].append(i)

        return ShrinkClusters2D(dictionary, n, p, step+1)
    return dictionary


def CheckRadius2D(dictionary):
    for key in dictionary.keys():
        vector = [NormP([i[0] - key[0], i[1] - key[1]], 2) for i in dictionary[key]]
        radius = max(vector, default=0)
        if radius >= 0.000001:
            return key
    return None


def Clean2D(dictionary):
    keys = list(dictionary.keys())
    for key in keys:
        vector = [NormP([i[0] - key[0], i[1] - key[1]], 2) for i in dictionary[key]]
        radius = max(vector, default=0)
        if radius == 0:
            del dictionary[key]
    return dictionary
