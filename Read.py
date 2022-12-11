"""
ამ ფოლდერში გაწერილია ლოგიკა რომ ამოვიღოთ ყველა მონაცემი excel-ებიდან.
ექსელის გასახსნელად ვიყენებთ pandas ბიბლიოთეკას, Path ფაილს რომ
მივწვდეთ ფაილების მისამართებს და Modeles ფაილს ინფორმაციის შესანახად
"""

import pandas as pd
import Paths
import Models


def GetData():
    # პირველ რიგში NEA-ს მონაცემებს ვპოულობთ ყოველი წუთისთვის
    NEA = []  # example -> [obj1, obj2, ...]
    missedDates = []
    for sheet in Paths.sheets:  # ყოველი sheet თითო დღეა
        nea = pd.read_excel(Paths.nea, sheet_name=sheet)

        for co, no, no2, o3, date in zip(nea[Paths.neaCO], nea[Paths.neaNO], nea[Paths.neaNO2], nea[Paths.neaO3],
                                         nea[Paths.neaDate]):
            if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
                minute = str(date).split(" ")[1].split(":")[1]
                if len(minute) == 1:
                    minute = int(minute)
                else:
                    if minute[0] == '0':
                        minute = int(minute[1])
                    else:
                        minute = int(minute)
                container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
                                          str(date) + ":00", minute,0)
                NEA.append(container)
            else:
                missedDates.append(str(date))
    print("NEA-ს excel-იდან ამოღებულია: " + str(len(NEA)) + " მონაცემი.")
    print("NEA-ს excel-ში ნაპოვნია " + str(len(missedDates)) + " დაზიანებული მონაცემი")

    Seconds = []

    file = pd.read_csv("Alphasense_output.csv")  # minute second

    for co, no, no2, o3, minute, second, year, month, day, hour in zip(file[Paths.secondCO], file[Paths.secondNO], file[Paths.secondNO2],
                                               file[Paths.secondO3], file["minute"], file["second"], file["year"], file["month"], file["day"], file["hour"]):
        if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3):
            if len(str(hour)) == 1:
                hour = "0" + str(hour)
            if len(str(minute)) == 1:
                minute = "0" + str(minute)
            if len(str(second)) == 1:
                second = "0" + str(second)
            d = str(day) + "/" + str(month) + "/" + str(year) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
            container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
                                      d, minute, second)
            Seconds.append(container)
    print("წამებიდან ამოღებულია: " + str(len(Seconds)) + " მონაცემი.")

    # # პირველ რიგში NEA-ს მონაცემებს ვპოულობთ ყოველი წუთისთვის
    # NEA = []  # example -> [obj1, obj2, ...]
    # missedDates = []
    # for sheet in Paths.sheets:  # ყოველი sheet თითო დღეა
    #     nea = pd.read_excel(Paths.nea, sheet_name=sheet)
    #
    #     for co, no, no2, o3, date in zip(nea[Paths.neaCO], nea[Paths.neaNO], nea[Paths.neaNO2], nea[Paths.neaO3],
    #                                      nea[Paths.neaDate]):
    #         if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
    #             minute = str(date).split(" ")[1].split(":")[1]
    #             if len(minute) == 1:
    #                 minute = int(minute)
    #             else:
    #                 if minute[0] == '0':
    #                     minute = int(minute[1])
    #             container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
    #                                       str(date) + ":00", minute, 0)
    #             NEA.append(container)
    #         else:
    #             missedDates.append(str(date))
    # print("NEA-ს excel-იდან ამოღებულია: " + str(len(NEA)) + " მონაცემი.")
    # print("NEA-ს excel-ში ნაპოვნია " + str(len(missedDates)) + " დაზიანებული მონაცემი")
    #
    # # ახლა ამოვიღოთ მონაცემები წამობრივი სენსორებიდან
    # Seconds = []  # example -> [obj1, obj2, ...]
    #
    # # for excel in Paths.excels:  # თითო excel ერთი დღის მონაცემებია
    # #     second = pd.read_excel(excel)
    # #     print("იტვირთება ფაილი: " + excel)
    # #
    # #     for co, no, no2, o3, o3no2, date in zip(second[Paths.secondCO], second[Paths.secondNO], second[Paths.secondNO2],
    # #                                             second[Paths.secondO3], second[Paths.secondO3NO2],
    # #                                             second[Paths.secondDate]):
    # #         if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
    # #             container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
    # #                                       str(date))
    # #             Seconds.append(container)
    # # print("წამებიდან ამოღებულია: " + str(len(Seconds)) + " მონაცემი.")
    #
    # file = pd.read_csv("Alphasense_output.csv")  # minute second
    #
    # for co, no, no2, o3, minute, second, year, month, day, hour in zip(file[Paths.secondCO], file[Paths.secondNO], file[Paths.secondNO2],
    #                                            file[Paths.secondO3], file["second"], file["minute"], file["year"], file["month"], file["day"], file["hour"]):
    #     if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3):
    #         if len(str(hour)) == 1:
    #             hour = "0" + str(hour)
    #         if len(str(minute)) == 1:
    #             minute = "0" + str(minute)
    #         if len(str(second)) == 1:
    #             second = "0" + str(second)
    #         d = str(day) + "/" + str(month) + "/" + str(year) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
    #         container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
    #                                   d, minute, second)
    #         Seconds.append(container)
    # print("წამებიდან ამოღებულია: " + str(len(Seconds)) + " მონაცემი.")

    # ახლა ვცადოთ გასაშუალება. ამ ჯერად ვაკეთებთ 9k-ზე ამიტომ 9 ქვესიმრავლე გვექნება

    linearSystems = Mean(Seconds, NEA, missedDates)
    print("შექმნილია: " + str(len(linearSystems)) + " ცალი წრფივი სისტემა")

    return linearSystems


