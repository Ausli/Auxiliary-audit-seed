from bs4 import BeautifulSoup
import re
def tag_check(title, response,medium,subtitle,info,Production_team,Complete,region):
    subtitle=subtitle.replace('多国','')
    title = title.replace(' ', '').replace('+','%2').strip()
    soup2 = BeautifulSoup(response.text, 'lxml')
    tag_data = soup2.select('.tag')
    tag_feedback = []
    tag = set([o.text for o in tag_data if not re.search('\d+', o.text) and not re.search('email', o.text)])
    tag_feedback=tag_feedback+GuoYu_Zhongzi(tag_feedback, response, medium, subtitle, info, Production_team, Complete, region, tag)
    tag_check3=re.search('diy',subtitle,re.I)
    tag_check3_1=re.search('diy',title,re.I)
    tag_check7=re.search('Cantonese',info,re.I)
    tag_check8=re.search('Audio.*Chinese.*Cantonese',info,re.I)
    tag_check8_1=re.search('粤.*语|粤语',subtitle)
    tag_check9=re.search('LHD',Production_team)
    tag_check9_1=re.search('League',Production_team,re.I)
    tag_check10=re.search('Audio.*粤语',info,re.I)
    tag_check12=re.search('语.*言.*粤语',response.text)
    url_type_tv=re.search('tv',str(response.url))
    if region=='HK&TW(港台)'and tag_check12:
        tag_feedback.append('粤语')
    if url_type_tv:
        tag_check12=re.search('完结',str(tag))
        tag_check13_1=re.search('是否完结</b>：完结',str(Complete))
        if tag_check12 and tag_check13_1:
            tag_feedback.append('完结')
    if tag_check9 or tag_check9_1:
        tag_feedback.append('官方')
    if tag_check7 or tag_check8 or tag_check8_1:
        tag_feedback.append('粤语')
    if tag_check3  and (medium=='Blu-ray' or medium=='UHD Blu-ray'):
        tag_feedback.append('DIY')
    if tag_check3_1:
        tag_feedback.append ('DIY')
    # if (medium=='Blu-ray' or medium=='UHD Blu-ray'or medium=='DVD') and not (tag_check3 or tag_check3_1)  :
    #     tag_feedback.append('Untouched')
    if medium=='Blu-ray':
        cc=re.search('Criterion Collection',title)
        cc2=re.search('CC.*原盘',subtitle)
        ccnodiy=re.search('DIY',str(tag_feedback))
        if cc or cc2 and not ccnodiy:
            tag_feedback.append('Criterion')
    if tag_check10:
        tag_feedback.append('粤语')
    return feedback(tag_feedback,tag)

def GuoYu_Zhongzi(tag_feedback, response,medium,subtitle,info,Production_team,Complete,region,tag):
    tag_check12_1 = re.search('语.*言.*国语', response.text)
    tag_check4 = re.search('中字', str(tag))
    tag_check4_9 = re.search('SUBTiTLES.*(?=chs|cht)', info, re.I)
    tag_check4_1 = re.search('原生中字', str(tag))
    tag_check4_2 = re.search('Subtitle.*Chinese', info, re.I)
    tag_check4_3 = re.findall('Language.*Chinese', info, re.I)
    tag_check4_7 = re.search('SUBTiTLE.*Chs', info, re.I)
    tag_check4_8 = re.search('SUBTiTLE.*Cht', info, re.I)
    tag_check4_4 = re.findall('语言.*中文', info)
    tag_check4_5 = re.search('Simplified', info)
    tag_check4_6 = re.search('Traditional', info)
    tag_check5 = re.search('Audio.*Chinese', info, re.I)
    tag_check5_2 = re.search('国语|国.*语', subtitle.replace('国家', ''))
    tag_check5_3 = re.search('中字', subtitle)
    tag_check5_4 = re.search('简.*字|繁.*字', subtitle)
    tag_check6 = re.search('Presentation Graphics.*Chinese', info)
    tag_check7_1 = re.search('Mandarin', info, re.I)
    tag_check10_1 = re.search('Audio.*国语', info.replace('韩国', ''), re.I)
    tag_check11 = re.search('SUBTiTLE.*(?=简体|繁体)|Subtitle.*\s.*Chinese|Subtitle.*Chinese', info, re.I)
    tag_check11_1 = re.search('字.*幕(?=.*\s.*Chinese|.*Chinese)', info, re.I)
    tag_check14_1=re.search('语.*言.*汉语普通话',response.text)
    if tag_check6 or tag_check4_9 or tag_check11 or tag_check11_1 or tag_check5_3 or tag_check5_4 :
        tag_feedback.append('中字')
    if (not tag_check4 and (tag_check4_2 or tag_check4_7 or tag_check4_8))and not tag_check4_1 :
        tag_feedback.append('中字')
    if tag_check7_1 or tag_check5_2 or tag_check12_1:
        tag_feedback.append('国语')
    if tag_check5 or tag_check10_1 or tag_check14_1:
        tag_feedback.append('国语')
    if tag_check4_3 or tag_check4_4 and (tag_check4_5 and tag_check4_6):
            tag_feedback.append('中字')
    return tag_feedback
def feedback(tag_feedback,tag):
    if (set(tag_feedback)-tag)==set() and len(set(tag_feedback))==len(tag) and set(tag_feedback)!=set() :
        return str(tag) + '正确'''
    if len(tag_feedback)>0:
        return  '标签有待确认Now:' + str(tag).replace('set()','无标签')+'===' +'Standard:' + str(set(tag_feedback))
    if len(tag) == 0:
        return '无标签'
    return str(tag)