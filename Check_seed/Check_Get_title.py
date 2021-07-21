import re
import numpy as np
from .email_decode import email_jimi
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
    check_Video_suffix = re.search ('(mkv|mp4|iso|ts)\Z', title.replace(' ','').replace('its','').strip(), re.I)
    check_float=len(re.findall('/ss',title.replace('.','/ss')))
    if check_float>3:
        return '标题符号错误'

    if check_Video_suffix:
        return '标题有错误'