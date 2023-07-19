-- A Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id.
-- only one SELECT statement allowed.
SELECT ts.title, tg.genre_id
FROM `tv_shows` AS ts
INNER JOIN `tv_show_genres` AS tg
ON ts.id = tg.show_id
ORDER BY ts.title, tg.genre_id;
