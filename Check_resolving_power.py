import re
def check_resolving_power_All(resolving_power,info,medium,route,title,soup):
    def check_resolving_power_feedback():
        info2=re.sub('SOURCE.*','',info,re.I)
        resolving_power_type = re.search('1080i', info2)
        resolving_power_type_1 = re.search(resolving_power, route.text)
        resolving_power_type_3 = re.search('1080i', title)
        resolving_power_type6 = re.search('3840.*2160', info)
        resolving_power_type7 = re.search('3 840', info2)
        resolving_power_type7_1 = re.search('4096 x 2160', info)
        resolving_power_type3 = re.search('1920 x 1080', info)
        resolving_power_type4 = re.search('1 920', info2)
        resolving_power_type4_1 = re.search('1 080', info2)
        #resolving_power_type4_2 = re.search('1080p', info2)
        if resolving_power_type3 :
            return ' 应为2K/1080p'
        if resolving_power_type4 and resolving_power_type4_1:
            return ' 应为2K/1080p'
        if resolving_power_type7 or resolving_power_type7_1 or resolving_power_type6:
            return ' 应为4K/2160p'
        if resolving_power_type and resolving_power_type_3:
            return ' 应为1080i'
        if resolving_power_type_3 and resolving_power_type_1:
            return ' 应为1080i'

    def check_resolving_power():
        if resolving_power=='720p/i':
            resolving_power8=re.search('720.*pixels',info)
            resolving_power8_1=re.search('1280 x 720',info)
            resolving_power8_2=re.search('720像素',info)
            resolving_power8_3=re.search('1280x536',info)
            resolving_power8_4=re.search('1280x720',info)
            if resolving_power8 or resolving_power8_1 or resolving_power8_2 \
                    or resolving_power8_3 or resolving_power8_4:
                return True
        if resolving_power =='1080i':
            resolving_power_type=re.search(resolving_power,info)
            resolving_power_type_1=re.search(resolving_power,route.text)
            resolving_power_type_3=re.search(resolving_power,title)
            resolving_power_type_4=re.search('Interleaved',info)
            resolving_power_type_2=re.search('1 920',info)
            resolving_power_type_5=re.search('1 080',info)
            if resolving_power_type_4 and resolving_power_type_2 and resolving_power_type_5:
                return True
            if resolving_power_type_1 and resolving_power_type_3:
                return True
            if resolving_power_type and resolving_power_type_3:
                return True
            if resolving_power_type and resolving_power_type_1:
                return True


        if resolving_power=='4K/2160p' and medium=='UHD Blu-ray':
            resolving_power_type2=re.search('2160p',info)
            if resolving_power_type2:
                return True
        if resolving_power=='4K/2160p':
            resolving_power_type6=re.search('3840.*2160',info)
            resolving_power_type7=re.search('3 840',info)
            resolving_power_type7_1=re.search('4096 x 2160',info)
            resolving_power_type7_2=re.search('Video.*2160p',info)
            if resolving_power_type7 or resolving_power_type7_1 \
                or resolving_power_type6 or resolving_power_type7_2:
                return True
        if resolving_power=='2K/1080p':
            resolving_power_type3=re.search('1920.*1080',info)
            resolving_power_type4=re.search('1 920',info)
            resolving_power_type4_1=re.search('1 080',info)
            resolving_power_type4_2=re.search('1080p',info)
            if resolving_power_type3 or resolving_power_type4_2:
                return True
            if resolving_power_type4 and resolving_power_type4_1:
                return True
    def check_resolving_power_answer():
        if check_resolving_power() is True:
            return '分辨率'+resolving_power+'正确'
        else:
            resolving_power_check=check_resolving_power_feedback()
            if resolving_power_check:
                return '分辨率' + resolving_power + '错误'+resolving_power_check
            else:
                return '分辨率' + resolving_power + '错误'
    return check_resolving_power_answer()