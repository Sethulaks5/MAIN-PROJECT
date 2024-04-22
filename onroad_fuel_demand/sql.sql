/*
SQLyog Community
MySQL - 10.4.25-MariaDB : Database - django_onroad_fuels
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`django_onroad_fuels` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `django_onroad_fuels`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add bookings',7,'add_bookings'),
(26,'Can change bookings',7,'change_bookings'),
(27,'Can delete bookings',7,'delete_bookings'),
(28,'Can view bookings',7,'view_bookings'),
(29,'Can add fuel_type',8,'add_fuel_type'),
(30,'Can change fuel_type',8,'change_fuel_type'),
(31,'Can delete fuel_type',8,'delete_fuel_type'),
(32,'Can view fuel_type',8,'view_fuel_type'),
(33,'Can add tbl_login',9,'add_tbl_login'),
(34,'Can change tbl_login',9,'change_tbl_login'),
(35,'Can delete tbl_login',9,'delete_tbl_login'),
(36,'Can view tbl_login',9,'view_tbl_login'),
(37,'Can add vehicles',10,'add_vehicles'),
(38,'Can change vehicles',10,'change_vehicles'),
(39,'Can delete vehicles',10,'delete_vehicles'),
(40,'Can view vehicles',10,'view_vehicles'),
(41,'Can add users',11,'add_users'),
(42,'Can change users',11,'change_users'),
(43,'Can delete users',11,'delete_users'),
(44,'Can view users',11,'view_users'),
(45,'Can add stocks',12,'add_stocks'),
(46,'Can change stocks',12,'change_stocks'),
(47,'Can delete stocks',12,'delete_stocks'),
(48,'Can view stocks',12,'view_stocks'),
(49,'Can add rating',13,'add_rating'),
(50,'Can change rating',13,'change_rating'),
(51,'Can delete rating',13,'delete_rating'),
(52,'Can view rating',13,'view_rating'),
(53,'Can add payments',14,'add_payments'),
(54,'Can change payments',14,'change_payments'),
(55,'Can delete payments',14,'delete_payments'),
(56,'Can view payments',14,'view_payments'),
(57,'Can add drivers',15,'add_drivers'),
(58,'Can change drivers',15,'change_drivers'),
(59,'Can delete drivers',15,'delete_drivers'),
(60,'Can view drivers',15,'view_drivers'),
(61,'Can add complaints',16,'add_complaints'),
(62,'Can change complaints',16,'change_complaints'),
(63,'Can delete complaints',16,'delete_complaints'),
(64,'Can view complaints',16,'view_complaints'),
(65,'Can add assign_vehicle',17,'add_assign_vehicle'),
(66,'Can change assign_vehicle',17,'change_assign_vehicle'),
(67,'Can delete assign_vehicle',17,'delete_assign_vehicle'),
(68,'Can view assign_vehicle',17,'view_assign_vehicle');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(17,'onroad','assign_vehicle'),
(7,'onroad','bookings'),
(16,'onroad','complaints'),
(15,'onroad','drivers'),
(8,'onroad','fuel_type'),
(14,'onroad','payments'),
(13,'onroad','rating'),
(12,'onroad','stocks'),
(9,'onroad','tbl_login'),
(11,'onroad','users'),
(10,'onroad','vehicles'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-06-02 04:46:56.924321'),
(2,'auth','0001_initial','2023-06-02 04:46:57.706872'),
(3,'admin','0001_initial','2023-06-02 04:46:57.911754'),
(4,'admin','0002_logentry_remove_auto_add','2023-06-02 04:46:58.110641'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-06-02 04:46:58.165610'),
(6,'contenttypes','0002_remove_content_type_name','2023-06-02 04:46:58.331514'),
(7,'auth','0002_alter_permission_name_max_length','2023-06-02 04:46:58.394479'),
(8,'auth','0003_alter_user_email_max_length','2023-06-02 04:46:58.430458'),
(9,'auth','0004_alter_user_username_opts','2023-06-02 04:46:58.448448'),
(10,'auth','0005_alter_user_last_login_null','2023-06-02 04:46:58.543394'),
(11,'auth','0006_require_contenttypes_0002','2023-06-02 04:46:58.548390'),
(12,'auth','0007_alter_validators_add_error_messages','2023-06-02 04:46:58.571377'),
(13,'auth','0008_alter_user_username_max_length','2023-06-02 04:46:58.607357'),
(14,'auth','0009_alter_user_last_name_max_length','2023-06-02 04:46:58.650332'),
(15,'auth','0010_alter_group_name_max_length','2023-06-02 04:46:58.712296'),
(16,'auth','0011_update_proxy_permissions','2023-06-02 04:46:58.731286'),
(17,'auth','0012_alter_user_first_name_max_length','2023-06-02 04:46:58.772264'),
(18,'onroad','0001_initial','2023-06-02 04:47:00.250416'),
(19,'sessions','0001_initial','2023-06-02 04:47:00.318377');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('gpurga91r6l7jg8oxlqo1e39kl7n4qkh','eyJpZCI6MX0:1q8ucH:o0UjV0nURiR6d0GFez2pBrPJB4qlg2i6WMfELYzDZNo','2023-06-27 03:22:45.726853'),
('tpu8b92kgo9878ayibpfdidoksggeu2p','eyJpZCI6MX0:1qJS2o:B-F62Sm2GosE-8q4LnmT9aVC1DtHPhCPBDO3LzbmauQ','2023-07-26 05:05:42.331359'),
('zdx9rf40zfb6svr0gv1fs9k0zdvrbf3d','eyJpZCI6MX0:1qJSn8:qI4r0p8IRmjryxD3bQ6QOW5HyEQ1PtktDRefNqGFPYs','2023-07-26 05:53:34.400268');

/*Table structure for table `onroad_assign_vehicle` */

