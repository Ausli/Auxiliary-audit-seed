import sys
#https://lemonhd.org/details_movie.php?id=26063
import requests
from pyhtml.headersdata import headersdata
import re
import time

def get_response(url):
    try:
        response = requests.get(url, headers=headersdata(), timeout=8)
        if response.status_code == (200 or 304) and response != 'None':
            return response
        else:
            raise ValueError
    except:
            try:
                response = requests.get(url, headers=headersdata(), timeout=15,)
                if response.status_code == (200 or 304) and response != 'None':
                    return response
            except:
                print ('response重新连接')
                time.sleep (2)
                response = requests.get (url, headers=headersdata (), timeout=15)
                if response.status_code == (200 or 304) and response != 'None':
                    return response



if __name__ == '__main__':
    url = 'https://lemonhd.org/details_movie.php?id=26079'
    print(get_response (url).text)
    print(get_response (url))