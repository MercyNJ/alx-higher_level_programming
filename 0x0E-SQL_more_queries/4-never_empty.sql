-- A Script that creates the table id_not_null on my MySQL server.
-- Tbale should have ID & Name, ID has a default value 0f 1.
-- If the table id_not_null already exists, your script should not fail.
CREATE TABLE IF NOT EXISTS `id_not_null` (
	`id` INT DEFAULT 1,
	`name` VARCHAR(256)
	);
