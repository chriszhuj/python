import xlwt as xl

file = xl.Workbook()
sheet = file.add_sheet('蓝月亮')
sheet.write(0, 1, 'test1')
file.save('/Users/chrisz/Desktop/test.xls')