def isfloat(num):  # ამ ფუნქციას ვიყენებ ექსელიდან ამოღებული ინფორმაციის შესამოწმებლად
    try:
        float(num)
        return True
    except ValueError:
        return False


def Mean(seconds, nea, missedDates):  # ამ ფუნქციით ვპოულობთ კოეფიციენტებს
    result = []
    start = 0
    neaIndex = 0
    n = len(seconds)

    while start < n:
        interval = []
        doInterval = True
        for i in range(start, n):
            left = seconds[i].Date[:len(seconds[i].Date) - 3]
            # თუ NEA-ს მონაცემში დაზიანებული იყო მაშინ აქ მსგავსი დრო არ განიხილოს
            if left in missedDates:
                start += 1
                doInterval = False
                break
            if i == n-1:
                interval.append(seconds[i])
                start = n
                break
            if seconds[i].Date.split(" ")[1].split(":")[1] != seconds[start].Date.split(" ")[1].split(":")[1]:
                start = i
                neaIndex += 1
                break
            interval.append(seconds[i])
        if doInterval and neaIndex - 1 < len(nea):
            system = Subseqtion(interval)
            system.append(nea[neaIndex-1])
            result.append(system)
    return result


def Subseqtion(interval):
    S1 = []
    S2 = []
    S3 = []
    S4 = []
    S5 = []
    S6 = []
    S7 = []
    S8 = []
    S9 = []
    index = 0
    length = len(interval)
    while index < length:
        if index < length:
            S1.append(interval[index])
        if index + 1 < length:
            S2.append(interval[index + 1])
        if index + 2 < length:
            S3.append(interval[index + 2])
        if index + 3 < length:
            S4.append(interval[index + 3])
        if index + 4 < length:
            S5.append(interval[index + 4])
        if index + 5 < length:
            S6.append(interval[index + 5])
        if index + 6 < length:
            S7.append(interval[index + 6])
        if index + 7 < length:
            S8.append(interval[index + 7])
        if index + 8 < length:
            S9.append(interval[index + 8])
        index += 9

    c1 = CalculatingMean(S1)
    c2 = CalculatingMean(S2)
    c3 = CalculatingMean(S3)
    c4 = CalculatingMean(S4)
    c5 = CalculatingMean(S5)
    c6 = CalculatingMean(S6)
    c7 = CalculatingMean(S7)
    c8 = CalculatingMean(S8)
    c9 = CalculatingMean(S9)

    return [c1, c2, c3, c4, c5, c6, c7, c8, c9]


