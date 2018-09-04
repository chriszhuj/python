import xlwt as xl

t = "yunid=&f351e50e7e546&trid=792a11cc14944070226038595e&asid=AQAAAABu1xJZQYNVEgAAAAAu"
print(t.find('yunid'))
print(type(t.find('trid')))
yunid = t[0 + 6: 21]
yunid = t[t.find('yunid') + 6: t.find('trid')]
print(yunid)

brands = ['蓝月亮', '白猫', ]
for brand in brands:
    print(brand)

pageCount = 0
file = xl.Workbook()
nextPage = True
for brand in brands:
    sheet = file.add_sheet(brand)
    sheet.write(0, 0, '产品名称')
    while pageCount < 2 and nextPage:
        pageCount += 1
        sheet.write(pageCount, 0, '产品名称')
file.save('/Users/chrisz/Desktop/test.xls')
