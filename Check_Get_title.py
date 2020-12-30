import re
import numpy as np
from email_decode import email_jimi
def title_get(soup):
    titlerow = soup.select('#top')[0].text
    title2 = re.match('(.*)    ', titlerow)
    titlemail = soup.select('.__cf_email__ ', )

    def title_check2():
        if title2:
            title = title2.group()
            return title
        else:
            title = titlerow
            return title
    title4=title_check2()
    if titlemail:
        email = email_jimi(titlemail[0].attrs['data-cfemail'])
        title3 = title4.replace('[email protected]', email)
        return title3
    else:
        return title4


def title_check(title):
    def title_float(title3):
        '''re.findall("(([1-9][0-9]*\.?[0-9]*)|(\.[0-9]+))([Ee][+-]?[0-9]+)?", title3)'''
        c = re.findall("(([1-9][0-9]*\.?[0-9]*)|(\.[0-9]+))([+-]?[0-9]+)?", title3)
        cc = []
        c1 = np.unique([j for i in c for j in i])
        for oo in c1:
            if oo.isdigit():
                pass
            if oo:
                try:
                    oo = int(oo)
                except:
                    if ValueError:
                        pass
                if type(eval(str(oo))) == float:
                    cc.append(oo)
        return cc
    check_title_folat=title_float(title)
    if check_title_folat:
        for team in check_title_folat:
            title_check3 = re.sub(str(team), '', title)
            if title_check3:
                title = title_check3

    if title.replace('[email protected]', '').replace('@', '').replace(' ', '') \
            .replace('WEB-DL', '').replace('-', '').replace(':', '').replace('：','') \
            .replace('H.264', '').replace('AVS+','').replace('H.265', '')\
            .replace('DD+','').replace("'", '') \
            .replace(' ', '').isalnum() is False:
        return '标题有问题'