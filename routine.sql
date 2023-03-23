CREATE DATABASE IF NOT EXISTS routine;
USE routine;
CREATE TABLE IF NOT EXISTS routine_1 (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  date INT(15),
  earnings INT,
  exercise VARCHAR(25),
  study VARCHAR(25),
  coding VARCHAR(25),
  rest VARCHAR(25)
);
DESC routine_1;
