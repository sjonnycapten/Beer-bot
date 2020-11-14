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
        self.beerBrands = {'Kordaat': 'la7v3lufqw','Hertog Jan' : '8ldwqfawjn','Brand Pilsener':'40mww3song'}
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
        headers["content-length"] = "148"
        headers["Content-Type"] = "application/json"
        headers["cookie"] = "_hjid=ad23061e-01b5-4af0-93ee-d0271288e7f1; _hjTLDTest=1; _ga=GA1.2.989828755.1600548388; _gid=GA1.2.389293464.1600548388; _fbp=fb.1.1600548388094.1621092380; G_ENABLED_IDPS=google; G_AUTHUSER_H=0; random_session=s%3A8Th6eoPluhUo5za7quEgWNhI56FWNVPg.PBs5HOHUVEj%2Fvl4i56QVAAl%2FxJhPXX5edAZGBlsGJ8Y; _hjAbsoluteSessionInProgress=1; _hjIncludedInPageviewSample=1; _gat_gtag_UA_135468472_2=1"
        headers["origin"] = "https://panel.turff.nl"
        headers["referer"] = "https://panel.turff.nl/huis/1dgmk0msrhfsyvl/turflog"
        headers["sec-fetch-dest"] = "empty"
        headers["sec-fetch-mode"] = "cors"
        headers["sec-fetch-site"] = "same-origin"
        headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"

        fullRecords = []
        count = 0
        end = False
        for beer in self.beerBrands:
            #print(self.beerBrands[beer])
            end = False
            count = 0
            while not end: 

                data = '{"offset":%s,"limit":%s,"itemUID":"%s"}' % (count,25,self.beerBrands[beer])
                print(data)
                resp = requests.post(url, headers=headers, data=data)
                bytes_content = resp.content
                string_content = bytes_content.decode("UTF-8")
                records = json.loads(string_content)
                count = count + 25
                
                for r in records:  
                    if(type(r) is str):
                        end = True
                        #print(end)
                        break
                    #print(r)
                    fullRecords.append(r)

        return fullRecords 
