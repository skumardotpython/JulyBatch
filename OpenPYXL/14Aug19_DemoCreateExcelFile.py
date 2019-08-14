from openpyxl import Workbook

book = Workbook()
sheet = book.active

sheet['b4'] = 'Python'
sheet['c5'] = 'Sheet'
sheet['d6'] = 12345

book.save('FirstExcelBook.xlsx')