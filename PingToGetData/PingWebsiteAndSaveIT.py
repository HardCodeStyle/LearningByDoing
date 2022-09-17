import os
from datetime import datetime

from pythonping import ping


def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)


a = ping('www.google.de')
dateTimeObj = datetime.now()
remove_empty_lines('Ping_' + str(dateTimeObj.date()) + '.txt')
print(dateTimeObj.time())
with open('Ping_' + str(dateTimeObj.date()) + '.txt', 'a') as f:
    f.write("\n")
    f.write(str(a))
    f.write("")
    f.write("\n")
    f.write(str(dateTimeObj))
    f.write("\n")
    f.write("===")
    print('go on')
