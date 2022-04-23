import xlsxwriter
import pandas as pd
from pathlib import Path
import os.path
import numpy as np

file = 'autoExcel.xlsx'
file_exists = os.path.exists(file)
workbook = xlsxwriter.Workbook(file)
worksheet = workbook.add_worksheet()

if file_exists == False:
	new = True
elif file_exists == True:
	oldf = pd.read_excel(file)
	oldstr= oldf.to_numpy()
	oldstr = oldstr.flatten()
	#column = len(oldstr)
	new = False
	print("file_exists, but thats fine")
	print("last value saved :")
	print(str(oldstr[-2])," ", str(oldstr[-1]))
column = 1
wholeString = input("input the whole text ")
#wholeString= "a 1 b 2 c 3 d 4"

newstrt = wholeString.split(" ")
newstr = list(newstrt)
if new == False:
	#aray = np.extend(oldstr, newstr)
	aray = np.append(oldstr, newstr)
else:
	aray = newstr

newsum = len(aray)

#print("file_exists, but thats fine")
for i in aray:
	temp = i
	if str(temp).isalpha():
		worksheet.write(column, 0, i)
	elif str(temp).isdigit() == True:
		worksheet.write(column, 1, str(i))
		#worksheet.write(column, 1, i)
		column += 1
workbook.close()
print("saved at ", file)