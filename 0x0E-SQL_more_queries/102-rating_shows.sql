-- A Script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum.Sorted in dsc order.
-- You can use only one SELECT statement.
SELECT `title`, SUM(rate) AS rating
FROM `tv_shows` AS ts
INNER JOIN `tv_show_ratings` AS tsr ON ts.id = tsr.show_id
GROUP BY `title`
ORDER BY `rating` DESC;