DROP TABLE IF EXISTS `onroad_assign_vehicle`;

CREATE TABLE `onroad_assign_vehicle` (
  `assign_vehicle_id` int(11) NOT NULL AUTO_INCREMENT,
  `latitude` varchar(100) NOT NULL,
  `longitude` varchar(100) NOT NULL,
  `driver_id` int(11) NOT NULL,
  `vehicles_id` int(11) NOT NULL,
  PRIMARY KEY (`assign_vehicle_id`),
  KEY `onroad_assign_vehicl_driver_id_568d3ecb_fk_onroad_dr` (`driver_id`),
  KEY `onroad_assign_vehicl_vehicles_id_77a99735_fk_onroad_ve` (`vehicles_id`),
  CONSTRAINT `onroad_assign_vehicl_driver_id_568d3ecb_fk_onroad_dr` FOREIGN KEY (`driver_id`) REFERENCES `onroad_drivers` (`driver_id`),
  CONSTRAINT `onroad_assign_vehicl_vehicles_id_77a99735_fk_onroad_ve` FOREIGN KEY (`vehicles_id`) REFERENCES `onroad_vehicles` (`vehicles_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `onroad_assign_vehicle` */

insert  into `onroad_assign_vehicle`(`assign_vehicle_id`,`latitude`,`longitude`,`driver_id`,`vehicles_id`) values 
(1,'9.977980240986346','76.28305435180664',1,1);

/*Table structure for table `onroad_bookings` */

DROP TABLE IF EXISTS `onroad_bookings`;

CREATE TABLE `onroad_bookings` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `no_of_litter` varchar(100) NOT NULL,
  `booking_amount` varchar(100) NOT NULL,
  `booking_datetime` varchar(100) NOT NULL,
  `booking_status` varchar(100) NOT NULL,
  `driver_id` int(11) NOT NULL,
  `fuel_type_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `onroad_bookings_driver_id_311fe769_fk_onroad_drivers_driver_id` (`driver_id`),
  KEY `onroad_bookings_fuel_type_id_8ed9a53f_fk_onroad_fu` (`fuel_type_id`),
  KEY `onroad_bookings_user_id_a813774a_fk_onroad_users_user_id` (`user_id`),
  CONSTRAINT `onroad_bookings_driver_id_311fe769_fk_onroad_drivers_driver_id` FOREIGN KEY (`driver_id`) REFERENCES `onroad_drivers` (`driver_id`),
  CONSTRAINT `onroad_bookings_fuel_type_id_8ed9a53f_fk_onroad_fu` FOREIGN KEY (`fuel_type_id`) REFERENCES `onroad_fuel_type` (`fuel_type_id`),
  CONSTRAINT `onroad_bookings_user_id_a813774a_fk_onroad_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `onroad_users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `onroad_bookings` */

insert  into `onroad_bookings`(`booking_id`,`no_of_litter`,`booking_amount`,`booking_datetime`,`booking_status`,`driver_id`,`fuel_type_id`,`user_id`) values 
(5,'2','45.0','','pending',1,1,1);

/*Table structure for table `onroad_complaints` */

DROP TABLE IF EXISTS `onroad_complaints`;

CREATE TABLE `onroad_complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `com_date` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`complaint_id`),
  KEY `onroad_complaints_user_id_1a5d9f1a_fk_onroad_users_user_id` (`user_id`),
  CONSTRAINT `onroad_complaints_user_id_1a5d9f1a_fk_onroad_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `onroad_users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `onroad_complaints` */

insert  into `onroad_complaints`(`complaint_id`,`complaint`,`reply`,`com_date`,`user_id`) values 
(7,'Gghhhggy','asjhsd','2023-06-03',1),
(8,' Gvyh7y7ycyfgyf','hcxbshdcb','2023-06-03',1),
(9,'Gggg','pending','2023-07-12',1);

/*Table structure for table `onroad_drivers` */

DROP TABLE IF EXISTS `onroad_drivers`;

CREATE TABLE `onroad_drivers` (
  `driver_id` int(11) NOT NULL AUTO_INCREMENT,
  `d_first_name` varchar(100) NOT NULL,
  `d_last_name` varchar(100) NOT NULL,
  `d_phone` varchar(100) NOT NULL,
  `d_email` varchar(100) NOT NULL,
  `d_licence` varchar(100) NOT NULL,
  `login_id` int(11) NOT NULL,
  PRIMARY KEY (`driver_id`),
  KEY `onroad_drivers_login_id_3dea1308_fk_onroad_tbl_login_login_id` (`login_id`),
  CONSTRAINT `onroad_drivers_login_id_3dea1308_fk_onroad_tbl_login_login_id` FOREIGN KEY (`login_id`) REFERENCES `onroad_tbl_login` (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `onroad_drivers` */

insert  into `onroad_drivers`(`driver_id`,`d_first_name`,`d_last_name`,`d_phone`,`d_email`,`d_licence`,`login_id`) values 
(1,'arun','a','9874561230','ar@gmail.com','1254',2);

/*Table structure for table `onroad_fuel_type` */

DROP TABLE IF EXISTS `onroad_fuel_type`;

CREATE TABLE `onroad_fuel_type` (
  `fuel_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `fuel_type_name` varchar(100) NOT NULL,
  `fuel_type_rate` varchar(100) NOT NULL,
  `fuel_type_datetime` varchar(100) NOT NULL,
  PRIMARY KEY (`fuel_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `onroad_fuel_type` */

insert  into `onroad_fuel_type`(`fuel_type_id`,`fuel_type_name`,`fuel_type_rate`,`fuel_type_datetime`) values 
(1,'petrol','22.50','2023-06-02 04:50:29.789632+00:00'),
(2,'xxx','55','2023-07-12 05:51:22.887258+00:00');

/*Table structure for table `onroad_payments` */

DROP TABLE IF EXISTS `onroad_payments`;

CREATE TABLE `onroad_payments` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `payment_datetime` varchar(100) NOT NULL,
  `booking_id` int(11) NOT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `onroad_payments_booking_id_30101df5_fk_onroad_bo` (`booking_id`),
  CONSTRAINT `onroad_payments_booking_id_30101df5_fk_onroad_bo` FOREIGN KEY (`booking_id`) REFERENCES `onroad_bookings` (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `onroad_payments` */

/*Table structure for table `onroad_rating` */

DROP TABLE IF EXISTS `onroad_rating`;

CREATE TABLE `onroad_rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` varchar(100) NOT NULL,
  `rating_datetime` varchar(100) NOT NULL,
  `booking_id` int(11) NOT NULL,
  PRIMARY KEY (`rating_id`),
  KEY `onroad_rating_booking_id_60f782af_fk_onroad_bookings_booking_id` (`booking_id`),
  CONSTRAINT `onroad_rating_booking_id_60f782af_fk_onroad_bookings_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `onroad_bookings` (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `onroad_rating` */

/*Table structure for table `onroad_stocks` */

DROP TABLE IF EXISTS `onroad_stocks`;

CREATE TABLE `onroad_stocks` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `fuel_stock` varchar(100) NOT NULL,
  `stock_datetime` varchar(100) NOT NULL,
  `vehicle_id` int(11) NOT NULL,
  PRIMARY KEY (`stock_id`),
  KEY `onroad_stocks_vehicle_id_f87df9aa_fk_onroad_vehicles_vehicles_id` (`vehicle_id`),
  CONSTRAINT `onroad_stocks_vehicle_id_f87df9aa_fk_onroad_vehicles_vehicles_id` FOREIGN KEY (`vehicle_id`) REFERENCES `onroad_vehicles` (`vehicles_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `onroad_stocks` */

insert  into `onroad_stocks`(`stock_id`,`fuel_stock`,`stock_datetime`,`vehicle_id`) values 
(1,'1218','2023-06-02 04:52:20.833817+00:00',1);

/*Table structure for table `onroad_tbl_login` */

DROP TABLE IF EXISTS `onroad_tbl_login`;

CREATE TABLE `onroad_tbl_login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `user_type` varchar(100) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `onroad_tbl_login` */

insert  into `onroad_tbl_login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'d','d','driver'),
(3,'U','u','user'),
(4,'ann','ann','user');

/*Table structure for table `onroad_users` */

DROP TABLE IF EXISTS `onroad_users`;

CREATE TABLE `onroad_users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_first_name` varchar(100) NOT NULL,
  `u_last_name` varchar(100) NOT NULL,
  `u_phone` varchar(100) NOT NULL,
  `u_email` varchar(100) NOT NULL,
  `u_licence` varchar(100) NOT NULL,
  `u_latitude` varchar(100) NOT NULL,
  `u_longitude` varchar(100) NOT NULL,
  `login_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `onroad_users_login_id_acb64f9c_fk_onroad_tbl_login_login_id` (`login_id`),
  CONSTRAINT `onroad_users_login_id_acb64f9c_fk_onroad_tbl_login_login_id` FOREIGN KEY (`login_id`) REFERENCES `onroad_tbl_login` (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `onroad_users` */

insert  into `onroad_users`(`user_id`,`u_first_name`,`u_last_name`,`u_phone`,`u_email`,`u_licence`,`u_latitude`,`u_longitude`,`login_id`) values 
(1,'Akash','Philip','9463682245','akash.edva@gmail.com','12','9.9762903','76.2862192',3),
(2,'anu','n','9874561230','davidphotogallery7@gmail.com','565','','',4);

/*Table structure for table `onroad_vehicles` */

DROP TABLE IF EXISTS `onroad_vehicles`;

CREATE TABLE `onroad_vehicles` (
  `vehicles_id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicles_reg_no` varchar(100) NOT NULL,
  `vehicles_name` varchar(100) NOT NULL,
  `vehicles_capacity` varchar(100) NOT NULL,
  `fuel_type_id` int(11) NOT NULL,
  PRIMARY KEY (`vehicles_id`),
  KEY `onroad_vehicles_fuel_type_id_7cbdc000_fk_onroad_fu` (`fuel_type_id`),
  CONSTRAINT `onroad_vehicles_fuel_type_id_7cbdc000_fk_onroad_fu` FOREIGN KEY (`fuel_type_id`) REFERENCES `onroad_fuel_type` (`fuel_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `onroad_vehicles` */

insert  into `onroad_vehicles`(`vehicles_id`,`vehicles_reg_no`,`vehicles_name`,`vehicles_capacity`,`fuel_type_id`) values 
(1,'kl 32 b ','car','8',1),
(2,'kl 32 b ','car','8',1),
(3,'kl 32 b ','car','8',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
