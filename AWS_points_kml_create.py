#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:55:10 2020

@author: Jason Box, GEUS.dk

"""
import os
import pandas as pd
import simplekml

#%%
fn='./input_data/PROMICE_info_from_GPS_data_2017-2018.csv'
df = pd.read_csv(fn,sep='\t')

n_sites=len(df.name)
opath='./kml/PROMICE/'

for k in range(0,n_sites):
    print(k,df.name[k],df.lon[k],df.lat[k],df.elev[k])
    kml = simplekml.Kml()
    pnt = kml.newpoint(name=df.name[k])
    pnt.coords = [(df.lon[k],df.lat[k])]
    pnt.style.labelstyle.color = simplekml.Color.blue  # Make the text red
    pnt.style.labelstyle.scale = 1.5  # text scaling multiplier
    pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
    pnt.altitudemode = simplekml.AltitudeMode.relativetoground
    pnt.camera.latitude=df.lat[k]
    pnt.camera.longitude=df.lon[k]
    pnt.camera.altitude=4e5
    pnt.camera.tilt = 0
    ofile=opath+str(df.name[k]).lstrip()+'.kml'
    kml.save(ofile)
    
#%%
fn='/Users/jason/Dropbox/AWS/GCN_PROMICE_kml/input_data/GCN info ca.2000.csv'
df = pd.read_csv(fn)

n_sites=len(df.name)
opath='./kml/GCN/'

for k in range(0,n_sites):
    print(k,df.name[k],df.lon[k],df.lat[k],df.elev[k])
    kml = simplekml.Kml()
    pnt = kml.newpoint(name=df.name[k])
    pnt.coords = [(df.lon[k],df.lat[k],df.elev[k])]
    pnt.style.labelstyle.color = simplekml.Color.cyan  # Make the text red
    pnt.style.labelstyle.scale = 1.5  # text scaling multiplier
    pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
    pnt.altitudemode = simplekml.AltitudeMode.relativetoground
    pnt.camera.latitude=df.lat[k]
    pnt.camera.longitude=df.lon[k]
    pnt.camera.altitude=4e5
    pnt.camera.tilt = 0
    ofile=opath+str(df.nickname[k]).lstrip()+'.kml'
    kml.save(ofile)
    
