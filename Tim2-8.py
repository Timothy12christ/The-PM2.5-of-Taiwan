import requests
#import pprint
r=requests.get('http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json',verify=False)#verify認證不需要認證
#print(r.text)1
#pprint.pprint(r.text)
list_=r.json()#用json賴拿資料
for i in list_:
    print(i["County"],i["SiteName"],i["PM2.5"],('PM2.5值'))# 縣市  鄉鎮 PM2.5質


#print(r.status_code)
