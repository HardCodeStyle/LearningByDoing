from datetime import datetime

with open('MSCI_ACWI.txt') as f:
    content = str(f.readlines())
split_string = content.split("data-last-price=", 1)
split_string_two = split_string[1].split("data-last-normal-market-timestamp", 1)
print(split_string_two[0])
price = split_string_two[0].replace('"', "")
new_price = float(price.strip())
print(price)
dateTimeObj = datetime.now()
print(dateTimeObj.time())
with open('Price.txt', 'a') as f:
    f.write("\n")
    f.write(str(new_price))
    f.write(",")
    f.write(str(dateTimeObj.date()))
