import httpx
import time
import re
import sys
from .headersdata import headersdata
def proxy():
    import random
    import linecache
    # 打开代理
    proxies_location = 'D:\workarea\Tools\ippool\lemon_ip.txt'
    count = len (open (proxies_location, 'r').readlines ())
    ram = random.randrange (1, count)
    ff = linecache.getline (proxies_location, ram)
    ff = ff.strip ().split (':', 1)
    list1 = [ff[0]]
    list2 = [ff[1]]
    proxies = dict (zip (list1, list2))
    return proxies
def get_route(url_id):
    try:
        route = httpx.get('https://lemonhd.org/viewfilelist.php?id=' + url_id, headers=headersdata(), timeout=8)
        if route.status_code==(200 or 304)and route != 'None':
            return route
        else:
            raise ValueError
    except:
            time.sleep (2)
            print('route重新连接')
            route = httpx.get('https://lemonhd.org/viewfilelist.php?id=' + url_id,headers=headersdata(), timeout=12)
            if route.status_code == (200 or 304)and  route != 'None':
                return route
            else:
                raise ValueError


