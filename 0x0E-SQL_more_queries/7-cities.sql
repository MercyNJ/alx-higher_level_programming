-- A Script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on my MySQL server.
-- City has an id, state_id & name;state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table.
-- If either database or table exists,  script should not fail.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	`id` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	`state_id`  INT   NOT NULL,
	`name`  VARCHAR(256)  NOT NULL,
	FOREIGN KEY(`state_id`) REFERENCES `hbtn_0d_usa`.`states`(`id`)
	);
