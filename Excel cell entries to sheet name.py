# create new sheets from cell values
import os, openpyxl
os.chdir(r'F:\Downloads Firefox and Chrome')
wb = openpyxl.load_workbook('source_file.xlsx')
sheet = wb.active
# convert rows 2 - 32 in column A
for i in range(2,33):
    cellVal = sheet[('A'+str(i))].value
    wb.create_sheet(title=(cellVal))

wb.save('newfilename.xlsx')