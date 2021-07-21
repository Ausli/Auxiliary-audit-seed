import requests
from requests.packages import urllib3
urllib3.disable_warnings()
def img_check(soup,imgheaders):
    imgcheck=soup.select('#kdescr img')
    o=0
    p=0
    n=0
    all=len (imgcheck)
    if all<3:
        return '缺少图片'
    for i in imgcheck:
        try:
            response2 = requests.get (i['src'], headers=imgheaders, verify=False, timeout=1)
            if response2.status_code==(200 or 304):
                p=p+1
            else:
                n=n+1
        except requests.exceptions.ReadTimeout:
            o=o+1
    return '图片通过'+str(p)+'张','图片不通过'+str(n+o)+'张'