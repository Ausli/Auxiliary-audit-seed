
import random
import requests
import re
from pyhtml.headersdata import headersdata
import os
import time

def cookie_test(cookie_data):
    try:
        f = open ('cookie_check.txt', 'a', encoding='utf8')
        f.write (time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime ()))
        url_list=['https://lemonhd.org/index.php','https://lemonhd.org/torrents_movie.php','https://lemonhd.org/torrents_music.php','https://lemonhd.org/torrents_doc.php']
        url=url_list[random.randint(0,len(url_list)-1)]
        headers=headersdata()
        if 'cookie' not in  headersdata() :
            cookie ={'cookie': cookie_data}
            headers={**headersdata(), **cookie}
        response=requests.get(url,headers=headers,timeout=12)
        re_check=re.search('分享率',response.text)
        re_check2=re.search('登录',response.text)
        if re_check :
            if not os.path.exists('cookie.txt'):
                f2 = open ('cookie.txt','w')
                f2.write (cookie_data)
            else:
                f2 = open ('cookie.txt')
                if len(f2.read())<10:
                    f3= open ('cookie.txt','w')
                    f3.write(cookie_data)
            return True
        else:
            if re_check2:
                f.write('\n网站正常==cookie错误')
            f.write('\n'+str(response.status_code))
            f.write('\n'+response.text)
            return False
    except requests.exceptions.ReadTimeout:
            return TimeoutError
if __name__ == '__main__':
    if os.path.exists('cookie.txt'):
        print(cookie_test (open('cookie.txt').read()))


