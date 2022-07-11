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

freq1 = data.groupby(['confirmed_date', 'sex']).size()
freq1 = freq1.reset_index()
freq1.columns = ['date', 'sex', 'confirmed']
freq1['date'] = pd.to_datetime(freq1['date'])

freq2 = data.groupby(['released_date', 'sex']).size()
freq2 = freq2.reset_index()
freq2.columns = ['date', 'sex', 'released']
freq2['date'] = pd.to_datetime(freq2['date'])

freq3 = data.groupby(['deceased_date', 'sex']).size()
freq3 = freq3.reset_index()
freq3.columns = ['date', 'sex', 'deceased']
freq3['date'] = pd.to_datetime(freq3['date'])

freq = pd.merge(df, freq1, how = 'outer', on='date')
freq = pd.merge(freq, freq2, how = 'outer', on=['date','sex'])
freq = pd.merge(freq, freq3, how = 'outer', on=['date','sex'])
freq = freq.sort_values(by=['date', 'sex'], ascending=[True, False])
freq = freq.fillna(0)

freq['confirmed'] = freq.groupby('sex')['confirmed'].cumsum()
freq['released'] = freq.groupby('sex')['released'].cumsum()
freq['deceased'] = freq.groupby('sex')['deceased'].cumsum()
indexNames = freq[freq['sex']==0].index
freq.drop(indexNames, inplace= True)

dtypesql = {'date':sqlalchemy.types.DATE, 'sex':sqlalchemy.types.VARCHAR(10), 'confirmed':sqlalchemy.types.INTEGER, 'released':sqlalchemy.types.INTEGER, 'deceased':sqlalchemy.types.INTEGER}

freq.to_sql(name = 'timegender', con = db_cennction, if_exists='append', index=False, dtype=dtypesql)