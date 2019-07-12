# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#
#from simple_salesforce import Salesforce

#from collections import namedtuple

#credential = namedtuple('credential', "username password token")
#cred = credential(username= "glenn.abastillas@gmail.com",
#password = "^-aM)e}TPP8kB#3DYyzJ",
#token = "SLtuFzh1N5GiSHysLJuPyRhJ")
#
#import pickle
#
#with open('key.pkl', 'wb') as fout:
#    pickle.dump(cred, fout)

#sf = Salesforce(username=username, 
#                password=password, 
#                security_token=token)
#
#description = sf.describe()
#contacts = sf.Contact.describe()
#sobjects = description['sobjects']
#
#sobjects_names = [__['name'] for __ in sobjects]
#


#%% GeoPy Coordinates

from geopy import Point
from geopy.geocoders import Nominatim
import geopandas as gp