def CalculatingMean(S):
    c = Models.Object(0., 0., 0., 0., 0., "", 0, 0)
    for obj in S:
        c.CO += obj.CO
        c.NO += obj.NO
        c.NO2 += obj.NO2
        c.O3 += obj.O3
        c.O3NO2 += obj.O3NO2

    n = len(S)

    if n != 0:
        c.CO /= n
        c.NO /= n
        c.NO2 /= n
        c.O3 /= n
        c.O3NO2 /= n

    return c


def GetData15():
    # # პირველ რიგში NEA-ს მონაცემებს ვპოულობთ ყოველი წუთისთვის
    # NEA = []  # example -> [obj1, obj2, ...]
    # missedDates = []
    # for sheet in Paths.sheets:  # ყოველი sheet თითო დღეა
    #     nea = pd.read_excel(Paths.nea, sheet_name=sheet)
    #
    #     for co, no, no2, o3, date in zip(nea[Paths.neaCO], nea[Paths.neaNO], nea[Paths.neaNO2], nea[Paths.neaO3],
    #                                      nea[Paths.neaDate]):
    #         if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
    #             container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
    #                                       str(date) + ":00")
    #             NEA.append(container)
    #         else:
    #             missedDates.append(str(date))
    # print("NEA-ს excel-იდან ამოღებულია: " + str(len(NEA)) + " მონაცემი.")
    # print("NEA-ს excel-ში ნაპოვნია " + str(len(missedDates)) + " დაზიანებული მონაცემი")
    #
    # # ახლა ამოვიღოთ მონაცემები წამობრივი სენსორებიდან
    # Seconds = []  # example -> [obj1, obj2, ...]
    #
    # for excel in Paths.excels:  # თითო excel ერთი დღის მონაცემებია
    #     second = pd.read_excel(excel)
    #     print("იტვირთება ფაილი: " + excel)
    #
    #     for co, no, no2, o3, o3no2, date in zip(second[Paths.secondCO], second[Paths.secondNO], second[Paths.secondNO2],
    #                                             second[Paths.secondO3], second[Paths.secondO3NO2],
    #                                             second[Paths.secondDate]):
    #         if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
    #             container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
    #                                       str(date))
    #             Seconds.append(container)
    # print("წამებიდან ამოღებულია: " + str(len(Seconds)) + " მონაცემი.")

    # ახლა ვცადოთ გასაშუალება. ამ ჯერად ვაკეთებთ 15-15-15-15 ინტერვალებზე

    # პირველ რიგში NEA-ს მონაცემებს ვპოულობთ ყოველი წუთისთვის
    NEA = []  # example -> [obj1, obj2, ...]
    missedDates = []
    for sheet in Paths.sheets:  # ყოველი sheet თითო დღეა
        nea = pd.read_excel(Paths.nea, sheet_name=sheet)

        for co, no, no2, o3, date in zip(nea[Paths.neaCO], nea[Paths.neaNO], nea[Paths.neaNO2], nea[Paths.neaO3],
                                         nea[Paths.neaDate]):
            if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
                minute = str(date).split(" ")[1].split(":")[1]
                if len(minute) == 1:
                    minute = int(minute)
                else:
                    if minute[0] == '0':
                        minute = int(minute[1])
                    else:
                        minute = int(minute)
                container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
                                          str(date) + ":00", minute,0)
                NEA.append(container)
            else:
                missedDates.append(str(date))
    print("NEA-ს excel-იდან ამოღებულია: " + str(len(NEA)) + " მონაცემი.")
    print("NEA-ს excel-ში ნაპოვნია " + str(len(missedDates)) + " დაზიანებული მონაცემი")

    Seconds = []

    file = pd.read_csv("Alphasense_output.csv")  # minute second

    for co, no, no2, o3, minute, second, year, month, day, hour in zip(file[Paths.secondCO], file[Paths.secondNO], file[Paths.secondNO2],
                                               file[Paths.secondO3], file["minute"], file["second"], file["year"], file["month"], file["day"], file["hour"]):
        if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3):
            if len(str(hour)) == 1:
                hour = "0" + str(hour)
            if len(str(minute)) == 1:
                minute = "0" + str(minute)
            if len(str(second)) == 1:
                second = "0" + str(second)
            d = str(day) + "/" + str(month) + "/" + str(year) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
            container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
                                      d, minute, second)
            Seconds.append(container)
    print("წამებიდან ამოღებულია: " + str(len(Seconds)) + " მონაცემი.")


    linearSystems = fourFifteen(Seconds, NEA, missedDates)

    print("შექმნილია: " + str(len(linearSystems)) + " ცალი წრფივი სისტემა")

    return linearSystems


