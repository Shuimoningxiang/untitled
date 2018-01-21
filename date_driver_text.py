#coding=utf-8
import csv
#C:\Users\51Testing\PycharmProjects\untitled\date\huiyuan.csv
path ="C:/Users/51Testing/PycharmProjects/untitled/date/huiyuan.csv"
#path=r'C:\Users\51Testing\PycharmProjects\untitled\date\huiyuan.csv'
file=open(path,'r')
table=csv.reader(file)
for item in table:
    print(item)