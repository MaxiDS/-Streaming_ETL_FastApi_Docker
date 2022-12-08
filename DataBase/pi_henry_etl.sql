#drop database pi_henry_etl;

CREATE DATABASE pi_henry_etl;

use henry_etl;


-- MAESTROS DE LOS ARCHIVOS CARGADOS

DROP TABLE IF EXISTS streaming;

CREATE TABLE streaming (
	idStream varchar(30) NOT NULL,
	category varchar(50) NOT NULL,
	title varchar(120) NOT NULL,
	release_year INTEGER(20) NOT NULL,
    duration INTEGER(10) NOT NULL,
    type_duration varchar(20) NOT NULL,
    platform  varchar(20) NOT NULL
    
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
 
 DROP TABLE IF EXISTS `genre_table`;

CREATE TABLE genre_table (
  idStream varchar(30) ,
  genre varchar(80) NOT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
 
 
 DROP TABLE IF EXISTS `cast_table`;
CREATE TABLE cast_table (
  idStream varchar(30),
  cast varchar(120) NOT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;


