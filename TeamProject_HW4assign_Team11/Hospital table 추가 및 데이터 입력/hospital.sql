-- create hospital
CREATE TABLE hospital(
hospital_id int NOT NULL,
hospital_name varchar(100),
hospital_province varchar(50),
hospital_city varchar(50),
hospital_latitude float,
hospital_longitude float,
capacity int,
current int,
primary key(hospital_id)
);

-- add hospital_id into patientinfo table
ALTER TABLE patientinfo ADD hospital_id int;
