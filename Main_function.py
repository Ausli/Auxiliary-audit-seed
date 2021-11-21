from Check_seed import *
from pyhtml.email_decode import email_jimi
from MyThread import MyThread
import re


def Principal_function(messagerow,soup,route,subtitle,response,movie_type,Complete):
    medium,code,resolving_power,Audio_coding ,region,Production_team,edition=messagerow
    info = str(vidioparme(soup))
    judge_info=''
    if info[0] ==False:
        info=info[1]
        judge_info = '===info错误，没用quote括起来'
    x_info = re.findall('data-cfemail="(.*)" href="/cdn-cgi/l/email-protection', info)
    if x_info:
        email_ = email_jimi(x_info[0])
        info = re.sub('<a class="__cf_email__".*>', email_, info)

    img_url = [i['src'] for i in soup.select('#kdescr img')]
    title = title_get(soup)
    title_check_ans = title_check(title)
    # 创建9个线程
    #task10 = MyThread(img_check, (img_url,))
    task = MyThread(medium_check_All, (route, medium, info, title, soup))
    task2 = MyThread(check_code_All, (code, info, medium, route, title))
    task3 = MyThread(check_Audio_coding_All, (Audio_coding, info, Production_team, title))
    task4 = MyThread(check_resolving_power_All, (resolving_power, info, medium))
    task5 = MyThread(check_region_all, (soup, region))
    task6 = MyThread(team_processing, (route, medium, title))
    task7 = MyThread(tag_check, (title, response, medium, subtitle, info, Production_team,Complete,region))
    task8 = MyThread(link_check, (soup, response))
    task9=MyThread(movie_type_check_All,(movie_type, medium, resolving_power, title))
    task.start(),task2.start(),task3.start(),task4.start(),task5.start(),task6.start()
    task7.start(),task8.start(),task9.start(),#task10.start()
    task.join(),task2.join(),task3.join(),task4.join(),task5.join(),task6.join()
    task7.join(),task8.join(),task9.join(),#task10.join()
    if title_check_ans:
        title = title + title_check_ans
    return title, subtitle, task9.get_result(), messagerow, task.get_result(),task2.get_result(),task3.get_result(),\
           task4.get_result(),task5.get_result(),task6.get_result(),task7.get_result(),task8.get_result()+judge_info,#task10.result






