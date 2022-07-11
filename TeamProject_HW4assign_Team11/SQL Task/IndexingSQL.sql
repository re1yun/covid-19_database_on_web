-- create index
CREATE INDEX idx_case_date ON PATIENTINFO(infection_case, confirmed_date);

-- invisible index
ALTER TABLE PATIENTINFO ALTER INDEX idx_infection_case_id INVISIBLE;
ALTER TABLE PATIENTINFO ALTER INDEX idx_wdate_id INVISIBLE;
ALTER TABLE PATIENTINFO ALTER INDEX idx_case_date INVISIBLE;

EXPLAIN SELECT patient_id, infection_case, confirmed_date FROM PATIENTINFO WHERE infection_case = 'overseas inflow' and confirmed_date = '2020-04-12';

SELECT patient_id, infection_case, confirmed_date FROM PATIENTINFO WHERE infection_case = 'overseas inflow' and confirmed_date = '2020-04-12';

-- visible index
ALTER TABLE PATIENTINFO ALTER INDEX idx_case_date VISIBLE;

EXPLAIN SELECT patient_id, infection_case, confirmed_date FROM PATIENTINFO WHERE infection_case = 'overseas inflow' and confirmed_date = '2020-04-12';

SELECT patient_id, infection_case, confirmed_date FROM PATIENTINFO WHERE infection_case = 'overseas inflow' and confirmed_date = '2020-04-12';