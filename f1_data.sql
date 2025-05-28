-- MariaDB dump 10.19  Distrib 10.6.4-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: f1_data
-- ------------------------------------------------------
-- Server version	10.6.4-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `balapan`
--

DROP TABLE IF EXISTS `balapan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `balapan` (
  `kode` varchar(3) NOT NULL,
  `urutan` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `negara` varchar(255) NOT NULL,
  PRIMARY KEY (`kode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `balapan`
--

LOCK TABLES `balapan` WRITE;
/*!40000 ALTER TABLE `balapan` DISABLE KEYS */;
INSERT INTO `balapan` VALUES ('ABU',24,'Grand Prix F1 Abu Dhabi 2025','UAE'),('AUS',1,'Grand Prix F1 Australia 2025','AUS'),('AUT',11,'Grand Prix F1 Austria 2025','AUT'),('AZE',17,'Grand Prix F1 Azerbaijan 2025','AZE'),('BEL',13,'Grand Prix F1 Belgia 2025','BEL'),('BHR',4,'Grand Prix F1 Bahrain 2025','BHR'),('CAN',10,'Grand Prix F1 Kanada 2025','CAN'),('CHN',2,'Grand Prix F1 Tiongkok 2025','CHN'),('EMI',7,'Grand Prix F1 Emilia Romagna 2025','ITA'),('ESP',9,'Grand Prix F1 Spanyol 2025','ESP'),('GBR',12,'Grand Prix F1 Britania 2025','GBR'),('HUN',14,'Grand Prix F1 Hungaria 2025','HUN'),('ITA',16,'Grand Prix F1 Italia 2025','ITA'),('JPN',3,'Grand Prix F1 Jepang 2025','JPN'),('LVG',22,'Grand Prix F1 Las Vegas 2025','USA'),('MIA',6,'Grand Prix F1 Miami 2025','USA'),('MON',8,'Grand Prix F1 Monako 2025','MON'),('MXC',20,'Grand Prix F1 Kota Meksiko 2025','MEX'),('NED',15,'Grand Prix F1 Belanda 2025','NED'),('QAT',23,'Grand Prix F1 Qatar 2025','QAT'),('SAP',21,'Grand Prix F1 São Paulo 2025','BRA'),('SAU',5,'Grand Prix F1 Arab Saudi 2025','KSA'),('SIN',18,'Grand Prix F1 Singapura 2025','SIN'),('USA',19,'Grand Prix F1 Amerika Serikat 2025','USA');
/*!40000 ALTER TABLE `balapan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hasil_balapan`
--

DROP TABLE IF EXISTS `hasil_balapan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hasil_balapan` (
  `kode_pembalap` varchar(3) NOT NULL,
  `kode_balapan` varchar(3) NOT NULL,
  `posisi` varchar(255) NOT NULL,
  `posisi_sprint` varchar(255) DEFAULT NULL,
  `pole` tinyint(1) DEFAULT NULL,
  `fl` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`kode_pembalap`,`kode_balapan`),
  KEY `kode_balapan` (`kode_balapan`),
  CONSTRAINT `hasil_balapan_ibfk_1` FOREIGN KEY (`kode_pembalap`) REFERENCES `pembalap` (`kode`),
  CONSTRAINT `hasil_balapan_ibfk_2` FOREIGN KEY (`kode_balapan`) REFERENCES `balapan` (`kode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hasil_balapan`
--

LOCK TABLES `hasil_balapan` WRITE;
/*!40000 ALTER TABLE `hasil_balapan` DISABLE KEYS */;
INSERT INTO `hasil_balapan` VALUES ('ALB','AUS','05',NULL,NULL,NULL),('ALB','BHR','12',NULL,NULL,NULL),('ALB','CHN','07',NULL,NULL,NULL),('ALB','EMI','05',NULL,NULL,NULL),('ALB','JPN','09',NULL,NULL,NULL),('ALB','MIA','05',NULL,NULL,NULL),('ALB','SAU','09',NULL,NULL,NULL),('ALO','AUS','Ret',NULL,NULL,NULL),('ALO','BHR','15',NULL,NULL,NULL),('ALO','CHN','Ret',NULL,NULL,NULL),('ALO','EMI','11',NULL,NULL,NULL),('ALO','JPN','11',NULL,NULL,NULL),('ALO','MIA','15',NULL,NULL,NULL),('ALO','SAU','11',NULL,NULL,NULL),('ANT','AUS','04',NULL,NULL,NULL),('ANT','BHR','11',NULL,NULL,NULL),('ANT','CHN','06','07',NULL,NULL),('ANT','EMI','Ret',NULL,NULL,NULL),('ANT','JPN','06',NULL,NULL,1),('ANT','MIA','06','07',NULL,NULL),('ANT','SAU','06',NULL,NULL,NULL),('BEA','AUS','14',NULL,NULL,NULL),('BEA','BHR','10',NULL,NULL,NULL),('BEA','CHN','08',NULL,NULL,NULL),('BEA','EMI','17',NULL,NULL,NULL),('BEA','JPN','10',NULL,NULL,NULL),('BEA','MIA','Ret',NULL,NULL,NULL),('BEA','SAU','13',NULL,NULL,NULL),('BOR','AUS','Ret',NULL,NULL,NULL),('BOR','BHR','18',NULL,NULL,NULL),('BOR','CHN','14',NULL,NULL,NULL),('BOR','EMI','18',NULL,NULL,NULL),('BOR','JPN','19',NULL,NULL,NULL),('BOR','MIA','Ret',NULL,NULL,NULL),('BOR','SAU','18',NULL,NULL,NULL),('COL','EMI','16',NULL,NULL,NULL),('DOO','AUS','Ret',NULL,NULL,NULL),('DOO','BHR','14',NULL,NULL,NULL),('DOO','CHN','13',NULL,NULL,NULL),('DOO','JPN','15',NULL,NULL,NULL),('DOO','MIA','Ret',NULL,NULL,NULL),('DOO','SAU','17',NULL,NULL,NULL),('GAS','AUS','11',NULL,NULL,NULL),('GAS','BHR','07',NULL,NULL,NULL),('GAS','CHN','DSQ',NULL,NULL,NULL),('GAS','EMI','13',NULL,NULL,NULL),('GAS','JPN','13',NULL,NULL,NULL),('GAS','MIA','13','08',NULL,NULL),('GAS','SAU','Ret',NULL,NULL,NULL),('HAD','AUS','DNS',NULL,NULL,NULL),('HAD','BHR','13',NULL,NULL,NULL),('HAD','CHN','11',NULL,NULL,NULL),('HAD','EMI','09',NULL,NULL,NULL),('HAD','JPN','08',NULL,NULL,NULL),('HAD','MIA','11',NULL,NULL,NULL),('HAD','SAU','10',NULL,NULL,NULL),('HAM','AUS','10',NULL,NULL,NULL),('HAM','BHR','05',NULL,NULL,NULL),('HAM','CHN','DSQ','01',NULL,NULL),('HAM','EMI','04',NULL,NULL,NULL),('HAM','JPN','07',NULL,NULL,NULL),('HAM','MIA','08','03',NULL,NULL),('HAM','SAU','07',NULL,NULL,NULL),('HUL','AUS','07',NULL,NULL,NULL),('HUL','BHR','DSQ',NULL,NULL,NULL),('HUL','CHN','15',NULL,NULL,NULL),('HUL','EMI','12',NULL,NULL,NULL),('HUL','JPN','16',NULL,NULL,NULL),('HUL','MIA','14',NULL,NULL,NULL),('HUL','SAU','15',NULL,NULL,NULL),('LAW','AUS','Ret',NULL,NULL,NULL),('LAW','BHR','16',NULL,NULL,NULL),('LAW','CHN','12',NULL,NULL,NULL),('LAW','EMI','14',NULL,NULL,NULL),('LAW','JPN','17',NULL,NULL,NULL),('LAW','MIA','Ret',NULL,NULL,NULL),('LAW','SAU','12',NULL,NULL,NULL),('LEC','AUS','08',NULL,NULL,NULL),('LEC','BHR','04',NULL,NULL,NULL),('LEC','CHN','DSQ','05',NULL,NULL),('LEC','EMI','06',NULL,NULL,NULL),('LEC','JPN','04',NULL,NULL,NULL),('LEC','MIA','07',NULL,NULL,NULL),('LEC','SAU','03',NULL,NULL,NULL),('NOR','AUS','01',NULL,1,1),('NOR','BHR','03',NULL,NULL,NULL),('NOR','CHN','02','08',NULL,1),('NOR','EMI','02',NULL,NULL,NULL),('NOR','JPN','02',NULL,NULL,NULL),('NOR','MIA','02','01',NULL,1),('NOR','SAU','04',NULL,NULL,1),('OCO','AUS','13',NULL,NULL,NULL),('OCO','BHR','08',NULL,NULL,NULL),('OCO','CHN','05',NULL,NULL,NULL),('OCO','EMI','Ret',NULL,NULL,NULL),('OCO','JPN','18',NULL,NULL,NULL),('OCO','MIA','12',NULL,NULL,NULL),('OCO','SAU','14',NULL,NULL,NULL),('PIA','AUS','09',NULL,NULL,NULL),('PIA','BHR','01',NULL,1,1),('PIA','CHN','01','02',1,NULL),('PIA','EMI','03',NULL,1,NULL),('PIA','JPN','03',NULL,NULL,NULL),('PIA','MIA','01','02',NULL,NULL),('PIA','SAU','01',NULL,NULL,NULL),('RUS','AUS','03',NULL,NULL,NULL),('RUS','BHR','02',NULL,NULL,NULL),('RUS','CHN','03','04',NULL,NULL),('RUS','EMI','07',NULL,NULL,NULL),('RUS','JPN','05',NULL,NULL,NULL),('RUS','MIA','03','04',NULL,NULL),('RUS','SAU','05',NULL,NULL,NULL),('SAI','AUS','Ret',NULL,NULL,NULL),('SAI','BHR','Ret',NULL,NULL,NULL),('SAI','CHN','10',NULL,NULL,NULL),('SAI','EMI','08',NULL,NULL,NULL),('SAI','JPN','14',NULL,NULL,NULL),('SAI','MIA','09',NULL,NULL,NULL),('SAI','SAU','08',NULL,NULL,NULL),('STR','AUS','06',NULL,NULL,NULL),('STR','BHR','17',NULL,NULL,NULL),('STR','CHN','09',NULL,NULL,NULL),('STR','EMI','15',NULL,NULL,NULL),('STR','JPN','20',NULL,NULL,NULL),('STR','MIA','16','05',NULL,NULL),('STR','SAU','16',NULL,NULL,NULL),('TSU','AUS','12',NULL,NULL,NULL),('TSU','BHR','09',NULL,NULL,NULL),('TSU','CHN','16','06',NULL,NULL),('TSU','EMI','10',NULL,NULL,NULL),('TSU','JPN','12',NULL,NULL,NULL),('TSU','MIA','10','06',NULL,NULL),('TSU','SAU','Ret',NULL,NULL,NULL),('VER','AUS','02',NULL,NULL,NULL),('VER','BHR','06',NULL,NULL,NULL),('VER','CHN','04','03',NULL,NULL),('VER','EMI','01',NULL,NULL,1),('VER','JPN','01',NULL,1,NULL),('VER','MIA','04',NULL,1,NULL),('VER','SAU','02',NULL,1,NULL);
/*!40000 ALTER TABLE `hasil_balapan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `klasemen`
--

DROP TABLE IF EXISTS `klasemen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `klasemen` (
  `kode_pembalap` varchar(3) NOT NULL,
  `poin` int(11) NOT NULL,
  `posisi_klasemen` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`kode_pembalap`),
  CONSTRAINT `klasemen_ibfk_1` FOREIGN KEY (`kode_pembalap`) REFERENCES `pembalap` (`kode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `klasemen`
--

LOCK TABLES `klasemen` WRITE;
/*!40000 ALTER TABLE `klasemen` DISABLE KEYS */;
INSERT INTO `klasemen` VALUES ('ALB',40,'08'),('ALO',0,'17'),('ANT',48,'07'),('BEA',6,'16'),('BOR',0,'20'),('COL',0,'21'),('DOO',0,'19'),('GAS',7,'13'),('HAD',7,'14'),('HAM',53,'06'),('HUL',6,'15'),('LAW',0,'18'),('LEC',61,'05'),('NOR',133,'02'),('OCO',14,'09'),('PIA',146,'01'),('RUS',99,'04'),('SAI',11,'11'),('STR',14,'10'),('TSU',10,'12'),('VER',124,'03');
/*!40000 ALTER TABLE `klasemen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pembalap`
--

DROP TABLE IF EXISTS `pembalap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pembalap` (
  `kode` varchar(3) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `judul` varchar(255) DEFAULT NULL,
  `nation` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`kode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pembalap`
--

LOCK TABLES `pembalap` WRITE;
/*!40000 ALTER TABLE `pembalap` DISABLE KEYS */;
INSERT INTO `pembalap` VALUES ('ALB','Alexander Albon',NULL,'THA'),('ALO','Fernando Alonso',NULL,'ESP'),('ANT','Andrea Kimi Antonelli',NULL,'ITA'),('BEA','Oliver Bearman',NULL,'GBR'),('BOR','Gabriel Bortoleto',NULL,'BRA'),('COL','Franco Colapinto',NULL,'ARG'),('DOO','Jack Doohan',NULL,'AUS'),('GAS','Pierre Gasly',NULL,'FRA'),('HAD','Isack Hadjar',NULL,'FRA'),('HAM','Lewis Hamilton',NULL,'GBR'),('HUL','Nico Hulkenberg',NULL,'DEU'),('LAW','Liam Lawson',NULL,'NZL'),('LEC','Charles Leclerc',NULL,'MON'),('NOR','Lando Norris',NULL,'GBR'),('OCO','Esteban Ocon',NULL,'FRA'),('PIA','Oscar Piastri',NULL,'AUS'),('RUS','George Russell','George Russell (pembalap)','GBR'),('SAI','Carlos Sainz Jr.',NULL,'ESP'),('STR','Lance Stroll',NULL,'CAN'),('TSU','Yuki Tsunoda',NULL,'JPN'),('VER','Max Verstappen',NULL,'NED');
/*!40000 ALTER TABLE `pembalap` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-24 21:18:46
