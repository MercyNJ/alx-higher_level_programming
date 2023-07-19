-- A Script that  lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id,sorted in asc order.
-- If a show doesn’t have a genre, display NULL,only one SELECT statement allowed.
SELECT ts.title, tg.genre_id
FROM `tv_shows` AS ts
LEFT JOIN `tv_show_genres` AS tg
ON ts.id = tg.show_id
ORDER BY ts.title, tg.genre_id;
