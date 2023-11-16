-- This script lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

USE hbtn_0d_tvshows_rate;

SELECT tv_genres.name, SUM(tv_show_ratings.rate) as rating
FROM
tv_shows
JOIN
tv_show_ratings
ON
tv_show_ratings.show_id = tv_shows.id
JOIN
tv_genres
ON
tv_genres.id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY rating DESC;
