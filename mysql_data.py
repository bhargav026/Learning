''' how to connect python and mysql workbench '''
import mysql_data.connector as con
mydb = con.connect(host = 'localhost', user = 'root', passwd = 'Bhargav@026')

cursor = mydb.cursor()
cursor.execute('show databases')
a = cursor.fetchall()
#print(a)
#print(len(a))

'''how to create table in dataset or create own dataset'''
cursor = mydb.cursor()
#cursor.execute('create database bhargav1')

#cursor.execute('create table bhargav1.ineuron(studentid INT(10), firstname VARCHAR(20), lastname VARCHAR(20), regid INT(15))')

cursor.execute('use bhargav1')
cursor.execute('show tables')
a = cursor.fetchall()
print(a)
cursor.execute('insert into bhargav1.ineuron values( 45461, "gfbff", "hufji", 445419 )')
mydb.commit()
cursor.execute('select * from bhargav1.ineuron')
a= cursor.fetchall()
print(a)
cursor.execute('insert into bhargav1.ineuron values( 844871, "ugfytdd", "uhgtyd", 54556 )')
mydb.commit()
print(cursor.fetchall())
 # if we insert values less or more than 4 gives an error
#cursor.execute('use bhargav1')
#cursor.execute('create table bhargav1.glassdata(col1 INT(10), col2 float(10,5), col3 float(10,5), col4 float(10,5), col5 float(10,5), col6 float(10,5), col7 float(10,5), col8 float(10,5), col9 float(10,5), col10 float(10,5), col11 INT(10))')
cursor.execute('show tables')
print(cursor.fetchall())

import csv
with open('glass.data','r') as f:
    glass_data = csv.reader(f, delimiter = '\n')
    for i in glass_data:
        #print(i)
        #print(i[0])
        #print(type(i[0]))
        cursor.execute(f'insert into bhargav1.glassdata values({str(i[0])})')
        #cursor.execute('insert into bhargav1.glassdata values({values})'.format(values = ({(i[0])})))
mydb.commit()
print(cursor.fetchall())

#import pandas as pd
#pd.read_sql("select * from bhargav1.glassdata", mydb)