def GetData9():
    # # პირველ რიგში NEA-ს მონაცემებს ვპოულობთ ყოველი წუთისთვის
    # NEA = []  # example -> [obj1, obj2, ...]
    # missedDates = []
    # for sheet in Paths.sheets:  # ყოველი sheet თითო დღეა
    #     nea = pd.read_excel(Paths.nea, sheet_name=sheet)
    #
    #     for co, no, no2, o3, date in zip(nea[Paths.neaCO], nea[Paths.neaNO], nea[Paths.neaNO2], nea[Paths.neaO3],
    #                                      nea[Paths.neaDate]):
    #         if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
    #             container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
    #                                       str(date) + ":00")
    #             NEA.append(container)
    #         else:
    #             missedDates.append(str(date))
    # print("NEA-ს excel-იდან ამოღებულია: " + str(len(NEA)) + " მონაცემი.")
    # print("NEA-ს excel-ში ნაპოვნია " + str(len(missedDates)) + " დაზიანებული მონაცემი")
    #
    # # ახლა ამოვიღოთ მონაცემები წამობრივი სენსორებიდან
    # Seconds = []  # example -> [obj1, obj2, ...]
    #
    # for excel in Paths.excels:  # თითო excel ერთი დღის მონაცემებია
    #     second = pd.read_excel(excel)
    #     print("იტვირთება ფაილი: " + excel)
    #
    #     for co, no, no2, o3, o3no2, date in zip(second[Paths.secondCO], second[Paths.secondNO], second[Paths.secondNO2],
    #                                             second[Paths.secondO3], second[Paths.secondO3NO2],
    #                                             second[Paths.secondDate]):
    #         if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
    #             container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
    #                                       str(date))
    #             Seconds.append(container)
    # print("წამებიდან ამოღებულია: " + str(len(Seconds)) + " მონაცემი.")

    # ახლა ვცადოთ გასაშუალება. ამ ჯერად ვაკეთებთ 15-15-15-15 ინტერვალებზე

    # პირველ რიგში NEA-ს მონაცემებს ვპოულობთ ყოველი წუთისთვის
    NEA = []  # example -> [obj1, obj2, ...]
    missedDates = []
    for sheet in Paths.sheets:  # ყოველი sheet თითო დღეა
        nea = pd.read_excel(Paths.nea, sheet_name=sheet)

        for co, no, no2, o3, date in zip(nea[Paths.neaCO], nea[Paths.neaNO], nea[Paths.neaNO2], nea[Paths.neaO3],
                                         nea[Paths.neaDate]):
            if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
                minute = str(date).split(" ")[1].split(":")[1]
                if len(minute) == 1:
                    minute = int(minute)
                else:
                    if minute[0] == '0':
                        minute = int(minute[1])
                    else:
                        minute = int(minute)
                container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
                                          str(date) + ":00", minute, 0)
                NEA.append(container)
            else:
                missedDates.append(str(date))
    print("NEA-ს excel-იდან ამოღებულია: " + str(len(NEA)) + " მონაცემი.")
    print("NEA-ს excel-ში ნაპოვნია " + str(len(missedDates)) + " დაზიანებული მონაცემი")

    Seconds = []

    file = pd.read_csv("Alphasense_output.csv")  # minute second

    for co, no, no2, o3, minute, second, year, month, day, hour in zip(file[Paths.secondCO], file[Paths.secondNO],
                                                                       file[Paths.secondNO2],
                                                                       file[Paths.secondO3], file["minute"],
                                                                       file["second"], file["year"], file["month"],
                                                                       file["day"], file["hour"]):
        if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3):
            if len(str(hour)) == 1:
                hour = "0" + str(hour)
            if len(str(minute)) == 1:
                minute = "0" + str(minute)
            if len(str(second)) == 1:
                second = "0" + str(second)
            d = str(day) + "/" + str(month) + "/" + str(year) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
            container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
                                      d, minute, second)
            Seconds.append(container)
    print("წამებიდან ამოღებულია: " + str(len(Seconds)) + " მონაცემი.")

    linearSystems = NineSeven(Seconds, NEA, missedDates)

    print("შექმნილია: " + str(len(linearSystems)) + " ცალი წრფივი სისტემა")

    return linearSystems


