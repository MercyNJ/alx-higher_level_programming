-- A Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on my MySQL server.
-- Table states should have id & name;id INT unique, auto generated, can’t be null and is a primary key,name cant be null.
-- If the table states already exists,my script should not fail.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
	`id` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	`name` VARCHAR(256) not null
	);
