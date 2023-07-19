-- A Script that  lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_genres.name.Display NULL if show has no genre.
-- You can use only one SELECT statement. Sorting in asc order.
SELECT ts.title, tg.name
FROM `tv_shows` AS ts
LEFT JOIN `tv_show_genres` AS tsg ON ts.id = tsg.show_id
LEFT JOIN `tv_genres` AS tg ON tsg.genre_id = tg.id
ORDER BY ts.title ASC, tg.name ASC;
