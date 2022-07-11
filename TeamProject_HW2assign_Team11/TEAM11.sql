-- CREATE DATABASE

create database TEAM11;
use TEAM11;

-- CREATE TABLES

-- PATIENTINFO
CREATE TABLE PATIENTINFO(
patient_id BIGINT not null,
sex VARCHAR(10) DEFAULT 'NULL',
age VARCHAR(10) DEFAULT 'NULL',
country VARCHAR(50) DEFAULT 'NULL',
province VARCHAR(50) DEFAULT 'NULL',
city VARCHAR(50) DEFAULT 'NULL',
infection_case VARCHAR(50) DEFAULT 'NULL',
infected_by BIGINT,
contact_number INT,
symptom_onset_date DATE,
confirmed_date DATE,
released_date DATE,
deceased_date DATE,
state VARCHAR(20) DEFAULT 'NULL',
primary key(patient_id)
);

-- CASEINFO
CREATE TABLE CASEINFO(
case_id INT not null,
province VARCHAR(50) DEFAULT 'NULL',
city VARCHAR(50) DEFAULT 'NULL',
infection_group TINYINT(1),
infection_case VARCHAR(50) DEFAULT 'NULL',
confirmed INT,
latitude FLOAT,
longitude FLOAT,
primary key(case_id)
);

-- REGION
CREATE TABLE REGION(
region_code INT not null,
province VARCHAR(50) DEFAULT 'NULL',
city VARCHAR(50) DEFAULT 'NULL',
latitude FLOAT,
longitude FLOAT,
elementary_school_count INT,
kindergarten_count INT,
university_count INT,
academy_ratio FLOAT,
elderly_population_ratio FLOAT,
elderly_alone_ratio FLOAT,
nursing_home_count INT,
primary key(region_code)
);

-- WEATHER
CREATE TABLE WEATHER(
region_code INT not null,
province VARCHAR(50) DEFAULT 'NULL',
wdate DATE not null,
avg_temp FLOAT,
min_temp FLOAT,
max_temp FLOAT,
primary key(region_code, wdate)
);

-- TIMEINFO
create table TimeInfo(
date DATE,
test int(11),
negative int(11),
confirmed int(11),
released int(11),
deceased int(11),
primary key (date)
);

-- TIMEAGE
create table TimeAge(
date DATE,
age varchar(4),
confirmed int(11),
released int(11),
deceased int(11),
primary key (date, age)
);

-- TIMEGENDER
create table TimeGender(
date DATE,
sex varchar(10),
confirmed int(11),
released int(11),
deceased int(11),
primary key (date, sex)
);

-- TIMEGENDER
create table TimeProvince(
date DATE,
province varchar(30),
confirmed int(11),
released int(11),
deceased int(11),
primary key (date, province)
);


--AFTER DATA INSERTING

--FOREIGN_KEY_CHECKS_DISABLED
set foreign_key_checks = 0;

-- CREATE INDEX FOR FOREIGN KEY
create index idx_age_id on patientinfo(age);
create index idx_sex_id on patientinfo(sex);
create index idx_province_id on patientinfo(province);
create index idx_infection_case_id on patientinfo(infection_case);
create index idx_wdate_id on patientinfo(confirmed_date);


-- ADD FOREIGN KEY
ALTER TABLE patientinfo ADD FOREIGN KEY (infected_by) REFERENCES patientinfo (patient_id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE caseinfo ADD FOREIGN KEY (infection_case) REFERENCES patientinfo (infection_case) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE region ADD FOREIGN KEY (province) REFERENCES patientinfo (province) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE weather ADD FOREIGN KEY (wdate) REFERENCES patientinfo (confirmed_date) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE timeage ADD FOREIGN KEY (date) REFERENCES timeinfo (date) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE timegender ADD FOREIGN KEY (date) REFERENCES timeinfo (date) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE timeprovince ADD FOREIGN KEY (date) REFERENCES timeinfo (date) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE timeage ADD FOREIGN KEY (age) REFERENCES patientinfo (age) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE timegender ADD FOREIGN KEY (sex) REFERENCES patientinfo (sex) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE timeprovince ADD FOREIGN KEY (province) REFERENCES patientinfo (province) ON DELETE CASCADE ON UPDATE CASCADE;

--FOREIGN_KEY_CHECKS_ENABLED
set foreign_key_checks = 1;