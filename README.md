# python-mysql
#ejemplo de conexión a mysql.
# se deben crear una base de datos llamada "python" y en ella una tabla llamada "usuarios".
#existen dos funciones operativas, la de crear usuarios y la de borrar por rut.

#script para crear la tabla usuarios:

CREATE TABLE `usuarios` (
  `nombre` varchar(20) DEFAULT NULL,
  `apepat` varchar(20) DEFAULT NULL,
  `apemat` varchar(20) DEFAULT NULL,
  `rut` varchar(10) NOT NULL,
  `edad` int DEFAULT NULL,
  `sede` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`rut`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
