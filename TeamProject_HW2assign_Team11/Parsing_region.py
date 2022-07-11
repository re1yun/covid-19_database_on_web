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
df = covid.iloc[:,[23, 4, 5, 24, 25, 26, 27, 28, 29, 30, 31, 32]].copy()
df.rename(columns={'latitude.1':'latitude'}, inplace=True)
df.rename(columns={'longitude.1':'longitude'}, inplace=True)
df = df.drop_duplicates()
NULLindex = df[df['region_code'].isnull()].index
df.drop(NULLindex, inplace=True)

#insert into table
dtypesql = {'region_code':sqlalchemy.types.INTEGER, 'province':sqlalchemy.types.VARCHAR(50), 'city':sqlalchemy.types.VARCHAR(50), 'latitude':sqlalchemy.types.FLOAT, 'longitude':sqlalchemy.types.FLOAT, 'elementary_school_count':sqlalchemy.types.INTEGER, 'kindergarten_count':sqlalchemy.types.INTEGER, 'university_count':sqlalchemy.types.INTEGER, 'academy_ratio':sqlalchemy.types.FLOAT, 'elderly_population_ratio':sqlalchemy.types.FLOAT, 'elderly_alone_ratio':sqlalchemy.types.FLOAT, 'nursing_home_count':sqlalchemy.types.INTEGER}
df.to_sql(name = 'region', con = db_cennction, if_exists='append', index=False, dtype=dtypesql)