import re
def check_code_All(code,info,medium,route,title):
    def check_code_feedback():
        code_type1 = re.search('MPEG' ,info.replace('V_MPEG4',''))
        code_type2 = re.search('Version.*2', info,re.I)
        code_type1_1=re.search('ViDEO.*MPEG2',info)
        code_type4 = re.search('Format.*AVC', info)
        code_type4_1 = re.search('MPEG4', info)
        code_type6 = re.search('HEVC', info)
        code_type6_1=re.search('H(?=.265|265)',route.text)
        code_type7=re.search('x265',info)
        code_type7_1=re.search('x265',route.text)
        code_type7_2=re.search('x264',info)
        code_type7_3=re.search('x264',route.text)
        if code_type1 and code_type2 or code_type1_1:
            return ' 应为MPEG-2'
        if code_type7_2 and code_type7_3:
            return ' 应为x264'
        if code_type7_1 and code_type7:
            return ' 应为x265'
        if code_type4_1 or code_type4:
            return ' 应为H.264/AVC'
        if code_type6 or code_type6_1:
            return ' 应为H.265/HEVC'
    def check_code():
        def email_decode():
            x_info=re.findall('data-cfemail="(.*)" href="/cdn-cgi/l/email-protection',info)
            if x_info:
                from  email_decode import email_jimi
                email_data = x_info[0]
                x_info_data = email_jimi(email_data)
                return x_info_data


        if code=='MPEG-2':
            code_type1_2 = re.search('ViDEO.*MPEG2', info)
            code_type1=re.search('MPEG',info.replace('V_MPEG4',''))
            code_type2=re.search('Version.*2',info,re.I)
            code_type1_1=re.search('MPEG-2 Video',info,re.I)
            if code_type1 and code_type2:
                return True
            if code_type1_1 or code_type1_2:
                return True
        if code=='H.264/AVC':
            code_type4=re.search('Format.*AVC',info)
            code_type4_1=re.search('MPEG4',info)
            code_type4_2=re.search('MPEG-4 AVC',info)
            code_type4_3=re.search('Video.*AVC',info,re.I)
            if code_type4 or code_type4_1 or code_type4_2 or code_type4_3:
                return True
        if code=='H.265/HEVC':
            code_type6=re.search('HEVC',info)
            if code_type6:
                return True

        if code=='H.264/AVC' and  medium=='Blu-ray' :
            code_type3=re.search('AVC',info)
            if code_type3:
                return True
        if code=='H.265/HEVC' and medium=='UHD Blu-ray':
            return True
        if code=='H.264/AVC' or code=='H.265/HEVC':
            code2=code.replace('H.','').replace('/AVC','').replace('/HEVC','')
            code_type9_1=re.search("h.*"+code2,info,re.I)
            code_type9_2=re.search("h.*"+code2,route.text,re.I)
            if   code_type9_1 and code_type9_2:
                return True
        if code=='x264' or code=='x265':
            code_type8=re.search('VIDEO.*'+code,info,re.I)
            if email_decode():
                code_type7=re.search(code,email_decode())
                if  code_type7:
                    return True
            if code_type8 :
                return True
        if code=='x264':
            code_type10=re.search('x264',info)
            code_type10_1=re.search('x265',info)
            code_type10_2=re.search('Writing.*library.*x264',info,re.I)
            if code_type10_2:
                return True
            if code_type10 and not code_type10_1:
                return True
        if code=='x265':
            code_type11_2=re.search('x265.*info',info)
            code_type11_3=re.search('x265',title)
            code_type11=re.search('x265',info)
            code_type11_1=re.search('264',info)
            if code_type11 and not code_type11_1:
                return True
            if code_type11_2 and code_type11_3:
                return True
        if code=='VC-1':
            code_type12=re.search('Video.*VC-1',info,re.I)
            code_type12_1=re.search('VC-1.*Video',info,re.I)
            code_type12_2=re.search('Format.*VC-1',info,re.I)
            if code_type12 or code_type12_1 or code_type12_2:
                return True
        if code=='Other':
            code_type13=re.search('Format.*AVS+',info,re.I)
            if code_type13:
                return True
    def check_code_answer():
        coded=check_code_feedback()
        if check_code() is True:
            return '编码'+code+'正确'
        else:
            if coded:
                return '编码'+code+'错误'+coded
            else:
                return '编码'+code+'错误'
    return check_code_answer()