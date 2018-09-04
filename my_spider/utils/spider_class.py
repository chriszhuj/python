import requests


class Spider:
    def __init__(self):
        header = dict()
        header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        header['Accept-Encoding'] = 'gzip, deflate, sdch, br'
        header['Accept-Language'] = 'zh-CN,zh;q=0.8'
        header['Connection'] = 'keep-alive'
        header['DNT'] = '1'
        header['referer'] = 'https://www.tmall.com/'
        header[
            'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
        # header['User-Agent'] = 'Mozilla/12.0 (compatible; MSIE 8.0; Windows NT)'
