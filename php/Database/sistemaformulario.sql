-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3307
-- Tiempo de generación: 18-10-2022 a las 18:35:04
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistemaformulario`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE `alumnos` (
  `CodAlumno` varchar(20) NOT NULL,
  `NombreAlumno` varchar(45) DEFAULT NULL,
  `ApellidoAlumno` varchar(45) DEFAULT NULL,
  `correo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `alumnos`
--

INSERT INTO `alumnos` (`CodAlumno`, `NombreAlumno`, `ApellidoAlumno`, `correo`) VALUES
('1', 'Renzo Arturo', 'Soles Contreras', 'renzoarturo12345@gmail.com'),
('2', 'Omar André', 'Cortijo Canaza', 'renzoarturo12345@gmail.com'),
('3', 'Carlos Daniel', 'Santisteban Torres', 'csantisteban@unitru.edu.pe'),
('4', 'Miguel', 'Castillo', 'renzoarturo12345@gmail.com'),
('5', 'Oscar', 'Contreras Silva', 'renzoarturo12345@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resultado_formulario`
--

CREATE TABLE `resultado_formulario` (
  `codAlumno` varchar(20) NOT NULL,
  `Pregunta1` int(11) DEFAULT NULL,
  `Pregunta2` int(11) DEFAULT NULL,
  `Pregunta3` int(11) DEFAULT NULL,
  `Pregunta4` int(11) DEFAULT NULL,
  `Pregunta5` int(11) DEFAULT NULL,
  `Pregunta6` int(11) NOT NULL,
  `Recomendacion` longtext NOT NULL,
  `promedio` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `resultado_formulario`
--

INSERT INTO `resultado_formulario` (`codAlumno`, `Pregunta1`, `Pregunta2`, `Pregunta3`, `Pregunta4`, `Pregunta5`, `Pregunta6`, `Recomendacion`, `promedio`) VALUES
('1', 5, 5, 5, 4, 4, 5, 'Recomendación', 4.66667),
('2', 5, 4, 5, 4, 5, 4, 'Recomendación', 4.5),
('4', 1, 2, 3, 4, 5, 4, 'Prueba de recomendación', 3.16667);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`CodAlumno`);

--
-- Indices de la tabla `resultado_formulario`
--
ALTER TABLE `resultado_formulario`
  ADD PRIMARY KEY (`codAlumno`),
  ADD KEY `ResultadoAlumno_idx` (`codAlumno`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `resultado_formulario`
--
ALTER TABLE `resultado_formulario`
  ADD CONSTRAINT `ResultadoAlumno` FOREIGN KEY (`codAlumno`) REFERENCES `alumnos` (`CodAlumno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
