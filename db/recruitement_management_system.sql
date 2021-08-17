-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 30, 2021 at 02:37 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recruitement_management_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `applicant`
--

CREATE TABLE `applicant` (
  `s_no` int(11) NOT NULL,
  `name` text NOT NULL,
  `username` text NOT NULL,
  `jobIdentity` text NOT NULL,
  `contact` text NOT NULL,
  `resumeFile` text NOT NULL,
  `applicant_state` text NOT NULL,
  `transfer_status` text NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `applicant`
--

INSERT INTO `applicant` (`s_no`, `name`, `username`, `jobIdentity`, `contact`, `resumeFile`, `applicant_state`, `transfer_status`, `date`) VALUES
(6, 'Mohammad Sufiyan', 'mdsufiyanidrisi786@gmail.com', '9', '7738771175', 'mdsufiya_9_2021-04-30.pdf', '1', '-1', '2021-04-30'),
(7, 'Mohammad Sufiyan', 'mdsufiyanidrisi786@gmail.com', '11', '8097958131', 'mdsufiya_11_2021-04-30.pdf', '0', '-3', '2021-04-30');

-- --------------------------------------------------------

--
-- Table structure for table `job_details`
--

CREATE TABLE `job_details` (
  `job_id` int(11) NOT NULL,
  `company_name` text DEFAULT NULL,
  `name_of_job` text NOT NULL,
  `location` text NOT NULL,
  `start_date` text DEFAULT NULL,
  `CTC` text DEFAULT NULL,
  `apply_by` date DEFAULT NULL,
  `experience` text NOT NULL,
  `applicant` text DEFAULT NULL,
  `about_the_job` text NOT NULL,
  `skill_required` text NOT NULL,
  `who_can_apply` text NOT NULL,
  `num_of_opening` text NOT NULL,
  `job_status` text NOT NULL,
  `slug` text NOT NULL,
  `img` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `job_details`
--

INSERT INTO `job_details` (`job_id`, `company_name`, `name_of_job`, `location`, `start_date`, `CTC`, `apply_by`, `experience`, `applicant`, `about_the_job`, `skill_required`, `who_can_apply`, `num_of_opening`, `job_status`, `slug`, `img`) VALUES
(9, 'Tata consultancy', 'Fronend developer', 'Byculla', 'Immediatly', '15L', '2021-07-23', 'Freshser', '23', '                                                front end web developers use three primary coding languages to code the website and web app designs created by web designers:\r\n\r\nhtml\r\ncss\r\njavascript\r\nthe code they write runs inside the user’s browser (as opposed to a back end developer, whose code runs on the web server). think of it a little like this: the back end developer is like the engineer who designs and creates the systems that make a city work (electricity, water and sewer, zoning, etc.), while the front end developer is the one who lays out the streets and makes sure everything is connected properly so people can live their lives (a simplified analogy, but you get the rough idea). a front end web developer is also in charge of making sure that there are no errors or bugs on the front end, as well as making sure that the design appears as it’s supposed to across various platforms and browsers.\r\n\r\ni’ve combed through dozens of front end web developer job listings to see which skills are the most in-demand right now. these are the things that real employers are looking for in job applicants today (and will still be looking for in the near future). master these things and you’re certain to land an awesome front end dev job!          \r\n                       \r\n                       \r\n                       ', 'html,css,js,bootsrap', 'Now you might be wondering that what front-end developer actually does? okay, a front-end developer is responsible for the development of the user interface of the website. in general, front-end developers works on the design & layout aspects of the websites alike back-end developers who are responsible for server-side processes such as database management, api integration, etc. a front-end developer is also concerned with the implementation \r\n                    ', '10', 'opend', 'tata-consult', 'tata-consult_2021-04-30.png'),
(10, 'Vipro', 'Back-end developer', 'Thane', 'Immediatly', '32L', '2021-06-12', 'Freshser', '23', 'A back-end web developer is responsible for server-side web application logic and integration of the work front-end developers do. back-end developers are usually write the web services and apis used by front-end developers and mobile application developers.                        \r\n      ', 'php,mysql,nodejs,mongodb,expressjs', 'Back-end developers work hand-in-hand with front-end developers by providing the outward facing web application elements server-side logic. in other words, back-end developers create the logic to make the web app function properly, and they accomplish this through the use of server-side scripting languages like ruby or php.\r\n\r\naside from making web applications functional, back-end developers are also responsible for optimizing the application for speed and efficiency. moreover, back-end developers often create a data storage solution with a database, which is a crucial component for all web applications since it stores information (like users, comments, posts, etc.). common databases include mysql, mongodb, and postgresql.\r\n                    ', '20', 'opend', 'vipro', 'vipro_2021-04-30.jpg'),
(11, 'Micro soft', 'Android developer', 'Dadar', 'Immediatly', '60L', '2021-05-09', 'Well experience', '20', 'Back-end developers work hand-in-hand with front-end developers by providing the outward facing web application elements server-side logic. in other words, back-end developers create the logic to make the web app function properly, and they accomplish this through the use of server-side scripting languages like ruby or php.\r\n\r\naside from making web applications functional, back-end developers are also responsible for optimizing the application for speed and efficiency. moreover, back-end developers often create a data storage solution with a database, which is a crucial component for all web applications since it stores information (like users, comments, posts, etc.). common databases include mysql, mongodb, and postgresql.       ', 'java,xml,dart,android studio,flutter', 'Back-end developers work hand-in-hand with front-end developers by providing the outward facing web application elements server-side logic. in other words, back-end developers create the logic to make the web app function properly, and they accomplish this through the use of server-side scripting languages like ruby or php.\r\n\r\naside from making web applications functional, back-end developers are also responsible for optimizing the application for speed and efficiency. moreover, back-end developers often create a data storage solution with a database, which is a crucial component for all web applications since it stores information (like users, comments, posts, etc.). common databases include mysql, mongodb, and postgresql.', '40', 'opend', 'micro-soft', 'micro-soft_2021-04-30.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`sno`, `name`, `email`, `password`) VALUES
(5, 'Mohammad Sufiyan', 'mdsufiyanidrisi786@gmail.com', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `applicant`
--
ALTER TABLE `applicant`
  ADD PRIMARY KEY (`s_no`);

--
-- Indexes for table `job_details`
--
ALTER TABLE `job_details`
  ADD PRIMARY KEY (`job_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `applicant`
--
ALTER TABLE `applicant`
  MODIFY `s_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `job_details`
--
ALTER TABLE `job_details`
  MODIFY `job_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
