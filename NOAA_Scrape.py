# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 22:18:02 2020
Class for handling requests to NOAA servers
@author: Brett
"""
import requests
import ftplib
import os

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
        
class NOAAftp:
    def __init__(self):
        self.base = 'aftp.cmdl.noaa.gov'
    def downloadCO2(self,savepath):
        cd =  '/data/greenhouse_gases/co2'
        ftp = ftplib.FTP(self.base)
        ftp.login()
        ftp.cwd(cd)
        self.saveAllFTP(ftp,savepath)
        ftp.quit()
        
    def saveAllFTP(self,ftp,savepath):
        if not os.path.exists(savepath):
            os.mkdir(savepath)
        files = ftp.nlst()
        for file in files:
            saveloc = os.path.join(savepath,file)        
            if len(ftp.nlst(file))==1 and file in ftp.nlst(file):
                savefile = open(saveloc,'wb')
                ftp.retrbinary('RETR '+ file, savefile.write)
                savefile.close()
            else:
                curr = ftp.pwd()
                ftp.cwd(file)
                self.saveAllFTP(ftp,saveloc)
                ftp.cwd(curr)
        
    
    
