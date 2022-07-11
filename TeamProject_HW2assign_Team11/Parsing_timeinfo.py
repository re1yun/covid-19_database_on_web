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

df = pd.read_csv('C:\python\\addtional_Timeinfo.csv')
df['date'] = pd.to_datetime(df['date'])

freq1 = data.groupby(['confirmed_date']).size()
freq1 = freq1.reset_index()
freq1.columns = ['date', 'confirmed']
freq1['date'] = pd.to_datetime(freq1['date'])

freq2 = data.groupby(['released_date']).size()
freq2 = freq2.reset_index()
freq2.columns = ['date', 'released']
freq2['date'] = pd.to_datetime(freq2['date'])

freq3 = data.groupby(['deceased_date']).size()
freq3 = freq3.reset_index()
freq3.columns = ['date', 'deceased']
freq3['date'] = pd.to_datetime(freq3['date'])

freq = pd.merge(df, freq1, how = 'outer', on='date')
freq = pd.merge(freq, freq2, how = 'outer', on='date')
freq = pd.merge(freq, freq3, how = 'outer', on='date')
freq = freq.fillna(0)
freq['confirmed'] = freq['confirmed'].cumsum()
freq['released'] = freq['released'].cumsum()
freq['deceased'] = freq['deceased'].cumsum()

dtypesql = {'date':sqlalchemy.types.DATE, 'test':sqlalchemy.types.INTEGER, 'negative':sqlalchemy.types.INTEGER, 'confirmed':sqlalchemy.types.INTEGER, 'released':sqlalchemy.types.INTEGER, 'deceased':sqlalchemy.types.INTEGER}
freq.to_sql(name = 'timeinfo', con = db_cennction, if_exists='append', index=False, dtype=dtypesql)
