import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

url = 'https://tianqi.2345.com/Pc/GetHistory'
headers = {
# ':authority': 'tianqi.2345.com',
# ':method':'GET',
# ':path' : """/Pc/GetHistory?areaInfo%5BareaId%5D=54511&areaInfo%5BareaType%5D=2&date%5Byear%5D=2011&date%5Bmonth%5D=3""",
# ':scheme':"https",
'accept': "application/json, text/javascript, */*; q=0.01",
'accept-encoding': "gzip, deflate, br, zstd",
'accept-language':"zh-CN,zh;q=0.9",
'cache-control':"no-cache",
'cookie':"lc2=59278; lc=59278; wc=71161; wc_n=%25u9AD8%25u8981%25u533A; Hm_lvt_a3f2879f6b3620a363bec646b7a8bcdd=1743324325; HMACCOUNT=B0B99500DF2DE7EC; BAIDU_SSP_lcr=https://www.baidu.com/link?url=xPJrUpZubKf0HstmfbVcA1RbP5kTAkwZ3dmqbg7wCOCf-GXgk3gGzWoM6IaQ0by6&wd=&eqid=c77932570086e7430000000667e90789; lastCountyId=54511; lastCountyPinyin=beijing; lastProvinceId=12; lastCityId=54511; lastCountyTime=1743328558; Hm_lpvt_a3f2879f6b3620a363bec646b7a8bcdd=1743328558",
'pragma':  "no-cache",
'priority':"u=1, i",
'referer':"https://tianqi.2345.com/wea_history/54511.htm",
'sec-ch-ua':""""Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134""""",
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
'x-requested-with':'XMLHttpRequest'
}
def tool(year,month):
    params = {'areaInfo[areaId]': 54511,
              'areaInfo[areaType]': 2,
              'date[year]': year,
              'date[month]': month}
    r = requests.get(url, headers=headers, params=params)
    print('现在网页的状态代码是：',r.status_code)
    with open('data11.json','w') as f1:
        f1.write(r.text)
    with open('data11.json','r') as f2:
        data = json.load(f2)
        data1 = str(data)
        p = open('the_real_data.text','w')
        p.write(data1)
        p.close()
        soup = BeautifulSoup(data1,'html.parser')
        # oo = soup.find('ul',class_='history-msg')
        oo1 = soup.find('li').get_text()
        oo1 = soup.find('em',class_='orange-txt').get_text()
        print(oo1)
    # print(r.text)
    # data = r.json()['data']
    # df = pd.read_html(data)[0]
    # print(df.head())
tool(2025,3)