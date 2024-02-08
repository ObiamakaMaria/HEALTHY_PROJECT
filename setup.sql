-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS HEALTHY;
CREATE USER IF NOT EXISTS 'memmalino'@'localhost' IDENTIFIED BY 'password##';
GRANT ALL PRIVILEGES ON `HEALTHY`.* TO 'memmalino'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'memmalino'@'localhost';
FLUSH PRIVILEGES;
