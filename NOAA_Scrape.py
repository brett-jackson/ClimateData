# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 22:18:02 2020
Class for handling requests to NOAA API v1
@author: Brett
"""
import requests

class NOAAv1:
    def __init__(self,token):
        self.data   = 'https://www.ncei.noaa.gov/access/services/data/v1?'
        self.dataSearch = 'https://www.ncei.noaa.gov/access/services/search/v1/data?'
        self.datasetSearch = 'https://www.ncei.noaa.gov/access/services/search/v1/dataset?'
        self.token = token
    def dataRequest(self,params):
        #Example: https://www.ncei.noaa.gov/access/services/data/v1?dataset=global-marine&dataTypes=WIND_DIR,WIND_SPEED&stations=AUCE&startDate=2016-01-01&endDate=2016-01-02&boundingBox=90,-180,-90,180
        params = {key: val for key, val in params.items() if val is not '' and val is not None}
        URL = self.data
        return requests.get(URL,headers={'token':self.token}, params=params)
    
    def dataSearchRequest(self,params):
        #Example: https://www.ncei.noaa.gov/access/services/search/v1/data?dataset=global-hourly&startDate=2016-01-01T00:00:00&endDate=2017-12-31T23:59:59&dataTypes=TMP&limit=10&offset=90
        params = {key: val for key, val in params.items() if val is not '' and val is not None}
        URL = self.dataSearch
        return requests.get(URL,headers={'token':self.token}, params=params)
    
    def datasetSearchRequest(self,params):
        params = {key: val for key, val in params.items() if val is not '' and val is not None}
        URL = self.datasetSearch
        return requests.get(URL,headers={'token':self.token}, params=params)
    
class NOAAv2:
    def __init__(self,token):
        self.base = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
        self.token = token
    def request(self,params,receive,ID=None):
        params = {key: val for key, val in params.items() if val is not '' and val is not None}
        URL = self.base+receive
        if ID:
            URL += '/' + ID
        return requests.get(URL,headers={'token':self.token}, params=params)
        
if __name__ == '__main__':
    token = ''
    with open('token.txt') as f:
        token = f.read()  
    print("Token: " + token)
    query = NOAAv2(token)
    
    print("\n***\n*** DEFAULT 25 DATASETS\n***")
    datasetParams = {'datatypeid':'',
                  'locationid':'',
                  'stationid':'',
                  'startdate':'',
                  'enddate':'',
                  'sortfield':'',
                  'sortorder':'',
                  'limit':'',
                  'offset':''}
    response = query.request(datasetParams,'datasets')
    print(response.text)
    
    print("\n***\n*** DEFAULT 25 CATEGORIES\n***")
    categoriesParams = {'datasetid':'',
                  'locationid':'',
                  'stationid':'',
                  'startdate':'',
                  'enddate':'',
                  'sortfield':'',
                  'sortorder':'',
                  'limit':'',
                  'offset':''}
    response2 = query.request(categoriesParams,'datacategories')
    print(response2.text)
    
    print("\n***\n*** DEFAULT 25 TYPES\n***")
    typesParams = {'datasetid':'',
                  'locationid':'',
                  'stationid':'',
                  'datacategoryid':'',
                  'startdate':'',
                  'enddate':'',
                  'sortfield':'',
                  'sortorder':'',
                  'limit':'',
                  'offset':''}
    response3 = query.request(typesParams,'datatypes')
    print(response3.text)
    
    print("\n***\n*** DEFAULT 25 LOCATION CATEGORIES\n***")
    loccatParams = {'datasetid':'',
                  'startdate':'',
                  'enddate':'',
                  'sortfield':'',
                  'sortorder':'',
                  'limit':'',
                  'offset':''}
    response4 = query.request(loccatParams,'locationcategories')
    print(response4.text)
    
    print("\n***\n*** DEFAULT 25 LOCATIONS\n***")
    locParams = {'datasetid':'',
                    'locationcategoryid':'',
                    'datacategoryid':'',
                    'startdate':'',
                    'enddate':'',
                    'sortfield':'',
                    'sortorder':'',
                    'limit':'',
                    'offset':''}
    response5 = query.request(locParams,'locations')
    print(response5.text)
    
    print("\n***\n*** DEFAULT 25 STATIONS\n***")
    stationParams = {'datasetid':'',
                    'locationid':'',
                    'datacategoryid':'',
                    'datatypeid':'',
                    'extent':'',
                    'startdate':'',
                    'enddate':'',
                    'sortfield':'',
                    'sortorder':'',
                    'limit':'',
                    'offset':''}
    response6 = query.request(stationParams,'stations')
    print(response6.text)
    
    print("\n***\n*** DEFAULT 25 DATAPOINT EXAMPLE\n***")
    dataParams = {'datasetid':'GSOM',
                    'datatypeid':'',
                    'locationid':'',
                    'stationid':'',
                    'startdate':'2005-10-03',
                    'enddate':'2012-09-10',
                    'units':'',
                    'sortfield':'',
                    'sortorder':'',
                    'limit':'',
                    'offset':'',
                    'includemetadata':''}
    response7 = query.request(dataParams,'data')
    print(response7.text)
    
    
    
