import openpyxl

book = openpyxl.load_workbook('ExcelApped.xlsx')
sheet = book.active

c1 = sheet['a1']
c2 = sheet['b2']
c3 = sheet.cell(row=3, column=3).value

print('Column1 - a1 : ', c1.value)
print('Column2 - b2 : ', c2.value)
print('Column3 - 3,3 : ', c3)