def fourFifteen(seconds, nea, missedDates):
    result = []
    start = 0
    neaIndex = 0
    n = len(seconds)

    while start < n:
        interval = []
        doInterval = True
        for i in range(start, n):
            left = seconds[i].Date[:len(seconds[i].Date) - 3]
            # თუ NEA-ს მონაცემში დაზიანებული იყო მაშინ აქ მსგავსი დრო არ განიხილოს
            if left in missedDates:
                start += 1
                doInterval = False
                break
            if i == n-1:
                interval.append(seconds[i])
                start = n
                break
            if seconds[i].Date.split(" ")[1].split(":")[1] != seconds[start].Date.split(" ")[1].split(":")[1]:
                start = i
                neaIndex += 1
                break
            interval.append(seconds[i])
        if doInterval and neaIndex - 1 < len(nea):
            system = Get15values(interval)
            system.append(nea[neaIndex-1])
            result.append(system)
    return result


def NineSeven(seconds, nea, missedDates):
    result = []
    start = 0
    neaIndex = 0
    n = len(seconds)

    while start < n:
        interval = []
        doInterval = True
        for i in range(start, n):
            left = seconds[i].Date[:len(seconds[i].Date) - 3]
            # თუ NEA-ს მონაცემში დაზიანებული იყო მაშინ აქ მსგავსი დრო არ განიხილოს
            if left in missedDates:
                start += 1
                doInterval = False
                break
            if i == n-1:
                interval.append(seconds[i])
                start = n
                break
            if seconds[i].Date.split(" ")[1].split(":")[1] != seconds[start].Date.split(" ")[1].split(":")[1]:
                start = i
                neaIndex += 1
                break
            interval.append(seconds[i])
        if doInterval and neaIndex - 1 < len(nea):
            system = Get9values(interval)
            system.append(nea[neaIndex-1])
            result.append(system)
    return result


def Get9values(interval):
    S1 = []
    S2 = []
    S3 = []
    S4 = []
    S5 = []
    S6 = []
    S7 = []
    S8 = []
    S9 = []

    for obj in interval:
        second = obj.Date.split(" ")[1].split(":")[2]
        if second in Paths.F9_1:
            S1.append(obj)
        if second in Paths.F9_2:
            S2.append(obj)
        if second in Paths.F9_3:
            S3.append(obj)
        if second in Paths.F9_4:
            S4.append(obj)
        if second in Paths.F9_5:
            S5.append(obj)
        if second in Paths.F9_6:
            S6.append(obj)
        if second in Paths.F9_7:
            S7.append(obj)
        if second in Paths.F9_8:
            S8.append(obj)
        if second in Paths.F9_9:
            S9.append(obj)

    c1 = CalculatingMean(S1)
    c2 = CalculatingMean(S2)
    c3 = CalculatingMean(S3)
    c4 = CalculatingMean(S4)
    c5 = CalculatingMean(S5)
    c6 = CalculatingMean(S6)
    c7 = CalculatingMean(S7)
    c8 = CalculatingMean(S8)
    c9 = CalculatingMean(S9)

    return [c1, c2, c3, c4, c5, c6, c7, c8, c9]


def Get15values(interval):
    S1 = []
    S2 = []
    S3 = []
    S4 = []

    for obj in interval:
        second = obj.Date.split(" ")[1].split(":")[2]
        if second in Paths.First15:
            S1.append(obj)
        if second in Paths.Seconds15:
            S2.append(obj)
        if second in Paths.Third15:
            S3.append(obj)
        if second in Paths.Fourth15:
            S4.append(obj)

    c1 = CalculatingMean(S1)
    c2 = CalculatingMean(S2)
    c3 = CalculatingMean(S3)
    c4 = CalculatingMean(S4)

    return [c1, c2, c3, c4]


