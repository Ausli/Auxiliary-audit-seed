import os

imgheaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4277.0 Safari/537.36 Edg/87.0.658.0',
        'Referer': 'https://lemonhd.org/torrents.php',
        }
def headersdata():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4346.0 Safari/537.36 Edg/89.0.731.0',
            'Referer': 'https://lemonhd.org/torrents.php',
            'authority': 'lemonhd.org'
        }
        if os.path.exists('cookie.txt'):
            cookie_data = open ('cookie.txt').read ()
            headers['cookie']=cookie_data
            return headers
        elif os.path.exists('../cookie.txt'):
            cookie_data = open ('../cookie.txt','r').read ()
            headers['cookie'] = cookie_data
            return headers
        else:
            return headers
if __name__ == '__main__':
    print (headersdata())