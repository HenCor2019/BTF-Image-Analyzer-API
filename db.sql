CREATE DATABASE IF NOT EXISTS brain_tumor_detection;
USE brain_tumor_detection;

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    country VARCHAR(255),
    medical_role VARCHAR(255)
);
