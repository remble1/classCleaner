import os
import sys
import glob

filePath = rf'C:\Prototypy\gotowe_datasety_do_nauki\gotowe_dane_26_10\labels\*.txt'
folder = glob.glob(filePath)
result = []
for file in folder:
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            lineList = list(line.split(" "))
            try:
                if int(lineList[0]) > 52:
                    result.append({file})
                    # print(f"znaleziono błąd w {file}")
                    # del line
                    break
                else:
                    pass
            except:
                print(f"Sprawdzić plik: {file}")
                pass
print(result)

