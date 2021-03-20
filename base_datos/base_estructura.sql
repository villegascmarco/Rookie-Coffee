DROP database IF EXISTS rookie_coffee_db;
create database rookie_coffee_db;
use rookie_coffee_db;
-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: rookie_coffee_db
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `detalle_venta`
--

DROP TABLE IF EXISTS `detalle_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_venta` (
  `_id` int NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `precio_historico` varchar(45) NOT NULL COMMENT 'Precio historico hace referencia al precio del producto al momento de la venta',
  `estatus` enum('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
  `producto` int NOT NULL,
  `venta` int NOT NULL,
  PRIMARY KEY (`_id`),
  KEY `producto_venta_FK_idx` (`producto`),
  KEY `detalle_venta_fk_idx` (`venta`),
  CONSTRAINT `detalle_venta_fk` FOREIGN KEY (`venta`) REFERENCES `venta` (`_id`),
  CONSTRAINT `producto_venta_FK` FOREIGN KEY (`producto`) REFERENCES `producto` (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ingrediente`
--

DROP TABLE IF EXISTS `ingrediente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingrediente` (
  `_id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  `cantidad_disponible` double NOT NULL,
  `estatus` enum('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
  `unidad_medida` varchar(4) NOT NULL,
  `usuario` int NOT NULL,
  `fecha_registro` varchar(45) NOT NULL,
  PRIMARY KEY (`_id`),
  UNIQUE KEY `_id_UNIQUE` (`_id`),
  KEY `unidad_medida_fk_idx` (`unidad_medida`),
  CONSTRAINT `unidad_medida_fk` FOREIGN KEY (`unidad_medida`) REFERENCES `unidad_medida` (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ingrediente_producto`
--

DROP TABLE IF EXISTS `ingrediente_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingrediente_producto` (
  `_id` int NOT NULL AUTO_INCREMENT,
  `cantidad_requerida` double NOT NULL,
  `producto` int NOT NULL,
  `ingrediente` int NOT NULL,
  `estatus` enum('Activo','Inactivo') DEFAULT 'Activo',
  `usuario` int NOT NULL,
  `fecha_registro` varchar(45) NOT NULL,
  PRIMARY KEY (`_id`),
  UNIQUE KEY `_id_UNIQUE` (`_id`),
  KEY `producto_fk_idx` (`producto`),
  KEY `ingrediente_fk_idx` (`ingrediente`),
  CONSTRAINT `ingrediente_fk` FOREIGN KEY (`ingrediente`) REFERENCES `ingrediente` (`_id`),
  CONSTRAINT `producto_fk` FOREIGN KEY (`producto`) REFERENCES `producto` (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `inicio_sesion`
--

DROP TABLE IF EXISTS `inicio_sesion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inicio_sesion` (
  `_id` int NOT NULL AUTO_INCREMENT,
  `usuario` int unsigned NOT NULL,
  `fecha_inicio_sesion` varchar(45) NOT NULL,
  `dispositivo` varchar(50) NOT NULL,
  `direccion_ip` varchar(20) NOT NULL,
  `estatus` enum('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
  `token` varchar(300) NOT NULL,
  PRIMARY KEY (`_id`),
  KEY `usuario` (`usuario`),
  CONSTRAINT `inicio_sesion_ibfk_1` FOREIGN KEY (`usuario`) REFERENCES `usuario` (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `_id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(100) DEFAULT 'null',
  `precio` double NOT NULL,
  `estatus` enum('Activo','Inactivo') DEFAULT 'Activo',
  `usuario` int NOT NULL,
  `fecha_registro` varchar(45) NOT NULL,
  PRIMARY KEY (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rol_usuario`
--

DROP TABLE IF EXISTS `rol_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rol_usuario` (
  `_id` int unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `estatus` enum('Activo','Inactivo') NOT NULL,
  PRIMARY KEY (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `unidad_medida`
--

DROP TABLE IF EXISTS `unidad_medida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unidad_medida` (
  `_id` varchar(4) NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  `usuario` int NOT NULL,
  `fecha_registro` varchar(45) NOT NULL,
  PRIMARY KEY (`_id`),
  UNIQUE KEY `_id_UNIQUE` (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `_id` int unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido_1` varchar(45) NOT NULL,
  `apellido_2` varchar(45) NOT NULL,
  `rfc` varchar(13) NOT NULL,
  `nombre_acceso` varchar(45) NOT NULL,
  `contrasena` varchar(64) NOT NULL,
  `estatus` enum('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
  `rol_usuario` int unsigned NOT NULL,
  PRIMARY KEY (`_id`),
  KEY `rol_fk_idx` (`rol_usuario`),
  CONSTRAINT `rol_fk` FOREIGN KEY (`rol_usuario`) REFERENCES `rol_usuario` (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `_id` int NOT NULL AUTO_INCREMENT,
  `fecha` varchar(45) NOT NULL,
  `total_venta` double NOT NULL,
  `estatus` enum('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
  `usuario` int unsigned NOT NULL,
  PRIMARY KEY (`_id`),
  KEY `usuario_venta_FK_idx` (`usuario`),
  CONSTRAINT `usuario_venta_FK` FOREIGN KEY (`usuario`) REFERENCES `usuario` (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-19 19:02:42
