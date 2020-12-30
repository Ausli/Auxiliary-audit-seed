import re



def vidioparme(soup):
    vidioinfo1 = soup.select('fieldset')
    vidioinfo2 = soup.select('.codemain')
    if vidioinfo1 and vidioinfo2:
        return vidioinfo1 + vidioinfo2
    if vidioinfo1 or vidioinfo2:
        return vidioinfo1, vidioinfo2




def link_check(soup, response):
    douban = soup.select('#kdouban a')
    imdb = re.search('http://www.imdb.com', response.text)
    if imdb or douban:
        return '有豆瓣或imdb链接'
    else:
        return '没有链接'




