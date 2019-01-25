-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 05, 2017 at 06:24 PM
-- Server version: 10.1.26-MariaDB
-- PHP Version: 7.1.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ClgMgmt`
--
CREATE DATABASE IF NOT EXISTS `ClgMgmt` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `ClgMgmt`;

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
CREATE TABLE `attendance` (
  `rollNo` bigint(20) UNSIGNED NOT NULL,
  `jan` int(11) NOT NULL DEFAULT '-1',
  `feb` int(11) NOT NULL DEFAULT '-1',
  `mar` int(11) NOT NULL DEFAULT '-1',
  `apr` int(11) NOT NULL DEFAULT '-1',
  `may` int(11) NOT NULL DEFAULT '-1',
  `jun` int(11) NOT NULL DEFAULT '-1',
  `jul` int(11) NOT NULL DEFAULT '-1',
  `aug` int(11) NOT NULL DEFAULT '-1',
  `sept` int(11) NOT NULL DEFAULT '-1',
  `oct` int(11) NOT NULL DEFAULT '-1',
  `nov` int(11) NOT NULL DEFAULT '-1',
  `december` int(11) NOT NULL DEFAULT '-1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`rollNo`, `jan`, `feb`, `mar`, `apr`, `may`, `jun`, `jul`, `aug`, `sept`, `oct`, `nov`, `december`) VALUES
(30, 50, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1);

-- --------------------------------------------------------

--
-- Table structure for table `parents`
--

DROP TABLE IF EXISTS `parents`;
CREATE TABLE `parents` (
  `rollNo` bigint(20) UNSIGNED NOT NULL DEFAULT '0',
  `name` text NOT NULL,
  `phone` text NOT NULL,
  `mail` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `parents`
--

INSERT INTO `parents` (`rollNo`, `name`, `phone`, `mail`) VALUES
(30, 'XYZ', '901901', 'ABC@XYZ');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `rollNo` bigint(20) UNSIGNED NOT NULL,
  `name` text NOT NULL,
  `dob` text NOT NULL,
  `addr` text NOT NULL,
  `phone` text NOT NULL,
  `mail` text NOT NULL,
  `dept` text NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`rollNo`, `name`, `dob`, `addr`, `phone`, `mail`, `dept`, `batch`) VALUES
(30, 'Sunny Soni', '1997', 'delhi', '989898', 'abc@xyz', 'cse', 2021);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`rollNo`),
  ADD UNIQUE KEY `rollNo` (`rollNo`);

--
-- Indexes for table `parents`
--
ALTER TABLE `parents`
  ADD PRIMARY KEY (`rollNo`),
  ADD UNIQUE KEY `rollNo` (`rollNo`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`rollNo`),
  ADD UNIQUE KEY `rollNo` (`rollNo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `rollNo` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
