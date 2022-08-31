# importing panda library
import os

import pandas as pd

destination = r"C:\Users\jbdim\Desktop"  # Place to save

print('File Path:')
filePath = input()
if os.path.join(filePath):
    print('File Fund')
    f = open(filePath, "r+")
    dataframe1 = pd.read_csv(f)
    dataframe1.to_csv(destination + r'\newCSV.csv',
                      index=None)
else:
    print('File not fund')
#test
