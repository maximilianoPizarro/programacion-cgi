DROP PROCEDURE IF EXISTS `busqueda`;

DELIMITER $$

CREATE DEFINER='root'@'localhost' PROCEDURE `busqueda` (
    IN titulo varchar(128), IN anio year, IN categoria int
)
BEGIN
    select film.film_id,         
            film.title, 
            film.release_year , 
            actor.first_name,actor.last_name
            from film, actor,film_actor, film_category 
            where film_actor.film_id=film.film_id      
            and film_actor.actor_id=actor.actor_id 
            and anio like film.release_year 
            and film.title LIKE CONCAT('%', titulo , '%')
            and categoria=film_category.category_id 
            group by  film.film_id,         
            film.title, 
            film.release_year,actor.first_name,actor.last_name  WITH ROLLUP;
END $$

DELIMITER ;