def GetDataMinMax():
    # # პირველ რიგში NEA-ს მონაცემებს ვპოულობთ ყოველი წუთისთვის
    # NEA = []  # example -> [obj1, obj2, ...]
    # missedDates = []
    # for sheet in Paths.sheets:  # ყოველი sheet თითო დღეა
    #     nea = pd.read_excel(Paths.nea, sheet_name=sheet)
    #
    #     for co, no, no2, o3, date in zip(nea[Paths.neaCO], nea[Paths.neaNO], nea[Paths.neaNO2], nea[Paths.neaO3],
    #                                      nea[Paths.neaDate]):
    #         if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
    #             container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
    #                                       str(date) + ":00")
    #             NEA.append(container)
    #         else:
    #             missedDates.append(str(date))
    # print("NEA-ს excel-იდან ამოღებულია: " + str(len(NEA)) + " მონაცემი.")
    # print("NEA-ს excel-ში ნაპოვნია " + str(len(missedDates)) + " დაზიანებული მონაცემი")
    #
    # # ახლა ამოვიღოთ მონაცემები წამობრივი სენსორებიდან
    # Seconds = []  # example -> [obj1, obj2, ...]
    #
    # for excel in Paths.excels:  # თითო excel ერთი დღის მონაცემებია
    #     second = pd.read_excel(excel)
    #     print("იტვირთება ფაილი: " + excel)
    #
    #     for co, no, no2, o3, o3no2, date in zip(second[Paths.secondCO], second[Paths.secondNO], second[Paths.secondNO2],
    #                                             second[Paths.secondO3], second[Paths.secondO3NO2],
    #                                             second[Paths.secondDate]):
    #         if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
    #             container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
    #                                       str(date))
    #             Seconds.append(container)
    # print("წამებიდან ამოღებულია: " + str(len(Seconds)) + " მონაცემი.")
    #
    # # ახლა ვცადოთ გასაშუალება. ამ ჯერად ვაკეთებთ მაქსიმუმს და მინიმუმს 30-30 ინტერვალზე

    # პირველ რიგში NEA-ს მონაცემებს ვპოულობთ ყოველი წუთისთვის
    NEA = []  # example -> [obj1, obj2, ...]
    missedDates = []
    for sheet in Paths.sheets:  # ყოველი sheet თითო დღეა
        nea = pd.read_excel(Paths.nea, sheet_name=sheet)

        for co, no, no2, o3, date in zip(nea[Paths.neaCO], nea[Paths.neaNO], nea[Paths.neaNO2], nea[Paths.neaO3],
                                         nea[Paths.neaDate]):
            if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
                minute = str(date).split(" ")[1].split(":")[1]
                if len(minute) == 1:
                    minute = int(minute)
                else:
                    if minute[0] == '0':
                        minute = int(minute[1])
                    else:
                        minute = int(minute)
                container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
                                          str(date) + ":00", minute, 0)
                NEA.append(container)
            else:
                missedDates.append(str(date))
    print("NEA-ს excel-იდან ამოღებულია: " + str(len(NEA)) + " მონაცემი.")
    print("NEA-ს excel-ში ნაპოვნია " + str(len(missedDates)) + " დაზიანებული მონაცემი")

    Seconds = []

    file = pd.read_csv("Alphasense_output.csv")  # minute second

    for co, no, no2, o3, minute, second, year, month, day, hour in zip(file[Paths.secondCO], file[Paths.secondNO],
                                                                       file[Paths.secondNO2],
                                                                       file[Paths.secondO3], file["minute"],
                                                                       file["second"], file["year"], file["month"],
                                                                       file["day"], file["hour"]):
        if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3):
            if len(str(hour)) == 1:
                hour = "0" + str(hour)
            if len(str(minute)) == 1:
                minute = "0" + str(minute)
            if len(str(second)) == 1:
                second = "0" + str(second)
            d = str(day) + "/" + str(month) + "/" + str(year) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
            container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
                                      d, minute, second)
            Seconds.append(container)
    print("წამებიდან ამოღებულია: " + str(len(Seconds)) + " მონაცემი.")

    linearSystems = MinMAX(Seconds, NEA, missedDates)

    print("შექმნილია: " + str(len(linearSystems)) + " ცალი წრფივი სისტემა")

    return linearSystems


