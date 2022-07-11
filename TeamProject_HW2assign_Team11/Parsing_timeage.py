import pandas as pd
import pymysql as mysqldb
from sqlalchemy import create_engine
import sqlalchemy

#connect to MySQL server
passwd = ''
dbname = 'team11'
db_connection_str = 'mysql+pymysql://root:' + passwd + '@localhost/' + dbname
db_cennction = create_engine(db_connection_str)
mydb = db_cennction.connect()

data = pd.read_sql_query('SELECT * FROM PATIENTINFO', mydb)

df = pd.read_csv('addtional_Timeinfo.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.drop(['test','negative'], axis = 1)

freq1 = data.groupby(['confirmed_date', 'age']).size()
freq1 = freq1.reset_index()
freq1.columns = ['date', 'age', 'confirmed']
freq1['date'] = pd.to_datetime(freq1['date'])

freq2 = data.groupby(['released_date', 'age']).size()
freq2 = freq2.reset_index()
freq2.columns = ['date', 'age', 'released']
freq2['date'] = pd.to_datetime(freq2['date'])

freq3 = data.groupby(['deceased_date', 'age']).size()
freq3 = freq3.reset_index()
freq3.columns = ['date', 'age', 'deceased']
freq3['date'] = pd.to_datetime(freq3['date'])

freq = pd.merge(df, freq1, how = 'outer', on='date')
freq = pd.merge(freq, freq2, how = 'outer', on=['date','age'])
freq = pd.merge(freq, freq3, how = 'outer', on=['date','age'])
freq = freq.sort_values(by=['date', 'age'], ascending=[True, True])
freq = freq.fillna(0)

freq['confirmed'] = freq.groupby('age')['confirmed'].cumsum()
freq['released'] = freq.groupby('age')['released'].cumsum()
freq['deceased'] = freq.groupby('age')['deceased'].cumsum()
indexNames = freq[freq['age']==0].index
freq.drop(indexNames, inplace= True)

dtypesql = {'date':sqlalchemy.types.DATE, 'age':sqlalchemy.types.VARCHAR(10), 'confirmed':sqlalchemy.types.INTEGER, 'released':sqlalchemy.types.INTEGER, 'deceased':sqlalchemy.types.INTEGER}

freq.to_sql(name = 'timeage', con = db_cennction, if_exists='append', index=False, dtype=dtypesql)