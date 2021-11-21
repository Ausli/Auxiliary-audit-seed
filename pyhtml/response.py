import sys
#https://lemonhd.org/details_movie.php?id=26063
import httpx
from pyhtml.headersdata import headersdata
import re
import time

def get_response(url):
    try:
        response = httpx.get(url, headers=headersdata(),timeout=3)
        if response.status_code == (200 or 304) and response != 'None':
            return response
        else:
            raise ValueError
    except:

        response = httpx.get(url, headers=headersdata(), timeout=15,)
        if response.status_code == (200 or 304) and response != 'None':
            return response
        else:
            raise ValueError




if __name__ == '__main__':
    url = 'https://lemonhd.org/details_movie.php?id=26079'
    s=time.time()
    get_response (url)
    f=time.time()
    print(f-s)