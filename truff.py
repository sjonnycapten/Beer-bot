import requests
import json
import ast
from requests.structures import CaseInsensitiveDict

class TurffConnection:

    def __init__(self):
        url = "https://panel.turff.nl/auth/auth/login"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        data = {"type":"local","email":"jankaptijn@outlook.com","password":"turff123"} 
        resp = requests.post(url,data = data)
        print(resp)
        self.beerBrands = {'Kordaat': 'la7v3lufqw','Hertog Jan' : '8ldwqfawjn','Brand Pilsener':'40mww3song','Grolsch Pils':'ylgk8kf0jh'}
        print(resp.content)
    
    def GetLogData(self):

        url = "https://panel.turff.nl/api/tablet/1dgmk0msrhfsyvl/log"

        headers = CaseInsensitiveDict()
        headers["authority"] = "panel.turff.nl"
        headers["method"] = "POST"
        headers["path"] = "/api/tablet/1dgmk0msrhfsyvl/log"
        headers["scheme"] = "https"
        headers["accept"] = "application/json, text/plain, */*"
        headers["accept-encoding"] = "gzip, deflate, br"
        headers["accept-language"] = "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7"
        headers["content-length"] = "158"
        headers["Content-Type"] = "application/json;charset=UTF-8"
        headers["cookie"] = "_hjid=ad23061e-01b5-4af0-93ee-d0271288e7f1; _ga=GA1.2.989828755.1600548388; G_ENABLED_IDPS=google; _fbp=fb.1.1610578846838.188693731; _gid=GA1.2.8993632.1610578847; _hjIncludedInPageviewSample=1; _hjTLDTest=1; _hjAbsoluteSessionInProgress=0; random_session=s%3AyxV7BLfPb-jIXX48Vr_9-XERs_HS77tZ.S7pM0Cls6o%2FlLPBOxDxryxRA7cNjfKKtvBIZv2KbMsc; _gat_gtag_UA_135468472_2=1"
        headers["origin"] = "https://panel.turff.nl"
        headers["referer"] = "https://panel.turff.nl/huis/1dgmk0msrhfsyvl/turflog"
        headers["sec-fetch-dest"] = "empty"
        headers["sec-fetch-mode"] = "cors"
        headers["sec-fetch-site"] = "same-origin"
        headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.366"

        fullRecords = []
        count = 0
        end = False
        for beer in self.beerBrands:
            #print(self.beerBrands[beer])
            end = False
            count = 0
            while not end: 

                data = '{"offset":%s,"limit":%s,"itemUID":"%s"}' % (count,100,self.beerBrands[beer])
                #data = '{"offset":%s,"limit":%s,"itemUID":"%s"}' % (count,100,'la7v3lufqw')
                print(data)
                #get data from turff api
                resp = requests.post(url, headers=headers, data=data)
                
                #format data to string
                bytes_content = resp.content
                print("1")
                string_content = bytes_content.decode("UTF-8")
                print(string_content)
                records = json.loads(string_content)
                print("3")
                
                count = count + 100
                
                for r in records:  
                    if(type(r) != dict):
                        end = True
                        break
                    fullRecords.append(r)

        return fullRecords 
