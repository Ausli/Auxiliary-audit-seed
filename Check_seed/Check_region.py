from pyhtml.region import European_American_countries,Gang_tai
def check_region_all(soup, region):
    import re
    def check_feedback():
        for i in European_American_countries:
            country = re.search('产.*地.*' + i, html,re.I)
            if country:
                return ' 应为EU&US(欧美)'
        for i2 in Gang_tai:
            country2 = re.search(i2, html)
            if country2:
                return ' 应为HK&TW(港台)'
        country_type = re.search('大陆', html)
        country_type_1 = re.search('中国大陆', html)
        if country_type or country_type_1:
            return ' 应为China(大陆)'

    def check_region():
        global html
        html = str(soup.select('#kdescr'))
        if region == 'EU&US(欧美)':
            # imdb_douban_link = str(soup.select('.faqlink'))
            for i in European_American_countries:
                country = re.search(i, html)
                if country:
                    return True
        if region == 'HK&TW(港台)':
            for i2 in Gang_tai:
                country2 = re.search(i2, html)
                if country2:
                    return True
        if region == 'China(大陆)':
            country_type = re.search('产.*地.*|国.*家.*' + '大陆', html)
            country_type_1 = re.search('产.*地.*|国.*家.*' + '中国大陆', html)
            country_type_2 = re.search('产.*地.*|国.*家.*' + '中国', html)
            if country_type or country_type_1 or country_type_2:
                return True
        if region == 'JP&KR(日韩)':
            country_type_2 = re.search('产.*地.*|国.*家.*' + '日本', html)
            country_type_3 = re.search('产.*地.*|国.*家.*' + '韩国', html)
            if country_type_2 or country_type_3:
                return True
        if region=='Other(其他)':
            country_type_4=re.search('产.*地.*未知',html)
            country_type_5=re.search('产.*地.*印度',html)
            country_type_6 = re.search ('产.*地.*巴西', html)
            if country_type_4 or country_type_5 or country_type_6:
                return True

    def check_region_answer():
        if check_region() is True:
            return '确认为' + region + '地区'
        else:
            if check_feedback():
                return '地区' + region + '错误' + check_feedback()
            else:
                return '地区' + region + '未知'

    return check_region_answer()