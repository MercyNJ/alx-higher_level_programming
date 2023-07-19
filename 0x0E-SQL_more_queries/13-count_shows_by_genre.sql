-- A Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>.
-- 1st column;genre,2nd column;number_of_shows,genres without a show shoulnt be displayed.
-- You can use only one SELECT statement, sorting;desc order.
SELECT tg.name AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS tg
       INNER JOIN `tv_show_genres` AS tsg
       ON tg.id = tsg.genre_id
 GROUP BY tg.name
 ORDER BY `number_of_shows` DESC;
