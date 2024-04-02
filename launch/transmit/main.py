import pandas as pd


offset = 1.310549

fil = pd.read_csv('Location.csv')
with open('/home/ysan/prac/InertialNav/launch/GPS.txt', 'w') as f:
    for i in range(len(fil)):
        f.write(
            f'{(fil["seconds_elapsed"][i] - offset) * 1e3} 3. {(fil["seconds_elapsed"][i] - offset) * 1e3} 0. 0. 0. {fil["latitude"][i]} {fil["longitude"][i]} '
            f'{fil["altitude"][i]} 0. {fil["speed"][i]} {fil["bearing"][i]} 0. 0.\n')

fil = pd.read_csv('GyroscopeUncalibrated.csv')[56:]
fol = pd.read_csv('AccelerometerUncalibrated.csv')[55:]
with open('/home/ysan/prac/InertialNav/launch/IMU.txt', 'w') as f:
    for i in range(56,56+len(fil)):
        f.write(
            f'{(fil["seconds_elapsed"][i] - offset) * 1e3} {(fil["seconds_elapsed"][i] - offset) * 1e3} {-fil["x"][i]} {-fil["y"][i]}'
            f' {-fil["z"][i]} {-fol["x"][i - 1]} {-fol["y"][i - 1]} {-fol["z"][i - 1]}\n')
fil = pd.read_csv('MagnetometerUncalibrated.csv')[106:]
with open('/home/ysan/prac/InertialNav/launch/MAG.txt', 'w') as f:
    for i in range(106,106+len(fil)):
        f.write(
            f'{(fil["seconds_elapsed"][i] - offset) * 1e3} {(fil["seconds_elapsed"][i] - offset) * 1e3} {fil["x"][i]} {-fil["y"][i]}'
            f' {-fil["z"][i]} 0. 0. 0.\n')

fol = pd.read_csv('Barometer.csv')[26:]
with open('/home/ysan/prac/InertialNav/launch/NTUN.txt', 'w') as f:
    for i in range(26,26+len(fol)):
        f.write(
            f'{(fol["seconds_elapsed"][i] - offset) * 1e3} {(fol["seconds_elapsed"][i] - offset) * 1e3} 0. 0. 0. 0. 0. 0. {fol["relativeAltitude"][i]} 0.\n')

fil = pd.read_csv('Orientation.csv')[56:]
with open('/home/ysan/prac/InertialNav/launch/ATT.txt', 'w') as f:
    for i in range(56,56+len(fil)):
        f.write(
            f'{(fil["seconds_elapsed"][i] - offset) * 1e3} {(fil["seconds_elapsed"][i] - offset) * 1e3} {fil["roll"][i]*180/3.1415} {fil["pitch"][i]*180/3.1415} {fil["yaw"][i]*180/3.1415} 0. 0.\n')
