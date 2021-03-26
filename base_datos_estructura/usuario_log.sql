USE rookie_coffee_db;

CREATE TABLE `log_acciones_usuario` (
  `_id` int NOT NULL AUTO_INCREMENT,
  `usuario` int unsigned NOT NULL,
  `accion` enum('Agregar','Modificar','Desactivar','Reactivar') NOT NULL,
  `tabla_objetivo` varchar(45) NOT NULL,
  `registro_objetivo` int NOT NULL,
  `fecha` varchar(45) NOT NULL,
  PRIMARY KEY (`_id`),
  KEY `usuario` (`usuario`),
  CONSTRAINT `usuario_log_fk` FOREIGN KEY (`usuario`) REFERENCES `usuario` (`_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
