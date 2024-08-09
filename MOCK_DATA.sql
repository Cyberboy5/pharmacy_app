CREATE DATABASE chat_db;
USE chat_db;

CREATE TABLE users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(32),
    username VARCHAR(32) UNIQUE,
    password VARCHAR(32)
);

INSERT INTO users (name, username, password) VALUES 
('Aziz', 'aziz_killer', 'qwerty')

SELECT id FROM users WHERE username = login AND password = password