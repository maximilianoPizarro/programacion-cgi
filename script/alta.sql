DROP PROCEDURE IF EXISTS `alta`;

DELIMITER $$

CREATE DEFINER='root'@'localhost' PROCEDURE `alta` (
    IN nombre varchar(128), IN apellido varchar(128),
    IN anio year)
BEGIN
    DECLARE identicador_actor INT;
    DECLARE identificador_film INT;
    DECLARE listado CURSOR FOR 
    SELECT film_id FROM film WHERE  film.release_year=anio;
START TRANSACTION;
    INSERT INTO actor (first_name,last_name) 
    VALUES(nombre,apellido);    
    SELECT max(actor.actor_id) FROM actor INTO identicador_actor;
    OPEN listado;
    read_loop: LOOP
      FETCH listado INTO identificador_film;
      INSERT INTO film_actor (actor_id,film_id)
      VALUES (identicador_actor,identificador_film);
    END LOOP;   
    CLOSE listado;
COMMIT;
SELECT max(actor_id), first_name, last_name 
FROM actor; 
END $$

DELIMITER ;



