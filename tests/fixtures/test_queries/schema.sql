CREATE SCHEMA IF NOT EXISTS test;
CREATE TABLE IF NOT EXISTS test.rooms (
id int PRIMARY KEY,
name VARCHAR(50));
CREATE TABLE IF NOT EXISTS test.students (
birthday DATE,
id int,
name VARCHAR(60),
room int,
sex CHAR(1),
FOREIGN KEY (room) REFERENCES test.rooms(id) ON DELETE CASCADE);
