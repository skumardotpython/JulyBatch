import openpyxl

book = openpyxl.load_workbook('ExcelApped.xlsx')
sheet = book.active

# c1 = sheet['a1']
# c2 = sheet['b2']
# c3 = sheet.cell(row=3, column=3).value

cells = sheet['A1' : 'B6']


#print(cells)

for cell in cells:
    for c in cell:
        print(c.value, end=' ')
    print()

print('*' * 100)

for c1,c2 in cells:
    print(c1.value, c2.value)

# cells = (
#             (10,20,30),
#             20,
#             30
#         )