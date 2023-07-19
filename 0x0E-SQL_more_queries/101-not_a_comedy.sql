-- A Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title.Sorted in asc order.
-- You can use a maximum of two SELECT statements.
SELECT ts.title
FROM `tv_shows` AS ts
WHERE ts.id NOT IN (
  SELECT tsg.show_id
  FROM `tv_show_genres` AS tsg
       INNER JOIN `tv_genres` AS tg
       ON tsg.genre_id = tg.id
  WHERE tg.name = 'Comedy'
)
ORDER BY ts.title ASC;
