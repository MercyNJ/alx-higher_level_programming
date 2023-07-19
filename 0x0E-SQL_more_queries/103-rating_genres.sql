-- A Script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum.
-- You can use only one SELECT statement. Res sorted in desc order.
SELECT name, SUM(rate) AS rating
FROM `tv_genres`
INNER JOIN `tv_show_genres` AS tsg ON id = tsg.genre_id
INNER JOIN `tv_show_ratings` AS tsr ON tsg.show_id = tsr.show_id
GROUP BY name
ORDER BY rating DESC;
