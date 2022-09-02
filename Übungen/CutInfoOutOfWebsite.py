fileName = '../Download/MSCI_ACWI.txt'  # Dateiname oder pfad
beforeInformation = 'data-last-price='  # Html teil vor info ohne anführungszeichen
behindInformation = 'data-last-normal-market-timestamp'  # Html teil nach info ohne anführungszeichen
with open(fileName) as f:
    content = str(f.readlines())
splitBeforeInfo = content.split(beforeInformation, 1)
splitBehindInfo = splitBeforeInfo[1].split(behindInformation, 1)
info = splitBehindInfo[0].replace('"', "")  # Anführungszeichen entfernen
print(info)
