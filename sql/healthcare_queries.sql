CREATE TABLE patients (
 patient_id VARCHAR(20) PRIMARY KEY, age INT, gender VARCHAR(20),
 admission_type VARCHAR(30), diagnosis VARCHAR(50), length_of_stay INT,
 previous_admissions INT, emergency_visits INT, medication_count INT,
 diagnosis_count INT, lab_tests INT, days_since_last_admission INT,
 discharge_disposition VARCHAR(50), age_group VARCHAR(20),
 readmitted_30_days INT
);

-- Readmission rate by admission type
SELECT admission_type, COUNT(*) AS total_patients,
       SUM(readmitted_30_days) AS readmitted,
       ROUND(AVG(readmitted_30_days)*100,2) AS readmission_rate_pct
FROM patients GROUP BY admission_type;

-- Readmission rate by diagnosis
SELECT diagnosis, COUNT(*) AS total_patients,
       ROUND(AVG(readmitted_30_days)*100,2) AS readmission_rate_pct
FROM patients GROUP BY diagnosis ORDER BY readmission_rate_pct DESC;

-- High-utilization patients
SELECT patient_id, age, previous_admissions, emergency_visits,
       readmitted_30_days
FROM patients
WHERE previous_admissions >= 4 OR emergency_visits >= 3
ORDER BY previous_admissions DESC, emergency_visits DESC;
