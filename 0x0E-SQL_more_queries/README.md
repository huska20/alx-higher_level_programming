7. Cities table

7-cities.sql: MySQL script that creates the database hbtn_0d_usa with a table cities.
cities description:
id: INT (unique, auto-generated, cannot be null and is a primary key)
state_id: INT (cannot be null, foreign key that references to id of the states table)
name: VARCHAR(256) (cannot be null)
8. Cities of California

8-cities_of_california_subquery.sql: MySQL script that lists all the cities of California that can be found in the database hbtn_0d_usa, ordered by ascending city id.
9. Cities by States

9-cities_by_state_join.sql: MySQL script that lists all cities contained in the database hbtn_0d_usa, ordered by ascending city id.
10. Genre ID by show

10-genre_id_by_show.sql: MySQL script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked, in order
