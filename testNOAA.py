# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:07:27 2020

@author: Brett
"""
from NOAA_Scrape import NOAAv2, NOAAftp
import os 
def testFTP():
    directory = NOAAftp()
    directory.downloadCO2(os.getcwd())
def testV2():
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
                    'startdate':'2012-07-03',
                    'enddate':'2012-09-10',
                    'units':'',
                    'sortfield':'',
                    'sortorder':'',
                    'limit':'',
                    'offset':'',
                    'includemetadata':''}
    response7 = query.request(dataParams,'data')
    print(response7.text)
if __name__ == '__main__':
    testFTP()
    