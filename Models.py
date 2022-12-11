"""
ამ ფოლდერში გაწერილი იქნება მოდელები სადაც ინფორმაცია მარტივად შეინახება
"""


class Chemicals:
    CO = []
    NO = []
    NO2 = []
    O3 = []
    O3NO2 = []


class Object:
    CO = 0.
    NO = 0.
    NO2 = 0.
    O3 = 0.
    O3NO2 = 0.
    Date = ""
    minute = 0
    second = 0

    def __init__(self, co, no, no2, o3, o3no2, date, minute, second):
        self.CO = co
        self.NO = no
        self.NO2 = no2
        self.O3 = o3
        self.O3NO2 = o3no2
        self.Date = date
        self.minute = minute
        self.second = second


class SystemValues:  # example -> [c1, c2, c3, c4, c5, c6, c7, c8, c9, b]
    CO = []
    NO = []
    NO2 = []
    O3 = []
    O3NO2 = []

    def __init__(self, co, no, no2, o3, o3no2):
        self.CO = co
        self.NO = no
        self.NO2 = no2
        self.O3 = o3
        self.O3NO2 = o3no2


class Solutions:
    def __init__(self):
        self.CO = []
        self.NO = []
        self.NO2 = []
        self.O3 = []
        self.O3NO2 = []



