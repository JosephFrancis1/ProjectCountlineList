#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import sys

file = sys.argv[1]
sensors = pd.read_csv(file)

sensors[['latlong','longitude']] = sensors['latlong'].str.split(',',expand=True)   #splits column into 2 via delimiter

sensors = sensors.sort_values(by='deviceid',ascending=True)                             #sorts sensors in ascending order

sensors = sensors.drop(['projectid','deleted','deviceid','deviceuid','direction','junctionid','latlongend','latlongstart','nextjunctionid'],1)

sensors.columns = ['id', 'name', 'latitude', 'longitude']
sensors = sensors[['name', 'id', 'latitude', 'longitude']]

sensors['latitude'] = sensors['latitude'].str[1:]                              #splits entire column of strings
sensors['longitude'] = sensors['longitude'].str[:-1]

print(sensors)

sensors.to_csv(file, index=False)                                               #Overwrites csv enterted in command


