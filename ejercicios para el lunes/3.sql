CREATE TABLE empleados (
  cedula INT PRIMARY KEY,
  nombre VARCHAR(100),
  apellido VARCHAR(100),
  salario INT(50),
  edad INT(50)
);

INSERT INTO empleados
(cedula, nombre, apellido, salario, edad)
VALUES
(33456123, 'Ana', 'Bermudez', 300, 50),
(12787711, 'Orlando', 'Gutierrez', 1200, 38),
(20775612, 'Maximiliano', 'Torres', 3000, 22);

SELECT nombre, apellido, salario
FROM empleados
WHERE salario > 1000;

UPDATE empleados
SET salario = salario * 1.10
WHERE cedula = 12787711; 

DELETE FROM empleados
WHERE edad > 40;

SELECT nombre, apellido, salario
FROM empleados
ORDER BY salario DESC
LIMIT 5;