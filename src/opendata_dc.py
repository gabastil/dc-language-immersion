# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:36:09 2019

@author: abastillasgl
"""

import geopandas as gp
import requests
import json

api_base = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/"
map_type = ["Administrative_Other_Boundaries_WebMercator/MapServer",
            "Education_WebMercator/MapServer"]


api_ward = (f"{api_base}/{map_type[0]}/31/"
            f"query?where=1%3D1&"
            f"outFields=*&"
            f"geometry=&"
            f"geometryType=esriGeometryEnvelope&"
            f"inSR=4326&"
            f"spatialRel=esriSpatialRelIntersects&"
            f"outSR=4326&"
            f"f=json")

school_zone = (f"{api_base}/{map_type[1]}/{{index}}/"
               f"query?where=1%3D1&"
               f"outFields=*&"
               f"outSR=4326&"
               f"f=json")

api_elementary = school_zone.format(index=19)
api_middle = school_zone.format(index=17)
api_high = school_zone.format(index=15)

# Retrieve the dataset using the API defined above and extract the data
# it points to using json. Next extract just the geospatial data and load it
# into a GeoDataFrame.
                   
results_ward = requests.get(api_ward)
results_elem = requests.get(api_elementary)
results_midd = requests.get(api_middle)
results_high = requests.get(api_high)

if(results_ward.status_code == 200):
    ward_data = json.loads(results_ward.text)
    ward_geo = gp.GeoDataFrame(ward_data['features'])

if(results_elem.status_code == 200):
    elem_data = json.loads(results_elem.text)
    elem_geo = gp.GeoDataFrame(elem_data['features'])

if(results_midd.status_code == 200):
    midd_data = json.loads(results_midd.text)
    midd_geo = gp.GeoDataFrame(midd_data['features'])
    
if(results_high.status_code == 200):
    high_data = json.loads(results_high.text)
    high_geo = gp.GeoDataFrame(high_data['features'])