-- A Script that creates the MySQL server user user_0d_1.
-- User should have all priviledges, password should be set to user_0d_1_pwd & if user already exists, your script should not fail.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
