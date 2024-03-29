-- Script that displays the max temperature of each state (ordered by State name).
-- Utilizing provided table dump download.
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
