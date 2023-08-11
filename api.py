import requests

import json

#"key": "90c30b41c2fd414da85191743231008",
#url= "http://api.weatherapi.com/v1/forecast.json"
class Api:
    def __init__(self,baseurl,apikey):
        self.baseurl=baseurl
        self.apikey=apikey

    def gettemp(self,city):
        url = self.baseurl+"/current.json"
        print(url)
        par={
            "key":self.apikey,
            "q":city
        }
        res=requests.get(url,par)
        data=res.json()
        temp=data["current"]["temp_c"]
        return temp
    def get_temp_after(self,city,days,hour=None):
        url = self.baseurl + "/forecast.json"
        par={
            "key": self.apikey,
            "q": city,
            "days":days,
            "hour":hour,

        }
        res =requests.get(url,par)
        data=res.json()
        temperature_c = data["forecast"]["forecastday"][days - 1]["day"]["avgtemp_c"]
        return temperature_c

    def get_lat_lon(self,city):
        url = self.baseurl + "/current.json"
        par={
            "key": self.apikey,
            "q": city,
        }
        res=requests.get(url,par)
        data=res.json()
        print(data)
        lat=data['location']['lat']
        lon=data['location']['lon']
        return lat,lon

t=Api("http://api.weatherapi.com/v1","90c30b41c2fd414da85191743231008")
t2=Api("http://api.weatherapi.com/v1","90c30b41c2fd414da85191743231008")

print(t.get_lat_lon("cairo"))






