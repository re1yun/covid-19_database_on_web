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

freq1 = data.groupby(['confirmed_date', 'province']).size()
freq1 = freq1.reset_index()
freq1.columns = ['date', 'province', 'confirmed']
freq1['date'] = pd.to_datetime(freq1['date'])

freq2 = data.groupby(['released_date', 'province']).size()
freq2 = freq2.reset_index()
freq2.columns = ['date', 'province', 'released']
freq2['date'] = pd.to_datetime(freq2['date'])

freq3 = data.groupby(['deceased_date', 'province']).size()
freq3 = freq3.reset_index()
freq3.columns = ['date', 'province', 'deceased']
freq3['date'] = pd.to_datetime(freq3['date'])

freq = pd.merge(df, freq1, how = 'outer', on='date')
freq = pd.merge(freq, freq2, how = 'outer', on=['date','province'])
freq = pd.merge(freq, freq3, how = 'outer', on=['date','province'])
freq = freq.sort_values(by=['date', 'province'], ascending=[True, True])
freq = freq.fillna(0)

freq['confirmed'] = freq.groupby('province')['confirmed'].cumsum()
freq['released'] = freq.groupby('province')['released'].cumsum()
freq['deceased'] = freq.groupby('province')['deceased'].cumsum()
indexNames = freq[freq['province']==0].index
freq.drop(indexNames, inplace= True)

dtypesql = {'date':sqlalchemy.types.DATE, 'province':sqlalchemy.types.VARCHAR(30), 'confirmed':sqlalchemy.types.INTEGER, 'released':sqlalchemy.types.INTEGER, 'deceased':sqlalchemy.types.INTEGER}

freq.to_sql(name = 'timeprovince', con = db_cennction, if_exists='append', index=False, dtype=dtypesql)