def MinMAX(seconds, nea, missedDates):
    result = []
    start = 0
    neaIndex = 0
    n = len(seconds)

    while start < n:
        interval = []
        doInterval = True
        for i in range(start, n):
            left = seconds[i].Date[:len(seconds[i].Date) - 3]
            # თუ NEA-ს მონაცემში დაზიანებული იყო მაშინ აქ მსგავსი დრო არ განიხილოს
            if left in missedDates:
                start += 1
                doInterval = False
                break
            if i == n-1:
                interval.append(seconds[i])
                start = n
                break
            if seconds[i].Date.split(" ")[1].split(":")[1] != seconds[start].Date.split(" ")[1].split(":")[1]:
                start = i
                neaIndex += 1
                break
            interval.append(seconds[i])
        if doInterval and neaIndex - 1 < len(nea):
            system = GetMINMAXvalues(interval)
            system.append(nea[neaIndex-1])
            result.append(system)
    return result


def GetMINMAXvalues(interval):
    S1 = []
    S2 = []

    for obj in interval:
        second = obj.Date.split(" ")[1].split(":")[2]
        if second in Paths.First15 + Paths.Seconds15:
            S1.append(obj)
        if second in Paths.Third15 + Paths.Fourth15:
            S2.append(obj)

    c1 = MAX(S1)
    c2 = MIN(S1)
    c3 = MAX(S2)
    c4 = MIN(S2)

    return [c1, c2, c3, c4]


def MAX(S):
    c = Models.Object(0., 0., 0., 0., 0., "", 0, 0)
    c.CO = max([i.CO for i in S], default=0)
    c.NO = max([i.NO for i in S], default=0)
    c.NO2 = max([i.NO2 for i in S], default=0)
    c.O3 = max([i.O3 for i in S], default=0)
    c.O3NO2 = max([i.O3NO2 for i in S], default=0)

    return c


def MIN(S):
    c = Models.Object(0., 0., 0., 0., 0., "", 0, 0)
    c.CO = min([i.CO for i in S], default=0)
    c.NO = min([i.NO for i in S], default=0)
    c.NO2 = min([i.NO2 for i in S], default=0)
    c.O3 = min([i.O3 for i in S], default=0)
    c.O3NO2 = min([i.O3NO2 for i in S], default=0)

    return c


def Compearing():
    # პირველ რიგში NEA-ს მონაცემებს ვპოულობთ ყოველი წუთისთვის
    NEA = []  # example -> [obj1, obj2, ...]
    missedDates = []
    for sheet in Paths.sheets:  # ყოველი sheet თითო დღეა
        nea = pd.read_excel(Paths.nea, sheet_name=sheet)

        for co, no, no2, o3, date in zip(nea[Paths.neaCO], nea[Paths.neaNO], nea[Paths.neaNO2], nea[Paths.neaO3],
                                         nea[Paths.neaDate]):
            if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
                minute = str(date).split(" ")[1].split(":")[1]
                if len(minute) == 1:
                    minute = int(minute)
                else:
                    if minute[0] == '0':
                        minute = int(minute[1])
                    else:
                        minute = int(minute)
                container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
                                          str(date) + ":00", minute,0)
                NEA.append(container)
            else:
                missedDates.append(str(date))
    print("NEA-ს excel-იდან ამოღებულია: " + str(len(NEA)) + " მონაცემი.")
    print("NEA-ს excel-ში ნაპოვნია " + str(len(missedDates)) + " დაზიანებული მონაცემი")

    # ახლა ამოვიღოთ მონაცემები წამობრივი სენსორებიდან
    Seconds = []  # example -> [obj1, obj2, ...]

    for excel in Paths.excels:  # თითო excel ერთი დღის მონაცემებია
        second = pd.read_excel(excel)
        print("იტვირთება ფაილი: " + excel)

        for co, no, no2, o3, o3no2, date in zip(second[Paths.secondCO], second[Paths.secondNO], second[Paths.secondNO2],
                                                second[Paths.secondO3], second[Paths.secondO3NO2],
                                                second[Paths.secondDate]):
            if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
                container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
                                          str(date))
                Seconds.append(container)
    print("წამებიდან ამოღებულია: " + str(len(Seconds)) + " მონაცემი.")

    # ახლა ვცადოთ გასაშუალება. ამ ჯერად ვაკეთებთ 15-15-15-15 ინტერვალებზე

    linearSystems = MeanforOne(Seconds, NEA, missedDates)

    print("შექმნილია: " + str(len(linearSystems)) + " ცალი წრფივი სისტემა")

    return linearSystems


