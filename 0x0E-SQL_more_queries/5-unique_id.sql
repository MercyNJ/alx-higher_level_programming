-- A Script that creates the table unique_id on my MySQL server.
-- Should have id and name; id INT with the default value 1 and must be unique.
-- If the table unique_id already exists, your script should not fail.
CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
	);
