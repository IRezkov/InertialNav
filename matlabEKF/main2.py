import pandas as pd
import csv

fil = pd.read_csv('Barometer.csv')

BAR = {'LineNo': [], 'TimeMS': [], 'Alt': [], 'Press': [], 'Temp': [], 'CRt': []}

for tt in range(1,len(fil)):
  BAR['LineNo'].append(tt + 1)
  BAR['TimeMS'].append(fil['seconds_elapsed'][tt]*1e3)
  BAR['Alt'].append(-fil['relativeAltitude'][tt])
  BAR['Press'].append(fil['pressure'][tt]*100)
  BAR['Temp'].append(0)
  BAR['CRt'].append(0)
  
fil = pd.read_csv('GyroscopeUncalibrated.csv')
fol = pd.read_csv('AccelerometerUncalibrated.csv')

IMU = {'LineNo': [], 'TimeMS': [], 'GyrX': [], 'GyrY': [], 'GyrZ': [], 'AccX': [], 'AccY': [], 'AccZ': []}

for tt in range(len(fil) - 1):
   IMU['LineNo'].append(tt + 1)
   IMU['TimeMS'].append(fil['seconds_elapsed'][tt]*1e3)
   IMU['GyrX'].append(-fil['x'][tt])
   IMU['GyrY'].append(fil['y'][tt])
   IMU['GyrZ'].append(fil['z'][tt])
   IMU['AccX'].append(fol['x'][tt])
   IMU['AccY'].append(-fol['y'][tt])
   IMU['AccZ'].append(-fol['z'][tt])


fil = pd.read_csv('MagnetometerUncalibrated.csv')
MAG = {'LineNo': [], 'TimeMS': [], 'MagX': [], 'MagY': [], 'MagZ': [], 'OfsX': [], 'OfsY': [], 'OfsZ': [], 'MOfsX': [],
       'MOfsY': [], 'MOfsZ': []}

for tt in range(len(fil)):
    MAG['LineNo'].append(tt + 1)
    MAG['TimeMS'].append(fil['seconds_elapsed'][tt]*1e3)
    MAG['MagX'].append(-fil['x'][tt])
    MAG['MagY'].append(-fil['y'][tt])
    MAG['MagZ'].append(-fil['z'][tt])
    MAG['OfsX'].append(0)
    MAG['OfsY'].append(0)
    MAG['OfsZ'].append(0)
    MAG['MOfsX'].append(0)
    MAG['MOfsY'].append(0)
    MAG['MOfsZ'].append(0)

BAR = pd.DataFrame.from_dict(BAR)
IMU = pd.DataFrame.from_dict(IMU)
MAG = pd.DataFrame.from_dict(MAG)

BAR.to_csv('BARO.csv',index = False)
IMU.to_csv('IMU.csv',index = False)
MAG.to_csv('MAG.csv',index = False)