-- A Script that  lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id,in asc order sort.
-- Only one SELECT statement allowed.
SELECT ts.title, tg.genre_id
FROM `tv_shows` AS ts
LEFT JOIN `tv_show_genres` AS tg
ON ts.id = tg.show_id
WHERE tg.genre_id IS NULL
ORDER BY ts.title, tg.genre_id;
