# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 22:18:02 2020

@author: Brett
"""
import requests
import json

class NOAA:
    def __init__(self):
        self.search = 'https://www.ncei.noaa.gov/access/services/search/v1?'
        self.data   = 'https://www.ncei.noaa.gov/access/services/data/v1?'
    def appendQuery(paramName,param,URL):
        append = paramName + '=' + param
        if URL[-1] == '?':
            URL += '?'
        else:
            URL += '&'
        URL += append
        return URL
    def dataRequest(self,dataset,stations,startDate,endDate,dataTypes,boundingBox,dataFormat,options,includeAttributes,includeStationName,includeStationLocation,units):
        URL = self.data
        if dataset:
            URL = appendQuery('dataset',dataset,URL)
        if stations:
            URL = appendQuery('stations',stations,URL)
        if startDate:
            URL = appendQuery('startDate',startDate,URL)
        if endDate:
            URL = appendQuery('endDate',endDate,URL)
        if dataTypes:
            URL = appendQuery('dataTypes',dataTypes,URL)
        if boundingBox:
            URL = appendQuery('boundingBox',boundingBox,URL)
        if dataFormat:
            URL = appendQuery('format',dataFormat,URL)
        if options:
            URL = appendQuery('options',options,URL)
        if includeAttributes:
            URL = appendQuery('includeAttributes',includeAttributes,URL)
        if includeStationName:
            URL = appendQuery('includeStationName',includeStationName,URL)
        if includeStationLocation:
            URL = appendQuery('includeStationLocation',includeStationLocation,URL)
        if units:
            URL = appendQuery('units',units,URL)
        

