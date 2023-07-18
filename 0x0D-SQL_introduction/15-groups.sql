-- Script that ists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server..
-- The result should display: score the number of records for this score with the label number,in desc order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
