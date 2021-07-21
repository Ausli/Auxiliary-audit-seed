def check_Audio_coding_All(Audio_coding,info,Production_team,title):
    import re
    official_team=re.search('League',Production_team,re.I)
    def check_Audio_coding_feedback():
        Audio_check_1 = re.search('Dolby Digital Audio', info)
        Audio_check = re.search('AC-3', info)
        Audio_check2 = re.search('DTS-HD Master Audio', info)
        Audio_check2_1=re.search('MA',title,re.I)
        Audio_check3 = re.search('Atmos', info)
        Audio_check3_1=re.search('AUDIO.*TrueHD',info,re.I)
        Audio_check4 = re.search('Format.*AAC', info)
        Audio_check4_1=re.search('Audio.*AAC',info)
        Audio_check6 = re.search('Format.*DTS', info)
        Audio_check6_1 = re.search('音.*频.*DTS', info)
        Audio_check6_2 = re.search('文件格式.*DTS', info)
        Audio_check_2 = re.search('DD+', info)
        Audio_check_title=re.search('DD',title)
        Audio_check_title_1=re.search('AC3',title)
        Audio_check_title2=re.search('TrueHD',title)
        if (Audio_check or Audio_check_1 or Audio_check_2) and (Audio_check_title or Audio_check_title_1):
            return ' 应为DD/DD+/AC3'
        if Audio_check2 and Audio_check2_1:
            return ' 应为DTS-HD MA'
        if Audio_check3 and Audio_check_title2:
            return  ' 应为TrueHD Atmos'
        if Audio_check3_1 and not Audio_check3:
            return ' 应为TrueHD'
        if Audio_check4 or Audio_check4_1:
            return  ' 应为AAC'
        if Audio_check6 or Audio_check6_1 or Audio_check6_2:
            return  ' 应为DTS'
    def check_Audio_coding():
        if Audio_coding=='DD/DD+/AC3':
            Audio_check=re.search('DD+',info)
            Audio_check_2=re.search('Dolby Digital Plus',info)
            Audio_check_3=re.search('Dolby Digital Audio',info)
            Audio_check_4=re.search('AC.*3',info)
            Audio_check_5=re.search('音频.* Dolby Digital',info)
            Audio_check_6=re.search('AUDiO.*Dolby Digita',info)
            if Audio_check or Audio_check_5 or Audio_check_2 or Audio_check_3 or Audio_check_4 or Audio_check_6:
                return True
        if Audio_coding=='DTS-HD MA':
            Audio_check2=re.search('DTS-HD Master Audio',info)
            Audio_check2_1=('DTS-HD Master Audio',info)
            if Audio_check2 or Audio_check2_1:
                return True
        if Audio_coding=='TrueHD Atmos':
            Audio_check3=re.search('Atmos',info)
            if Audio_check3:
                return True
        if Audio_coding=='AAC':
            Audio_check4=re.search('Format.*AAC',info,re.I)
            Audio_check4_1 = re.search('Audio.*AAC', info,re.I)
            Audio_check4_2=re.search('格式.*AAC',info,re.I)
            Audio_check4_3=re.search('音.*频.*AAC',info)
            Audio_check_official=re.search('File Name.*AAC',info,re.I)
            if Audio_check4 or Audio_check4_1 or Audio_check4_2 or Audio_check4_3:
                return True
            if official_team and Audio_check_official:
                return True
        if Audio_coding=='TrueHD':
            Audio_check5=re.search('Dolby TrueHD',info,re.I)
            Audio_check5_1=re.search('Atmos',title,re.I)
            if Audio_check5 and not Audio_check5_1:
                return True
        if Audio_coding=='DTS':
            info2=info.replace('DTS-HD','')
            Audio_check6=re.search('Format.*DTS',info2)
            Audio_check6_1=re.search('音.*频.*DTS',info2)
            Audio_check6_2=re.search('文件格式.*DTS',info2)
            Audio_check6_3=re.search('AUDIO.*DTS',info2,re.I)
            if Audio_check6 or Audio_check6_1 or Audio_check6_2 or Audio_check6_3:
                return True
        if Audio_coding=='LPCM':
            Audio_check7_1=re.search('Format.*PCM',info,re.I)
            Audio_check7=re.search('LPCM.*Audio',info,re.I)
            if Audio_check7 or Audio_check7_1:
                return True
        if Audio_coding=='FLAC':
            Audio_check8=re.search('Format.*FLAC|AUDiO.*FLAC',info,re.I)
            if Audio_check8:
                return True
        if Audio_coding=='DTS-HD HR':
            Audio_check9=re.search('DTS-HD High Resolution Audio',info)
            Audio_check9_1=re.search('DTS-HD High-Res Audio',info)
            Audio_check9_2=re.search('DTS-HD Hi-Res',info)
            Audio_check9_3=re.search('DTS.*2046 Kbps',info)
            if Audio_check9 or Audio_check9_1 or Audio_check9_2 or Audio_check9_3:
                return True
        if Audio_coding=='Other':
            Audio_check10=re.search('MPEG Audio',info)
            Audio_check10_2=re.search('MPEG2',info)
            if Audio_check10 or Audio_check10_2:
                return True
        if Audio_coding=='TrueHD':
            Audio_check3 = re.search('Atmos', info)
            Audio_check11=re.search('AUDIO.*TrueHD',info,re.I)
            if Audio_check11 and not  Audio_check3:
                return True
    def check_Audio_coding_answer():
        Audiod=check_Audio_coding_feedback()
        if check_Audio_coding() is True:
            return '音频编码'+Audio_coding+'正确'
        else:
            if Audiod:
                return '音频编码' + Audio_coding + '错误'+Audiod
            else:
                return '音频编码' + Audio_coding + '错误'

    return check_Audio_coding_answer()