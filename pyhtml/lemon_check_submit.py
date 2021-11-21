import os
import requests
from pyhtml.headersdata import headersdata

'''
审核通过： check_type=ok&check_remark=
审核不通过：check_type=fail&check_remark=
'''


def check_submit(url, check_type, remark=''):
    checl_url = f'{url}&action=check'
    data = {"check_type": check_type, "check_remark": remark}
    response = requests.post(checl_url, headers=headersdata(), data=data)
    return response.status_code


if __name__ == '__main__':
    url = 'https://lemonhd.org/details_doc.php?id=265028&group_id=tt14505430'
    remark = '请添加中字标签'
    check_submit(url)
