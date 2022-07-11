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

#read the 'hospital.csv' data file
hospital = pd.read_csv('hospital.csv')

#필요한 열만 가져오기
data = hospital.iloc[:, 0: 7] #[0, 1, 2, 3, 4, 5, 6, 7]]
data.rename(columns={'Hospital_id':'hospital_id', 'Hospital name': 'hospital_name', 'Hospital_province':'hospital_province','Hospital_city':'hospital_city', 'Hospital_latitude':'hospital_latitude', 'Hospital_longitude':'hospital_longitude', 'Current':'current'}, inplace=True)

#insert into table
dtypesql = {'hospital_id':sqlalchemy.types.INTEGER, 'hospital_name':sqlalchemy.types.VARCHAR(100), 'hospital_province':sqlalchemy.types.VARCHAR(50), 'hospital_city':sqlalchemy.types.VARCHAR(50), 'hospital_latitude':sqlalchemy.types.FLOAT, 'hospital_longitude':sqlalchemy.types.FLOAT, 'capacity':sqlalchemy.types.INTEGER, 'now':sqlalchemy.types.INTEGER}
data.to_sql(name = 'hospital', con = db_cennction, if_exists='append', index=False, dtype=dtypesql)