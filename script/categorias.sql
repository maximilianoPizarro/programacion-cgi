DROP PROCEDURE IF EXISTS `categorias`;

DELIMITER $$

CREATE DEFINER='root'@'localhost' PROCEDURE `categorias` (
)
BEGIN
    select category_id,name from category;
END $$

DELIMITER ;

