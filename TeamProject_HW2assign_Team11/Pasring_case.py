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
df = covid.iloc[:,[17, 4, 18, 19, 6, 20, 21, 22]].copy()
df.rename(columns={'city.1':'city'}, inplace=True)
df = df.drop_duplicates()
NULLindex = df[df['case_id'].isnull()].index
df.drop(NULLindex, inplace=True)

#insert into table
dtypesql = {'case_id':sqlalchemy.types.INTEGER, 'province':sqlalchemy.types.VARCHAR(50), 'city':sqlalchemy.types.VARCHAR(50), 'infection_group':sqlalchemy.types.INTEGER, 'infection_case':sqlalchemy.types.VARCHAR(50), 'confirmed':sqlalchemy.types.INTEGER, 'latitude':sqlalchemy.types.FLOAT, 'longitude':sqlalchemy.types.FLOAT}
df.to_sql(name = 'caseinfo', con = db_cennction, if_exists='append', index=False, dtype=dtypesql)