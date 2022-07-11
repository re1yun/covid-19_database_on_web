import pandas as pd
import pymysql as mysqldb
from sqlalchemy import create_engine
import sqlalchemy

#connect to MySQL server
passwd = '' #password 입력
dbname = 'team11'
db_connection_str = 'mysql+pymysql://root:' + passwd + '@localhost/' + dbname
db_cennction = create_engine(db_connection_str)
mydb = db_cennction.connect()

#read the 'region.csv' data file
region = pd.read_csv('region.csv')

#필요한 열만 가져오기
df = region.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]].copy()
df.rename(columns={'code':'region_code'}, inplace=True)
df = df.drop_duplicates()

#insert into table
dtypesql = {'region_code':sqlalchemy.types.INTEGER, 'province':sqlalchemy.types.VARCHAR(50), 'city':sqlalchemy.types.VARCHAR(50), 'latitude':sqlalchemy.types.FLOAT, 'longitude':sqlalchemy.types.FLOAT, 'elementary_school_count':sqlalchemy.types.INTEGER, 'kindergarten_count':sqlalchemy.types.INTEGER, 'university_count':sqlalchemy.types.INTEGER, 'academy_ratio':sqlalchemy.types.FLOAT, 'elderly_population_ratio':sqlalchemy.types.FLOAT, 'elderly_alone_ratio':sqlalchemy.types.FLOAT, 'nursing_home_count':sqlalchemy.types.INTEGER}
df.to_sql(name = 'region', con = db_cennction, if_exists='replace', index=False, dtype=dtypesql)