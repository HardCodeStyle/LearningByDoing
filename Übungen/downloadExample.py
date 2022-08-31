from urllib.request import urlopen

url = 'https://www.google.com/finance/quote/IUSQ:FRA'  # url der website zum download
path = r'C:\Users\jbdim\Downloads'  # path wo die Text datei gespeichert wird
with urlopen(url) as webpage:
    content = webpage.read().decode()
print(content)
print("Download complete")

with open(path + r'\DownloadedPage.txt', 'w') as f:
    f.write(content)
