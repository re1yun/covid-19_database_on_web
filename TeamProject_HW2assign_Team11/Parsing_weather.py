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

#read the 'K_COVID19.csv' data file
covid = pd.read_csv('K_COVID19.csv')

#필요한 열만 가져오기
df = covid.loc[:,['region_code', 'province', 'confirmed_date', 'avg_temp', 'min_temp', 'max_temp']]
df.rename(columns={'confirmed_date':'wdate'}, inplace=True)
df = df.drop_duplicates()
NULLindex1 = df[df['region_code'].isnull()].index
NULLindex2 = df[df['wdate'].isnull()].index
df.drop(NULLindex1, inplace=True)
df.drop(NULLindex2, inplace=True)

#insert into table
dtypesql = {'region_code':sqlalchemy.types.INTEGER, 'province':sqlalchemy.types.VARCHAR(50), 'wdate':sqlalchemy.types.DATE, 'avg_temp':sqlalchemy.types.FLOAT, 'min_temp':sqlalchemy.types.FLOAT, 'max_temp':sqlalchemy.types.FLOAT}
df.to_sql(name = 'weather', con = db_cennction, if_exists='append', index=False, dtype=dtypesql)
