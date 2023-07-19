-- A Script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
-- Each record should display: tv_genres.name.Sorted in asc order.
-- You can use a maximum of two SELECT statements.
SELECT DISTINCT tg.`name`
FROM `tv_genres` AS tg
INNER JOIN `tv_show_genres` AS tsg
ON tg.`id` = tsg.`genre_id`
INNER JOIN `tv_shows` AS ts
ON tsg.`show_id` = ts.`id`
WHERE tg.`name` NOT IN
    (SELECT tg2.`name`
    FROM `tv_genres` AS tg2
    INNER JOIN `tv_show_genres` AS tsg2
    ON tg2.`id` = tsg2.`genre_id`
    INNER JOIN `tv_shows` AS ts2
    ON tsg2.`show_id` = ts2.`id`
    WHERE ts2.`title` = "Dexter")
ORDER BY tg.`name`;
