CREATE SCHEMA IF NOT EXISTS task_1; #Нужно ли ссылаться на датабейз
CREATE TABLE IF NOT EXISTS task_1.rooms (
id int PRIMARY KEY,
name VARCHAR(50));
CREATE TABLE IF NOT EXISTS task_1.students (
birthday DATE,
id int,
name VARCHAR(60),
room int,
sex CHAR(1),
FOREIGN KEY (room) REFERENCES task_1.rooms(id) ON DELETE CASCADE);
