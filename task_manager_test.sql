CREATE DATABASE IF NOT EXISTS task_manager_test;

USE task_manager_test;

CREATE TABLE IF NOT EXISTS ukoly (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nazev VARCHAR(255) NOT NULL,
  popis TEXT NOT NULL,
  stav ENUM('Nezahájeno','Probíhá','Hotovo') NOT NULL DEFAULT 'Nezahájeno',
  datum_vytvoreni TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
