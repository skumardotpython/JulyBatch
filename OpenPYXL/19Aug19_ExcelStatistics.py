import openpyxl
import statistics as stat

book = openpyxl.load_workbook('iterbycols.xlsx', data_only=True)
sheet = book.active

rows = sheet.rows

values = []

for row in rows:
    for cell in row:
        values.append(cell.value)

print("Length of list is ", len(values))
print("Min Value ", min(values))
print("Max Value ", max(values))
print("Variance ", stat.variance(values))
print("Mean ", stat.mean(values))
print('Sum : ', sum(values))

