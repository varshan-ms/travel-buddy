-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 18, 2024 at 07:45 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `2traveldbpy`
--

-- --------------------------------------------------------

--
-- Table structure for table `booktb`
--

CREATE TABLE `booktb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `Bookid` varchar(250) NOT NULL,
  `Qty` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `CardName` varchar(250) NOT NULL,
  `CardNo` varchar(250) NOT NULL,
  `CvNo` varchar(250) NOT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `booktb`
--

INSERT INTO `booktb` (`id`, `UserName`, `Bookid`, `Qty`, `Amount`, `CardName`, `CardNo`, `CvNo`, `Date`) VALUES
(1, 'san', 'BOOKID1', '2.00', '122.00', 'MASTERCARD', '1245236347457856', '123', '2023-04-09'),
(2, 'san123', 'BOOKID2', '4.00', '204.00', 'MASTERCARD', '1254236324645756', '123', '2023-04-09');

-- --------------------------------------------------------

--
-- Table structure for table `carttb`
--

CREATE TABLE `carttb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `ProductType` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `Qty` decimal(18,2) NOT NULL,
  `Tprice` decimal(28,2) NOT NULL,
  `Image` varchar(500) NOT NULL,
  `Date` date NOT NULL,
  `Status` varchar(250) NOT NULL,
  `Bookid` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `carttb`
--

INSERT INTO `carttb` (`id`, `UserName`, `ProductName`, `ProductType`, `Price`, `Qty`, `Tprice`, `Image`, `Date`, `Status`, `Bookid`) VALUES
(1, 'san', 'briyani', 'Non-Veg', '120', '2.00', '122.00', '2540.png', '2023-04-09', '1', 'BOOKID1'),
(2, 'san123', 'briyani', 'Non-Veg', '120', '2.00', '122.00', '6850.png', '2023-04-09', '1', 'BOOKID2'),
(3, 'san123', 'edli', 'Veg', '80', '2.00', '82.00', '4740.png', '2023-04-09', '1', 'BOOKID2');

-- --------------------------------------------------------

--
-- Table structure for table `employeetb`
--

CREATE TABLE `employeetb` (
  `Name` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employeetb`
--

INSERT INTO `employeetb` (`Name`, `Email`, `Mobile`, `Address`, `UserName`, `Password`, `Gender`) VALUES
('sangeeth Kumar', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san', 'Male'),
('logesh', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'logesh', 'logesh', 'Male'),
('loges', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'loges', 'loges', 'Male');

-- --------------------------------------------------------

--
-- Table structure for table `packagetb`
--

CREATE TABLE `packagetb` (
  `id` bigint(10) NOT NULL auto_increment,
  `RoomNo` varchar(250) NOT NULL,
  `RoomType` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `MaxPerson` varchar(250) NOT NULL,
  `info` varchar(500) NOT NULL,
  `Image` varchar(500) NOT NULL,
  `Source` varchar(500) NOT NULL,
  `Destination` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `packagetb`
--

INSERT INTO `packagetb` (`id`, `RoomNo`, `RoomType`, `Price`, `MaxPerson`, `info`, `Image`, `Source`, `Destination`) VALUES
(3, 'golden', 'International', '90000', '5', 'safasf', '5343.png', 'trichy', 'us');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `Name` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`Name`, `Email`, `Mobile`, `Address`, `UserName`, `Password`, `Gender`) VALUES
('sangeeth Kumar', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'sangeeth', 'sangeeth', 'Male'),
('sangeeth Kumar', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san', 'Male'),
('logesh', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'logesh', 'logesh', 'Male'),
('sangeeth Kumar', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san123', 'san123', 'Male');
