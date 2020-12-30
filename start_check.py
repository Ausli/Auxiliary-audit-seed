from bs4 import BeautifulSoup
import requests
import re
import os
import time
import sys
from Check_medium import  medium_check_All
from Check_code import  check_code_All
from Check_region import check_region_all
from Check_movie_type import movie_type_check_All
from Check_img import img_check
from Check_Audio_coding import check_Audio_coding_All
from Check_resolving_power import  check_resolving_power_All
from Check_production_team import team_processing
from Check_link_and_Get_info import vidioparme,link_check
from Check_Get_title import title_get,title_check
from email_decode import email_jimi
from Check_tag import tag_check

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4346.0 Safari/537.36 Edg/89.0.731.0',
    'Referer': 'https://lemonhd.org/torrents.php',
    'authority': 'lemonhd.org'
}
if os.path.exists('cookie.txt'):
    headers['cookie']=open('cookie.txt').read()
else:
    sys.exit('无cookie')
route_headers = headers
imgheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4277.0 Safari/537.36 Edg/87.0.658.0',
    'Host': 'img1.doubanio.com'}


def start_process(url):
    session = requests.Session()
    try:
        response = session.get(url, headers=headers, timeout=8)
    except:
        time.sleep(2)
        response = session.get(url, headers=headers, timeout=8)

    route_headers['Referer'] = response.url
    url_id = re.search('\d+', response.url).group()
    route = session.get('https://lemonhd.org/viewfilelist.php?id=' + url_id, headers=route_headers)
    soup = BeautifulSoup(response.text, 'lxml')
    titlemail = soup.select('.__cf_email__ ', )
    subtitle = re.findall('副标题</td><td class="rowfollow" valign="top" align="left">(.*)</td></tr>', response.text)[0]
    if titlemail:
        email = email_jimi(titlemail[0].attrs['data-cfemail'])
        subtitle = re.sub('<a.*</a>',email,subtitle)
    movie_message=re.findall('类型:</b>&nbsp;(.*)</td></tr>',response.text)
    message = re.findall('媒介:&nbsp;</b>(.*)&nbsp;&nbsp;&nbsp;<b>编码:&nbsp;</b>(.*)&nbsp;&nbsp;&nbsp;'
                         '<b>音频编码:&nbsp;</b>(.*)&nbsp;&nbsp;&nbsp;<b>分辨率:&nbsp;</b>(.*)&nbsp;&nbsp;&nbsp;'
                         '<b>地区:</b>(.*)&nbsp;&nbsp;&nbsp;<b>制作组:&nbsp;</b>(.*)</td></tr>', response.text)

    message = message[0]
    medium = message[0]
    code = message[1]
    Audio_coding = message[2]
    resolving_power = message[3]
    region = message[4]
    Production_team = message[5]
    info = str(vidioparme(soup))
    title = title_get(soup)
    title_check_ans=title_check(title)
    medium_check=medium_check_All(route, medium, info, title, soup)
    check_code=check_code_All(code, info, medium, route,title)
    check_Audio_coding=check_Audio_coding_All(Audio_coding, info,Production_team,title)
    check_resolving_power=check_resolving_power_All(resolving_power, info, medium, route, title, soup)
    check_region=check_region_all(soup, region)
    check_team=team_processing(route, medium, title)
    check_tag=tag_check(title, session,medium,subtitle,info,Production_team)
    check_link=link_check(soup, response)
    #img_check(soup, imgheaders)
    session.close()
    movie_type_false='类型获取失败'
    if title_check_ans:
        title=title+title_check_ans
    if movie_message:
        movie_type = movie_message[0]
        movie_type_check = movie_type_check_All(movie_type,medium,resolving_power,title)
        return title,subtitle,movie_type_check,message,medium_check,check_code,check_Audio_coding,\
               check_resolving_power,check_region,check_team,check_tag,check_link
    else:
        return title,subtitle,movie_type_false,message,medium_check,check_code,check_Audio_coding,\
               check_resolving_power,check_region,check_team,check_tag, check_link

if __name__ == '__main__':
    url = 'https://lemonhd.org/details_doc.php?id=196955'
    start = time.time()
    proess = start_process(url)
    end = time.time()
    print(end - start)
    for ii in range(len(proess)):
        print(proess[ii])
    pass_false = re.search('错误', str(proess))
    if pass_false:
        print('=============================Flase=============================')






