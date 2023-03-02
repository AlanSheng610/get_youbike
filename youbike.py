import  json, ssl, urllib.request
import requests

url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
context = ssl._create_unverified_context()

with urllib.request.urlopen(url, context=context) as jsondata:
    response = requests.get(url)
    #將JSON進行UTF-8的BOM解碼，並把解碼後的資料載入JSON陣列中
    if response.status_code == 200:
        data = json.loads(jsondata.read().decode('utf-8-sig')) 
    else :
        print('error')
name = '臺大男'

for i in data:
      if i['sna'].find(name)>=0:
        print(i['sna'],'\t',i['sbi'],'\t',i['bemp'])


# class getbike():
#     def __init__(self) :
#         self.url ='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
#         self.name = '臺大男'
#         self.context = ssl._create_unverified_context()
      
#         self._station = []
#         self._barrow = []
#         self._return = []
#         self.information = []
#         with urllib.request.urlopen(self.url, context=self.context) as jsondata:
#     #將JSON進行UTF-8的BOM解碼，並把解碼後的資料載入JSON陣列中
#             self.data = json.loads(jsondata.read()) 
#     def getnum(self) :
#         for i in self.data:
#             if i['sna'].find(self.name)>=0:
#                 print(i['sna'],'\t',i['sbi'],'\t',i['bemp'])
#                       # self._station.append(i['sna'])
#                 self._barrow.append(i['sbi'])
#                 self._return.append(i['bemp'])
#             # self.information = list[self._barrow, self._return ]
#         return  self._barrow



# a = getbike()
# b = a.getnum()
# print(b)
# t1 = '男一舍前：' + str(b[1])
# t2 = '男六舍前：' + str(b[2])
# t3 = '男八舍東側：' + str(b[3])
# t4 = '男七舍前：' + str(b[0])
# print(t1)
# print(t2)
# print(t3)
# print(t4)



    