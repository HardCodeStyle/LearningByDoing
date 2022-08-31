import csv

pathToDownload = r'C:\Users\jbdim\Downloads'  # pfad zum download
fileName = r'\cereal.csv'  # dateiname
with open(pathToDownload + fileName, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)  # data als list

print(data)
