-- Vytvoření databáze, pokud ještě neexistuje
CREATE DATABASE IF NOT EXISTS task_manager;

-- Přepnutí na databázi
USE task_manager;

-- Vytvoření tabulky ukoly, pokud ještě neexistuje
CREATE TABLE IF NOT EXISTS ukoly (
    id INT AUTO_INCREMENT PRIMARY KEY,                        -- unikátní ID úkolu
    nazev VARCHAR(255) NOT NULL,                              -- název úkolu (povinný)
    popis TEXT NOT NULL,                                      -- popis úkolu (povinný)
    stav ENUM('Nezahájeno', 'Probíhá', 'Hotovo') NOT NULL     -- stav úkolu
        DEFAULT 'Nezahájeno',                                 -- výchozí hodnota
    datum_vytvoreni DATETIME NOT NULL                         -- čas vytvoření
        DEFAULT CURRENT_TIMESTAMP                             -- výchozí čas: teď
);
