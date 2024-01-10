import pandas as pd
import pymysql
from sqlalchemy import create_engine
import xlrd

connection = pymysql.connect(host='localhost',user='root',password='')
cursor = connection.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS VIS')
cursor.close()
connection.close()

#NEO_EMON
engine = create_engine('mysql+pymysql://root:@localhost/VIS')
file_path="PQGAPP.xls"
sheet='NEO'
workbook = xlrd.open_workbook(file_path, encoding_override='utf-8')
df = pd.read_excel(workbook,sheet_name=sheet,usecols=['VIS', 'Date/heure de passage (porte physique)'])
df.columns = ['VIS', 'EMON']
df.to_sql('VIS', con=engine, if_exists='append', index=True)

print(df)
