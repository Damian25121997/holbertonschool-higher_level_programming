-- create a database and a table in MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT UNIQUE AUTO_INCREMENT NOT NULL, state_id INT NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
