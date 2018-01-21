import csv
import os
# path = os.path.dirname(__file__)
# final_path=path+"\date\huiyuan.csv"
# print(final_path)
def readData():
    path = os.path.dirname(__file__)
    final_path = path + "\date\huiyuan.csv"
    print(final_path)
    result=[]
    #file=open(final_path,'r')
    with open(final_path,'r') as file:
        table=csv.reader(file)
        for i in table:
            result.append(i)
#           print(i)
        #file.clse()
    return result
abcd=readData()
for i in abcd:
    for i2 in i:
        print(i2)
