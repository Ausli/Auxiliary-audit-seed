import re
def medium_check_All(route, medium, info, title,soup):
    def info_check_feedback():
        medium_type = re.search('Encoding settings', info, re.I)
        medium_type5 = re.search('WEBRiP', info, re.I)
        medium_type5_1 = re.search('TV', info, re.I)
        medium_type5_2 = re.search('WEB-DL', info, re.I)
        medium_type_1 = re.search('BluRay.*x264', title)
        medium_type_2 = re.search('BluRay.*x265', title)
        medium_type6 = re.search('编码库', info, re.I)
        if medium_type5 or medium_type5_2:
            return ' 应为WEB-DL '
        if medium_type5_1 and not medium_type and not medium_type6 :
            return ' 应为HDTV'
        if medium_type_1 or medium_type_2 or medium_type6 or medium_type :
            return ' 应为Encode'

    def info_check():
        if medium == 'encode' or medium == 'Encode':
            medium_type_1 = re.search('BluRay.*x264', title,re.I)
            medium_type_2 = re.search('BluRay.*x265', title,re.I)
            medium_type_4=re.search('Encoded date',info)
            medium_type_3 = re.search('Encoding settings', info, re.I)
            medium_type_5 = re.search('编码库', info, re.I)
            if medium_type_1 or medium_type_2 or medium_type_3 or medium_type_4 or medium_type_5:
                return True
        if medium == 'Blu-ray' or medium == 'UHD Blu-ray':
            medium_type2 = re.search('mpls', route.text, re.I)
            medium_type2_1 = re.search('iso', route.text, re.I)
            medium_type2_2=re.search('ts',route.text)
            if medium_type2 or medium_type2_1 or medium_type2_2:
                return True
        if medium == 'HDTV' or medium == 'WEB-DL':
            # medium_type3=re.search(medium,info,re.I)
            medium_type3_2 = re.search(medium, title, re.I)
            if medium_type3_2:
                return True
        if medium == 'HDTV':
            medium_type5_1=re.search('TV',info,re.I)
            if medium_type5_1:
                return True
        if medium == 'WEB-DL':
            medium_type6 = re.search('WEB', info, re.I)
            medium_type6_1 = re.search('WEB', title, re.I)
            medium_type6_2=re.search('WEB',route.text,re.I)
            if medium_type6 and medium_type6_1:
                return True
            if medium_type6_1 and medium_type6_2:
                return True
        if medium == 'Remux':
            medium_type4_1=re.search(medium,title,re.I)
            medium_type4_2=re.search(medium,route.text,re.I)
            medium_type4_3=re.findall('Video / (.*) kbps',info,re.I)
            medium_type4_4=re.findall('Bit.*rate.*:(.*) (?=Mbps|Mb/s)',info,re.I)
            try:
                if float(medium_type4_4[0].replace('\xa0','').replace(' ','')) >20:
                    return True
            except:
                pass
            if medium_type4_1 and medium_type4_2:
                return True
            if medium_type4_3:
                if int(medium_type4_3[0])>20480:
                    return True
    def Number_of_files():
        if medium == 'Blu-ray' or medium == 'UHD Blu-ray':
            wenjianshu = soup.select('.no_border_wide')[0].text
            Blu_ray_iso = re.search('iso', route.text, re.I)
            Blu_ray_ts = re.search('ts', route.text, re.I)
            if wenjianshu:
                wenjianshu1 = re.search('\d+', wenjianshu).group()
                if int(wenjianshu1) > 68 or Blu_ray_iso or Blu_ray_ts:
                    return ''
                else:
                   return '\nBlu-ray 文件数 False'
        else:
            return ''
    def info_check_answer():
        check_Number_of_files=Number_of_files()
        if info_check() is True:
            return '媒介' + medium + '正确'+check_Number_of_files
        else:
            feedback=info_check_feedback()
            if feedback:
                return '媒介' + medium + '错误' + feedback+check_Number_of_files
            else:
                return '媒介' + medium + '错误'+check_Number_of_files

    return info_check_answer()