from time import sleep
from bs4 import BeautifulSoup
import xlwt as xl
import requests

brands = ['蓝月亮', '白猫', ]
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

pageCount = 0
file = xl.Workbook()
for brand in brands:
    sheet = file.add_sheet(brand)
    sheet.write(0, 0, '产品名称')
    sheet.write(0, 1, '产品链接')
    sheet.write(0, 2, '产品价钱')
    sheet.write(0, 3, '商铺链接')
    sheet.write(0, 4, '商铺名称')
    sheet.write(0, 5, '月销量')
    sheet.write(0, 6, '产品代码')
    nextPage = True
    row = 0
    pageCount == 0
    while pageCount < 200 and nextPage:
        print('正在爬取第' + str(pageCount / 60 + 1) + '页数据')
        if pageCount == 0:
            url = "https://list.tmall.com/search_product.htm?q=" + brand
        else:
            url = "https://list.tmall.com/search_product.htm?s=" + str(pageCount) + "&q=" + brand
        print('正在访问：' + url)
        r1 = requests.get(url, headers=header)
        print('访问结束')
        status_code = r1.status_code
        if status_code == 200:
            soap = BeautifulSoup(r1.content, 'html.parser')
            products = soap.find_all(attrs={"class": "product-iWrap"})
            if len(products) == 0:
                print("看来被天猫封了，貌似隔一小时可以重新获取，url is :" + url)
                nextPage = False
                # exit()
            for product in products:
                try:
                    productTitle = product.find(attrs={"class": "productTitle"}).find('a').get('title')
                    productLink = product.find(attrs={"class": "productTitle"}).find('a').get('href')
                    yunid = ''
                    if productLink is not None:
                        print('正在访问：' + productLink)
                        url_detail = "https:" + productLink
                        r_detail = requests.get(url_detail)
                        if r_detail.status_code == 200:
                            soap_detail = BeautifulSoup(r_detail.content, 'html.parser')
                            tmp = str(soap_detail)
                            yunid = tmp[tmp.find('yunid') + 6: tmp.find('trid')]
                        else:
                            print('访问详细页出错:' + url_detail)

                    productPrice = product.find(attrs={"class": "productPrice"}).find('em').get('title')
                    saleShopLink = product.find(attrs={"class": "productShop"}).find('a').get('href')
                    saleShopName = product.find(attrs={"class": "productShop"}).find('a').get_text()
                    saleShopCounts = product.find(attrs={"class": "productStatus"}).find('span').find('em').get_text()
                except Exception as ex:
                    print('出错了' + ex)
                    exit()
                row += 1
                sheet.write(row, 0, productTitle)
                sheet.write(row, 1, productLink)
                sheet.write(row, 2, productPrice)
                sheet.write(row, 3, saleShopLink)
                sheet.write(row, 4, saleShopName)
                sheet.write(row, 5, saleShopCounts)
                sheet.write(row, 6, yunid)
        else:
            print("error")
        pageCount += 60
        sleep(200)
    sleep(60)
file.save('/Users/chrisz/Desktop/test.xls')
print('Finish.....')
