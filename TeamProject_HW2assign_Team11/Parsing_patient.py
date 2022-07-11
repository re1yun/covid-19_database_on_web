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
patient = covid.loc[:,['patient_id', 'sex', 'age', 'country', 'province', 'city', 'infection_case', 'infected_by', 'contact_number', 'symptom_onset_date', 'confirmed_date', 'released_date', 'deceased_date', 'state']]

#insert into table
dtypesql = {'patient_id':sqlalchemy.types.BIGINT, 'sex':sqlalchemy.types.VARCHAR(10), 'age':sqlalchemy.types.VARCHAR(10), 'country':sqlalchemy.types.VARCHAR(50), 'province':sqlalchemy.types.VARCHAR(50), 'city':sqlalchemy.types.VARCHAR(50), 'infection_case':sqlalchemy.types.VARCHAR(50), 'infected_by':sqlalchemy.types.BIGINT, 'contact_number':sqlalchemy.types.INT, 'symptom_onset_date':sqlalchemy.types.DATE, 'confirmed_date':sqlalchemy.types.DATE, 'released_date':sqlalchemy.types.DATE, 'deceased_date':sqlalchemy.types.DATE, 'state':sqlalchemy.types.VARCHAR(20)}
patient.to_sql(name = 'patientinfo', con = db_cennction, if_exists='append', index=False, dtype=dtypesql)