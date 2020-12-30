def img_check(soup,imgheaders):
    import requests
    imgcheck=soup.select('#kdescr img')
    o=0
    all=0
    for i in imgcheck:
        all=all+1
        imglink=(i.attrs['src'])

        try:
            if requests.get(imglink,headers=imgheaders).status_code is 200 or 304:
                pass
            else:
                o=o+1
        except:
            if requests.exceptions.MissingSchema:
                o=o+1
    if o==0:
        if len(imgcheck)>1:
            print('图片正常')
        pass
    else:
        print('图片挂了'+str(o)+'张')
        print('图片一共'+str(all)+'张')