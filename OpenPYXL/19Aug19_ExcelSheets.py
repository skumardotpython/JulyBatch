import openpyxl

book = openpyxl.load_workbook('iterbycols.xlsx')
sheet = book.active
print("Active Sheet : ", sheet.title)
print("All Sheet Names", book.sheetnames)

sheet = book['March']
print('Title is ', sheet.title)
print('Type of sheet is : ', type(sheet))
