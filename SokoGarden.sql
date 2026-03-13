-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 13, 2026 at 09:39 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `SokoGarden`
--

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_description` text DEFAULT NULL,
  `product_cost` int(11) DEFAULT NULL,
  `product_photo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`product_id`, `product_name`, `product_description`, `product_cost`, `product_photo`) VALUES
(2, 'tecno', 'brand new', 100000, 'phone1.jpg'),
(3, 'samsung', 'brand new', 150000, 'samsung galaxy S20.jpeg'),
(6, 'lenovo', 'brand new', 1500000, 'lenovo.jpeg'),
(7, 'Itel', 'high quality', 45000, 'Itel-A70.webp'),
(8, 'oppo', 'high quality', 28000, 'oppo A77s.png'),
(9, 'i-phone', 'high quality', 68000, 'i-phone.jpeg'),
(10, 'Gaming-laptop', 'brand new', 1500000, 'Gaming laptop.jpg'),
(11, 'Nokia', 'high quality screen', 34000, 'Nokia2.jpg'),
(12, 'oale', 'brand new', 24000, 'oale.jpeg'),
(13, 'Touch screen-desktop', 'smart-touch brand new', 1500000, 'Touch screen desktop computer.jpg'),
(14, 'headphones', 'Hybrid active', 4500, 'headphones. V.jpg'),
(15, 'headphones', 'Slim digital edition', 75000, 'ps 5.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `passwrd` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `passwrd`, `email`, `phone`) VALUES
(1, 'john', '1234', 'john10@gmail.com', '0700112233'),
(3, 'Alex', '5555', 'Alex10@gmail.com', '0722531648'),
(4, 'Bobby Wine', '1212', 'BobbyWine11@gmail.com', '0752531648'),
(5, 'Vincent', '2222', 'Vincent23@gmail.com', '0724531648');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product_details`
--
ALTER TABLE `product_details`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
