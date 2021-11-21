import requests
from pyhtml.headersdata import imgheaders
'''from requests.packages import urllib3
urllib3.disable_warnings()'''
def img_check(img_url):
    o=0
    p=0
    n=0
    for i in img_url:
        try:
            response2 = requests.get (i, headers=imgheaders, timeout=3)
            if response2.status_code==(200 or 304):
                p=p+1
            else:
                n=n+1
        except requests.exceptions.ReadTimeout:
            o=o+1
    return '图片通过'+str(p)+'张','图片不通过'+str(n+o)+'张','共'+str(len(img_url))+'张'