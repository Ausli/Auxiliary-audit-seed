url='https://lemonhd.org/details_movie.php?id=192363&action=check'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4346.0 Safari/537.36 Edg/89.0.731.0',
    'referer': 'https://lemonhd.org/details_movie.php?id=194625',
    'origin': 'https://lemonhd.org',
'authority': 'lemonhd.org',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1'
}
import os
if os.path.exists('app/cookie.txt'):
    headers['cookie']=open('app/cookie.txt').read()
import requests
requestdata={"check_type":"fail","check_remark":'info错误'}
session=requests.session()
response=session.post(url,headers=headers,data=requestdata)
print(response.headers)

#https://lemonhd.org/details_movie.php?id=194625&action=check