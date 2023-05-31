# Az Adat átalakítás folytonos szövegből Excel táblázatba (https://oa.webspecial.hu/posts/python-adat-atalakitas-folytonos-szoevegbol-excel-tablazatba/) bejegyzéshez tartozó kód.

import sys
import xlsxwriter

#Eredmény állomány nevének kiolvasása
if len(sys.argv) > 1:
    result=sys.argv[1]    
else:
    exit("A forrás állomány megadása kötelező! (Első paraméter)")

# Cél állomány megnevezése
if len(sys.argv) > 2:
    target=sys.argv[2]    
else:
    target=result+".xlsx"

print("Adatok feoldolgozása folyamatban!")

#Eredmények beolvasása
f = open(result)
  
lines = f.readlines()

keyList = []
data={}
lastKey=False

# átalakítása json fomrába - kiadvány a kulcs, tömb értékkel benne további tömb, dátum és érték páros
for line in lines:
    if not line.startswith(" "):
        lastKey=line.strip()
        data[lastKey] = []
        continue

    if lastKey == False:
        print("Hiba, nincs állomány név: {}".format(line))
        exit()

    dataValue = line.strip().split(" ")
    if not dataValue[1] in keyList:
        keyList.append(dataValue[1])
    
    data[lastKey].append([dataValue[1], dataValue[0]])


workbook = xlsxwriter.Workbook(target)
 
worksheet = workbook.add_worksheet()
 
row = 0

keyList.sort()

worksheet.write(row,0,"Url")
col = 1

#a header évek feltöltése
for date in keyList:
    worksheet.write(row,col,date)
    col +=1

row += 1

# adatok kiírása
for url in data.keys():
    worksheet.write(row, 0, url)
    for values in data[url]:
        col = keyList.index(values[0]);
        worksheet.write(row,col+1,int(values[1]))
    row +=1

workbook.close()
print("Excel sikeresen kiírva a(z) "+target+" állományba!")
