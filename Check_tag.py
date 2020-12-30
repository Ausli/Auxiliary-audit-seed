from bs4 import BeautifulSoup
import re
def tag_check(title, session,medium,subtitle,info,Production_team):
    title = title.replace(' ', '').replace('+','%2').strip()
    '''url2 = 'https://lemonhd.org/torrents.php?search=' + title + '&search_area=0&suggest=0'
    response2 = session.get(url2, headers=headers)
    print(response2.url)
    soup2 = BeautifulSoup(response2.text, 'lxml')'''
    soup2=BeautifulSoup('', 'lxml')
    tag_data = soup2.select('.torrentname .embedded span')
    tag = set([o.text for o in tag_data if not re.search('\d+', o.text) and not re.search('email', o.text)])
    tag_check2=re.search('爱原盘',str(tag))
    tag_check3=re.search('diy',subtitle,re.I)
    tag_check3_1=re.search('diy',str(tag),re.I)
    tag_check4=re.search('中字',str(tag))
    tag_check4_9=re.search('中字',subtitle)
    tag_check4_1=re.search('原生中字',str(tag))
    tag_check4_2=re.search('Subtitle.*Chinese',info,re.I)
    tag_check4_3=re.findall('Language.*Chinese',info,re.I)
    tag_check4_7=re.search('SUBTiTLE.*Chs',info,re.I)
    tag_check4_8=re.search('SUBTiTLE.*Cht',info,re.I)
    tag_check4_4=re.findall('语言.*中文',info)
    tag_check4_5=re.search('Simplified',info)
    tag_check4_6=re.search('Traditional',info)
    tag_check5=re.search('Audio.*Chinese',info,re.I)
    tag_check5_1=re.search('国语',str(tag))
    tag_check5_2=re.search('国语',subtitle)
    tag_check6=re.search('Presentation Graphics.*Chinese',info)
    tag_check7=re.search('Cantonese',info,re.I)
    tag_check7_1=re.search('Mandarin',info,re.I)
    tag_check8=re.search('Audio.*Chinese.*Cantonese',info,re.I)
    tag_check9=re.search('LHD',Production_team)
    tag_check9_1=re.search('League',Production_team,re.I)
    tag_feedback = []
    if tag_check4_3 or tag_check4_4:
        if tag_check4_5 and tag_check4_6:
            tag_feedback.append('中字')
        else:
            tag_feedback.append('国语或中字')
    if tag_check9 or tag_check9_1:
        tag_feedback.append('官种')
    if tag_check7:
        tag_feedback.append('粤语')
    if tag_check7_1 or tag_check5_2:
        tag_feedback.append('国语')
    if tag_check6 or tag_check4_9:
        tag_feedback.append('中字')
    if tag_check3 and not tag_check3_1 and (medium=='Blu-ray' or medium=='UHD Blu-ray'):
        tag_feedback.append('Diy')
    if (not tag_check4 and (tag_check4_2 or tag_check4_7 or tag_check4_8))and not tag_check4_1 :
        tag_feedback.append('中字')
    if tag_check5 and not  tag_check5_1 and not tag_check8:
        tag_feedback.append('国语')
    if medium=='Blu-ray' and not tag_check2 and not tag_check3:
        tag_feedback.append('爱柠檬原盘')
    if medium=='Blu-ray':
        cc=re.search('Criterion Collection',title)
        if cc:
            tag_feedback.append('Criterion')
    if len(tag_feedback)>0:
        #return 'Now:' + str(tag).replace('set()','无标签') + '  '+'Standard:' + str(set(tag_feedback))
        return  'Standard:' + str(set(tag_feedback))
    else:
        if len(tag) == 0:
            return '无标签'
        else:
            return str(tag)