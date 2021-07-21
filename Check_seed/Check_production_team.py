import re
from bs4 import BeautifulSoup


def team_check(team_text):
    team_type = re.findall ("-(.*)", team_text.replace('-ray',''))
    if team_type:
        team_type2 = re.findall ('-(.*)', team_type[0])
        if team_type2:
            return team_type2[0]
        elif team_type:
            return team_type[0]
        else:
            pass
def title_team_check(route):
    soup2 = BeautifulSoup (route.text, 'lxml')
    team = soup2.select ('.rowfollow')
    teamdata = set()
    for i in team:
        i = i.text
        team_data2=team_check(i)
        if team_data2:
            teamdata.add(team_data2)
    return teamdata
def Blu_ray_team_check(teamdata,info):
    Bluray_check=re.search('Title.*|name.*',info)
    if Bluray_check:
        Bluray_check_isTure=re.search(str(teamdata),Bluray_check.group())
        if Bluray_check_isTure is None:
            return '原盘无制作组'
        else:
            return '制作组检查无误为' + str(teamdata)


def team_processing(route, medium, title,info):
    title_team = team_check(title)
    teamdata=title_team_check(route)
    if medium == 'Blu-ray' or medium == 'UHD Blu-ray' :
        #return Blu_ray_team_check(teamdata,info)
        return '原盘跳过制作组检查'
    if len(teamdata) == 0 and title_team == None:
        return '没有制作组'
    if len(teamdata) == 0:
        return '文件名未标明制作组'
    teamdata = list(teamdata)
    team_data = teamdata[0].replace('.mkv', '').replace('.mp4', '').replace('.ts', '')
    item = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", team_data)
    item2 = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", str(title_team))
    team_retiele = re.search(item, item2)
    team_retiele_1 = re.search (item2, item)
    if team_retiele or team_retiele_1:
        if len(title_team)>len(team_data):
            return  '制作组检查无误为' +team_data
        else:
            return '制作组检查无误为' + title_team
    elif title_team and teamdata:
        return '匹配制作组失败'+'team_data:' + team_data+"==="+ 'title_team:' + title_team
    else:
        return '无制作组'