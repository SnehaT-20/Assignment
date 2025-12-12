-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: marketco
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `CompanyID` int(11) NOT NULL,
  `CompanyName` varchar(45) DEFAULT NULL,
  `Street` varchar(45) DEFAULT NULL,
  `City` varchar(45) DEFAULT NULL,
  `State` varchar(2) DEFAULT NULL,
  `Zip` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`CompanyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'Urban Outfitters','100 Market St','Philadelphia','PA','19103'),(2,'TechNova Solutions','55 Innovation Way','Austin','TX','78701'),(3,'BlueWave Marketing','820 Ocean Ave','Miami','FL','33101'),(4,'Toll Brothers','42 Garden Rd','Portland','OR','97201'),(5,'Summit Financial','200 Finance Blvd','Charlotte','NC','28202'),(6,'Silverline Media','19 Sunset Ln','Los Angeles','CA','90001'),(7,'RedPeak Sports','88 Mountain Dr','Denver','CO','80202'),(8,'PrimeSource Logistics','77 Distribution Ct','Memphis','TN','38103'),(9,'BrightSky Telecom','450 Connect Dr','Seattle','WA','98101'),(10,'DailyBean Coffee','12 Roast Rd','Chicago','IL','60601');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact` (
  `ContactID` int(11) NOT NULL,
  `CompanyID` int(11) DEFAULT NULL,
  `FirstName` varchar(45) DEFAULT NULL,
  `LastName` varchar(45) DEFAULT NULL,
  `Street` varchar(45) DEFAULT NULL,
  `City` varchar(45) DEFAULT NULL,
  `State` varchar(2) DEFAULT NULL,
  `Zip` varchar(10) DEFAULT NULL,
  `IsMain` tinyint(1) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Phone` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`ContactID`),
  KEY `CompanyID` (`CompanyID`),
  CONSTRAINT `contact_ibfk_1` FOREIGN KEY (`CompanyID`) REFERENCES `company` (`CompanyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact`
--

LOCK TABLES `contact` WRITE;
/*!40000 ALTER TABLE `contact` DISABLE KEYS */;
INSERT INTO `contact` VALUES (101,4,'Sophie','Miller','12 Walnut St','Philadelphia','PA','19103',NULL,'sophie.miller@uo.com','215-555-1001'),(102,2,'Eric','Johnson','77 Tech Ave','Austin','TX','78701',NULL,'eric.johnson@gmail.com','512-555-2211'),(103,3,'Michael','Green','8 Forest Ln','Portland','OR','97201',NULL,'m.green@gmail.com','503-555-8921'),(104,4,'Tom','Baker','200 Finance Blvd','Charlotte','NC','28202',NULL,'t.baker@gmail.com','704-555-0901'),(105,5,'Ana','Lopez','55 Ocean Dr','Miami','FL','33101',NULL,'ana.lopez@gmail.com','305-555-3212'),(106,6,'Raj','Singh','450 Connect Dr','Seattle','WA','98101',NULL,'raj.singh@gmail.com','206-555-9911'),(107,7,'James','Washington','30 Fabric Rd','New York','NY','10001',NULL,'j.washington@gmail.com','212-555-5301'),(108,8,'Lucas','Reed','88 Mountain Dr','Denver','CO','80202',NULL,'lucas.reed@gmail.com','720-555-1234'),(109,9,'Julia','Harris','19 Sunset Ln','Los Angeles','CA','90001',NULL,'j.harris@gmail.com','213-555-2211'),(110,10,'Dianne','Connor','8 Forest Ln','Portland','OR','97201',NULL,'c,dianne@gmail.com','213-555-2270');
/*!40000 ALTER TABLE `contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contactemployee`
--

DROP TABLE IF EXISTS `contactemployee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contactemployee` (
  `ContactEmployeeID` int(11) NOT NULL,
  `ContactID` int(11) DEFAULT NULL,
  `EmployeeID` int(11) DEFAULT NULL,
  `ContactDate` date DEFAULT NULL,
  `Description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ContactEmployeeID`),
  KEY `ContactID` (`ContactID`),
  KEY `EmployeeID` (`EmployeeID`),
  CONSTRAINT `contactemployee_ibfk_1` FOREIGN KEY (`ContactID`) REFERENCES `contact` (`ContactID`),
  CONSTRAINT `contactemployee_ibfk_2` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contactemployee`
--

LOCK TABLES `contactemployee` WRITE;
/*!40000 ALTER TABLE `contactemployee` DISABLE KEYS */;
INSERT INTO `contactemployee` VALUES (1,101,1003,'2024-01-12','Initial meeting'),(2,102,1001,'2024-01-15','Follow-up call'),(3,103,1004,'2024-02-10','Project discussion'),(4,104,1002,'2024-02-20','Quarterly review'),(5,105,1006,'2024-03-01','Financial consultation'),(6,106,1005,'2024-03-14','Marketing strategy'),(7,107,1008,'2024-03-19','Sales update'),(8,108,1007,'2024-04-02','Logistics planning'),(9,109,1004,'2024-04-11','Project discussio');
/*!40000 ALTER TABLE `contactemployee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `EmployeeID` int(11) NOT NULL,
  `FirstName` varchar(45) DEFAULT NULL,
  `LastName` varchar(45) DEFAULT NULL,
  `Salary` decimal(10,2) DEFAULT NULL,
  `HireDate` date DEFAULT NULL,
  `JobTitle` varchar(25) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Phone` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1001,'Lesley','Bland',70000.00,'2021-11-20','Data Analyst','lesley.bland@gmail.com','215-555-8800'),(1002,'Julia','Frost',40000.00,'2022-10-24','Data Scientist','julia.frost@gmail.com','215-555-1199'),(1003,'Daniel','Kim',50000.00,'2020-02-28','Software Engineer','daniel.kim@gmail.com','215-555-5500'),(1004,'Nina','Patel',60000.00,'2019-03-25','Developer','nina.patel@gmail.com','215-555-7822'),(1005,'Chris','Moris',30000.00,'2021-02-05','Tester','chris.moore@gmail.com','215-555-4401'),(1006,'Jenner','David',40000.00,'2018-10-10','Game developer','ian.davis@gmail.com','215-555-7766'),(1007,'Alex','Jordan',45000.00,'2022-06-15','Data Analyst','alex.jordan@gmail.com','215-555-9988'),(1008,'Tara','Jonas',65000.00,'2021-09-01','Data Scientist','tara.young@gmail.com','215-555-2344'),(1009,'Jack','Lee',55000.00,'2019-11-11','Developer','jack.young@gmail.com','215-555-6655');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-12 21:05:59