def MeanforOne(seconds, nea, missedDates):
    result = []
    start = 0
    neaIndex = 0
    n = len(seconds)

    while start < n:
        interval = []
        doInterval = True
        for i in range(start, n):
            left = seconds[i].Date[:len(seconds[i].Date) - 3]
            # თუ NEA-ს მონაცემში დაზიანებული იყო მაშინ აქ მსგავსი დრო არ განიხილოს
            if left in missedDates:

                start += 1
                doInterval = False
                break
            if i == n-1:
                interval.append(seconds[i])
                start = n
                break
            if seconds[i].Date.split(" ")[1].split(":")[1] != seconds[start].Date.split(" ")[1].split(":")[1]:
                start = i
                neaIndex += 1
                break
            interval.append(seconds[i])
        if doInterval and neaIndex-1 < len(nea):
            system = CalculatingMean(interval)
            result.append([system, nea[neaIndex-1]])

    return result


def ReadCsv():
    # პირველ რიგში NEA-ს მონაცემებს ვპოულობთ ყოველი წუთისთვის
    NEA = []  # example -> [obj1, obj2, ...]
    missedDates = []
    for sheet in Paths.sheets:  # ყოველი sheet თითო დღეა
        nea = pd.read_excel(Paths.nea, sheet_name=sheet)

        for co, no, no2, o3, date in zip(nea[Paths.neaCO], nea[Paths.neaNO], nea[Paths.neaNO2], nea[Paths.neaO3],
                                         nea[Paths.neaDate]):
            if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3) and date is not None:
                minute = str(date).split(" ")[1].split(":")[1]
                if len(minute) == 1:
                    minute = int(minute)
                else:
                    if minute[0] == '0':
                        minute = int(minute[1])
                    else:
                        minute = int(minute)
                container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
                                          str(date) + ":00", minute,0)
                NEA.append(container)
            else:
                missedDates.append(str(date))
    print("NEA-ს excel-იდან ამოღებულია: " + str(len(NEA)) + " მონაცემი.")
    print("NEA-ს excel-ში ნაპოვნია " + str(len(missedDates)) + " დაზიანებული მონაცემი")

    Seconds = []

    file = pd.read_csv("Alphasense_output.csv")  # minute second

    for co, no, no2, o3, minute, second, year, month, day, hour in zip(file[Paths.secondCO], file[Paths.secondNO], file[Paths.secondNO2],
                                               file[Paths.secondO3], file["minute"], file["second"], file["year"], file["month"], file["day"], file["hour"]):
        if isfloat(co) and isfloat(no) and isfloat(no2) and isfloat(o3):
            if len(str(hour)) == 1:
                hour = "0" + str(hour)
            if len(str(minute)) == 1:
                minute = "0" + str(minute)
            if len(str(second)) == 1:
                second = "0" + str(second)
            d = str(day) + "/" + str(month) + "/" + str(year) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
            container = Models.Object(float(co), float(no), float(no2), float(o3), float(o3) + float(no2),
                                      d, minute, second)
            Seconds.append(container)
    print("წამებიდან ამოღებულია: " + str(len(Seconds)) + " მონაცემი.")

    linearSystems = MeanforOne(Seconds, NEA, missedDates)

    print("შექმნილია: " + str(len(linearSystems)) + " სისტემა")

    return linearSystems
