SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema beach_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema beach_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `beach_db` DEFAULT CHARACTER SET utf8 ;
USE `beach_db` ;

-- -----------------------------------------------------
-- Table `beach_db`.`beach`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `beach_db`.`beach` (
  `id` VARCHAR(22) NOT NULL,
  `name` VARCHAR(255) NULL,
  `beach` VARCHAR(255) NULL,
  `city` VARCHAR(255) NULL,
  `state` VARCHAR(255) NULL,
  `postal_code` VARCHAR(255) NULL,
  `latitude` FLOAT NULL,
  `longitude` FLOAT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `beach_db`.`photo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `beach_db`.`photo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `beach_id` VARCHAR(22) NOT NULL,
  `latitude` FLOAT NULL,
  `longitude` FLOAT NULL,
  `time_posted` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;
