# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 22:18:02 2020
Class for handling requests to NOAA API v1
@author: Brett
"""
import requests

class NOAA:
    def __init__(self,token):
        self.search = 'https://www.ncei.noaa.gov/access/services/search/v1?'
        self.data   = 'https://www.ncei.noaa.gov/access/services/data/v1?'
        self.token = token
    def dataRequest(self,params):
        #Example: https://www.ncei.noaa.gov/access/services/data/v1?dataset=global-marine&dataTypes=WIND_DIR,WIND_SPEED&stations=AUCE&startDate=2016-01-01&endDate=2016-01-02&boundingBox=90,-180,-90,180
        params = {key: val for key, val in params.items() if val is not '' and val is not None}
        URL = self.data
        return requests.get(URL,headers={'token':self.token}, params=params)
        
if __name__ == '__main__':
    token = ''
    with open('token.txt') as f:
        token = f.read()  
    print("Token: " + token)
    query = NOAA(token)
    params = {'dataset':'global-marine',
              'stations':'AUCE',
              'startDate':'2016-01-01',
              'endDate':'2016-01-02',
              'dataTypes':'WIND_DIR,WIND_SPEED',
              'boundingBox':'90,-180,-90,180',
              'dataFormat':'',
              'options':'',
              'includeAttributes':'',
              'includeStationName':'',
              'includeStationLocation':'',
              'units':''}
    response = query.dataRequest(params)
    print(response.text)