import os
from urllib.request import urlopen

with urlopen('https://www.google.com/finance/quote/IUSQ:FRA') as webpage:
    content = webpage.read().decode()

print("Download complete")

with open('MSCI_ACWI.txt', 'w') as f:
    f.write(content)
os.system("cutInfoOut.py")
