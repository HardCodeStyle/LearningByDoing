import csv

pathToDownload = r'C:\Users\jbdim\Downloads'  # pfad zum download
fileName = r'../WebApps/HistoricalData_1662138831034.csv'  # dateiname
with open(pathToDownload + fileName, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)  # data als list

newData = ['Halo'] * len(data)
newData[0] = data[0]
data.remove(data[0])

i = 1
for x in data:
    newData[i] = data[(len(data) - 1)]
    data.remove(data[(len(data) - 1)])

    i = i + 1
with open(pathToDownload + r'\bottomUP.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(newData)

print('Finish the exact path ---> ' + pathToDownload + r'bottomUP.csv')
