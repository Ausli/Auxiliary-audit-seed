from fake_useragent import UserAgent
import random
import requests
import re
import time
ua=UserAgent()
def cookie_test(cookie_data):
    headers = {
        'User-Agent': ua.chrome,
        'cookie': cookie_data,
        'Referer': 'https://lemonhd.org/torrents.php',
        'authority': 'lemonhd.org'
    }
    url_list=['https://lemonhd.org/index.php','https://lemonhd.org/torrents_movie.php','https://lemonhd.org/torrents_music.php','https://lemonhd.org/torrents_doc.php']
    url=url_list[random.randint(0,len(url_list)-1)]
    response=requests.get(url,headers=headers,timeout=12)
    re_check=re.search('分享率',response.text)
    re_check2=re.search('登录',response.text)
    f = open('cookie_check.txt', 'w', encoding='utf8')
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    if re_check:
        f2 = open('cookie.txt', 'w', encoding='utf8')
        f2.write(cookie_data)
        return True
    else:
        if re_check2:
            f.write('\n网站正常==cookie错误')
        f.write('\n'+str(response.status_code))
        f.write('\n'+response.text)
        return False
