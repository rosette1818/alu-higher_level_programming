-- lists all shows without the genre Comedy, using a single SELECT with joins
SELECT title FROM tv_shows AS t
LEFT JOIN tv_show_genres AS tsg ON t.id = tsg.show_id
LEFT JOIN tv_genres AS tg ON tsg.genre_id = tg.id AND tg.name = "Comedy"
WHERE tg.id IS NULL
ORDER BY title;
