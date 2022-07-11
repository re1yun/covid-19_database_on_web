import pandas as pd
import numpy as np
import pymysql as mysqldb
from sqlalchemy import create_engine
import sqlalchemy


mydb = mysqldb.connect(host = 'localhost', user = 'root', password = '', db = 'team11') #password 입력
curs = mydb.cursor()

#read the patientinfo, hospital and region data
patient = pd.read_sql_query('SELECT * FROM PATIENTINFO AS P LEFT JOIN REGION AS R ON P.province = R.province AND P.city = R.city', mydb)
hospital = pd.read_sql_query('SELECT * FROM hospital', mydb)
region = pd.read_sql_query('SELECT * FROM region', mydb)

#patient df에서 nan 값들을 모두 0으로 바꿔줌
patient = patient.fillna(0)
hospital = hospital.fillna(0)

#메인 프로세스
for pat, row in patient.iterrows():
    lat = row['latitude']               #환자의 위치 파악 완료
    long = row['longitude']
    min_distance = 9999999999999999999999.9
    if(lat == 0 and long == 0):         #값이 없으면 province의 대표 경도 위도 사용
        for reg, regrow in region.iterrows():
            province = row['province'].iloc[0]
            if(regrow['city'] == province):
                lat = regrow['latitude']
                long = regrow['longitude']
    pati = np.array((lat, long))
    for hos, hosrow in hospital.iterrows():        #hospital df를 돌면서 거리 계산
        hoslat = hosrow['hospital_latitude']
        hoslong = hosrow['hospital_longitude']
        hosi = np.array((hoslat, hoslong))
        distance = np.linalg.norm(pati - hosi)
        if(min_distance > distance):
            if(hosrow['current'] < hosrow['capacity']):
                min_distance = distance
                row['hospital_id'] = hosrow['hospital_id']
            else:
                continue
    hospital.loc[hospital['hospital_id'] == row['hospital_id'], 'current'] += 1
    patient.loc[patient['patient_id'] == row['patient_id'], 'hospital_id'] = row['hospital_id']

for i in range(0, len(patient)):
    sql = "UPDATE patientinfo SET hospital_id = " + str(int(patient.iloc[i, 14])) + " WHERE patient_id = " + str(patient.iloc[i, 0]) + ";"
    curs.execute(sql)
mydb.commit()