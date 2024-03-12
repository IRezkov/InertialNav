import pandas as pd

location = pd.read_csv('Location.csv')
gyroscope = pd.read_csv('GyroscopeUncalibrated.csv')
magnetometer = pd.read_csv('MagnetometerUncalibrated.csv')
barometer = pd.read_csv('Barometer.csv')
orientation = pd.read_csv('Orientation.csv')
accelerometer = pd.read_csv('AccelerometerUncalibrated.csv')

datas = [location, gyroscope, magnetometer, barometer, orientation, accelerometer]
fst_time = []
for i in datas:
    count = 0
    for j in i['seconds_elapsed']:
        if j >= 1.310549:
            fst_time.append(count)
            break
        else:
            count += 1

print(fst_time)
