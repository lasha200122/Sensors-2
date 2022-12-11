import pandas as pd
from pandas import DataFrame
import numpy as np
import math
import matplotlib.pyplot as plt
import os

dt = []
data = []

directory1 = r"Bin"
counter1 = 0
for entry in os.scandir(directory1):
    if (counter1 == 18):
        break
    with open(entry, "rb") as f:
        while (bytes := f.read(81)):
            year = int.from_bytes(bytes[0:2], byteorder='little', signed=False)
            month = int.from_bytes(bytes[2:3], byteorder='little', signed=False)
            day = int.from_bytes(bytes[3:4], byteorder='little', signed=False)
            hour = int.from_bytes(bytes[4:5], byteorder='little', signed=False)
            minute = int.from_bytes(bytes[5:6], byteorder='little', signed=False)
            second = int.from_bytes(bytes[6:7], byteorder='little', signed=False)
            pressure = int.from_bytes(bytes[7:11], byteorder='little', signed=False)
            temperature = int.from_bytes(bytes[11:15], byteorder='little', signed=False)
            humidity = int.from_bytes(bytes[15:19], byteorder='little', signed=False)
            ADC_CH_0_CO_B4_WE = int.from_bytes(bytes[19:23], byteorder='little', signed=False)
            ADC_CH_0_CO_B4_WE = (ADC_CH_0_CO_B4_WE * 2.5) / (2 ** 31)
            ADC_CH_1_CO_B4_AUX = int.from_bytes(bytes[23:27], byteorder='little', signed=False)
            ADC_CH_1_CO_B4_AUX = (ADC_CH_1_CO_B4_AUX * 2.5) / (2 ** 31)
            ADC_CH_2_NO_B4_WE = int.from_bytes(bytes[27:31], byteorder='little', signed=False)
            ADC_CH_2_NO_B4_WE = (ADC_CH_2_NO_B4_WE * 2.5) / (2 ** 31)
            ADC_CH_3_NO_B4_AUX = int.from_bytes(bytes[31:35], byteorder='little', signed=False)
            ADC_CH_3_NO_B4_AUX = (ADC_CH_3_NO_B4_AUX * 2.5) / (2 ** 31)
            ADC_CH_4_NO2_B43F_WE = int.from_bytes(bytes[35:39], byteorder='little', signed=False)
            ADC_CH_4_NO2_B43F_WE = (ADC_CH_4_NO2_B43F_WE * 2.5) / (2 ** 31)
            ADC_CH_5_NO2_B43F_AUX = int.from_bytes(bytes[39:43], byteorder='little', signed=False)
            ADC_CH_5_NO2_B43F_AUX = (ADC_CH_5_NO2_B43F_AUX * 2.5) / (2 ** 31)
            ADC_CH_6_OX_B431_WE = int.from_bytes(bytes[43:47], byteorder='little', signed=False)
            ADC_CH_6_OX_B431_WE = (ADC_CH_6_OX_B431_WE * 2.5) / (2 ** 31)
            ADC_CH_7_OX_B431_AUX = int.from_bytes(bytes[47:51], byteorder='little', signed=False)
            ADC_CH_7_OX_B431_AUX = (ADC_CH_7_OX_B431_AUX * 2.5) / (2 ** 31)
            TLB = int.from_bytes(bytes[51:52], byteorder='little', signed=False)
            THB = int.from_bytes(bytes[52:53], byteorder='little', signed=False)
            Outside_Temperature = ((THB * 64 + TLB / 4) / 2 ** 14) * 165 - 40
            RLB = int.from_bytes(bytes[53:54], byteorder='little', signed=False)
            RHB = int.from_bytes(bytes[54:55], byteorder='little', signed=False)
            Outside_Humidity = ((RHB * 256 + RLB) / 2 ** 14) * 100
            Voltage_VCC_main = int.from_bytes(bytes[55:57], byteorder='little', signed=False)
            Voltage_VCC_main = (Voltage_VCC_main / 2 ** 12) * (22750 / 2750)
            Voltage_5V_total = int.from_bytes(bytes[57:59], byteorder='little', signed=False)
            Voltage_5V_total = (Voltage_5V_total / 2 ** 12) * (15200 / 3100)
            Voltage_5V_ISB = int.from_bytes(bytes[59:61], byteorder='little', signed=False)
            Voltage_5V_ISB = (Voltage_5V_ISB / 2 ** 12) * (15200 / 3100)
            Voltage_4V = int.from_bytes(bytes[61:63], byteorder='little', signed=False)
            Voltage_4V = (Voltage_4V / 2 ** 12) * (20100 / 5100)
            Voltage_3_3_V = int.from_bytes(bytes[63:65], byteorder='little', signed=False)
            Voltage_3_3_V = (Voltage_3_3_V / 2 ** 12) * (15750 / 4750)
            Serialnumber_uc1 = int.from_bytes(bytes[65:69], byteorder='little', signed=False)
            Serialnumber_uc2 = int.from_bytes(bytes[69:73], byteorder='little', signed=False)
            Serialnumber_uc3 = int.from_bytes(bytes[73:77], byteorder='little', signed=False)
            Serialnumber_uc4 = int.from_bytes(bytes[77:81], byteorder='little', signed=False)
            # dt=[year,month,day,hour,minute,second,pressure,temperature,humidity,ADC_CH_0_CO_B4_WE,
            #          ADC_CH_1_CO_B4_AUX,ADC_CH_2_NO_B4_WE,ADC_CH_3_NO_B4_AUX,ADC_CH_4_NO2_B43F_WE,
            #          ADC_CH_5_NO2_B43F_AUX,ADC_CH_6_OX_B431_WE,ADC_CH_7_OX_B431_AUX,TLB,THB,Outside_Temperature,RLB,RHB,
            #          Outside_Humidity,Voltage_VCC_main,Voltage_5V_total,Voltage_5V_ISB,Voltage_4V,Voltage_3_3_V,Serialnumber_uc1,
            #          Serialnumber_uc2,Serialnumber_uc3,Serialnumber_uc4]
            dt = [year, month, day, hour, minute, second, ADC_CH_0_CO_B4_WE, ADC_CH_2_NO_B4_WE, ADC_CH_4_NO2_B43F_WE, ADC_CH_6_OX_B431_WE]
            data.append(dt)
    counter1 += 1
    print(counter1)

# df= pd.DataFrame(data, columns=["year","month","day","hour","minute","second","pressure","temperature","humidity",
#                                "ADC_CH_0_CO_B4_WE","ADC_CH_1_CO_B4_AUX",
#                                "ADC_CH_2_NO_B4_WE","ADC_CH_3_NO_B4_AUX","ADC_CH_4_NO2_B43F_WE","ADC_CH_5_NO2_B43F_AUX",
#                                "ADC_CH_6_OX_B431_WE","ADC_CH_7_OX_B431_AUX","TLB","THB","Outside_Temperature","RLB","RHB","Outside_Humidity","Voltage_VCC_main",
#                                "Voltage_5V_total","Voltage_5V_ISB","Voltage_4V","Voltage_3_3_V","Serialnumber_uc1",
#                                "Serialnumber_uc2","Serialnumber_uc3","Serialnumber_uc4"])
df = pd.DataFrame(data, columns=['year', 'month', 'day', 'hour', 'minute', 'second', 'CO', 'NO', "NO2", "O3"])
df.to_csv('Alphasense_output.csv', index=False)

