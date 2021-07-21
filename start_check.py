from bs4 import BeautifulSoup
import requests
import re
import os
import time
import sys
from lxml import etree
from Main_function import Principal_function
from MyThread import MyThread
from Check_seed import email_jimi
from pyhtml import *
import threading
def cookie_test():
    if not os.path.exists ('cookie.txt'):
        return False
def get_html_data(url,url_id):
    get_url = MyThread (get_response, (url,))
    get_url2 = MyThread (get_route, (url_id,))
    get_url.start (), get_url2.start ()
    get_url.join (), get_url2.join ()
    response = get_url.get_result ()
    route = get_url2.get_result ()
    return response,route
def start_process(url):
    if cookie_test() == False:
        sys.exit('无cookie')
    url_id = re.search('\d+', url).group()
    response = get_response(url)
    route = get_route(url_id)
    soup = BeautifulSoup(response.text,'html.parser')
    titlemail = soup.select ('.__cf_email__ ', )
    subtitle = re.findall('副标题</td><td class="rowfollow" valign="top" align="left">(.*)</td></tr>', response.text)[0]
    url_type_tv = re.search ('details_tv', url)
    url_type_movie=re.search('details_movie',url)
    messagerow = [x.replace('&nbsp;','').strip() for x in re.findall ('媒介<.b>:(.*)<b>编码<.b>:(.*)<b>分辨率<.b>:(.*)<b>音频编码<.b>:(.*)<b>地区<.b>:(.*)<b>制作组<.b>:(.*)<b>版本<.b>:(.*)<.td>', response.text)[0]]
    Complete=''
    email = email_jimi(titlemail[0].attrs['data-cfemail']) if titlemail else None
    subtitle = re.sub('<a.*</a>', email, subtitle) if titlemail else subtitle
    if url_type_tv:
        movie_message_tv = re.findall('类型</b>: (.*)&nbsp', response.text)
        movie_type = movie_message_tv[0].strip('&nbsp;')
        Complete=re.search('是否完结</b>：(.*)</td>',response.text)
    elif url_type_movie:
        messagerow = re.findall('媒介<.b>: (.*)&nbsp;&nbsp;&nbsp;<b>'
                                '编码</b>: (.*)&nbsp;&nbsp;&nbsp;<b>音频编码</b>: (.*)&nbsp;'
                                '&nbsp;&nbsp;<b>分辨率</b>: (.*)&nbsp;&nbsp;&nbsp;<b>地区'
                                '</b>: (.*)&nbsp;&nbsp;&nbsp;<b>制作组</b>: (.*)&nbsp;&nbsp;&nbsp;<b>版本</b>: (.*)</td>', response.text)
        movie_message = re.findall ('类型</b>:.(.*)</td>', response.text)
        movie_type = movie_message[0]
    else:
        movie_message = re.findall('类型</b>:.(.*)</td>', response.text)
        movie_type = movie_message[0]
    return Principal_function (messagerow, soup, route, subtitle, response, movie_type, Complete)


if __name__ == '__main__':
    start = time.time ()
    url = 'https://lemonhd.org/details_doc.php?id=240549&group_id=35290632'
    proess = start_process (url)
    for o in proess:
        print(o)
    end = time.time ()
    print (end - start)