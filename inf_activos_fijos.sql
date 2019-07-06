DROP SCHEMA IF EXISTS inf_Activos_Fijos;

CREATE SCHEMA inf_Activos_Fijos;
use inf_Activos_Fijos;

CREATE TABLE `departamentos` (
`id_departamento` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
`dep_descripcion` VARCHAR(60) NOT NULL DEFAULT '',
`dep_estado` VARCHAR(30) NOT NULL DEFAULT 'Activo'
);

CREATE TABLE `tipo_activos` (
`id_tipo_activo` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
`ta_descripcion` VARCHAR(60) NOT NULL DEFAULT '',
`ta_CCCompra` int NOT NULL,
`ta_CCDepreciacion` int NOT NULL,
`ta_estado` VARCHAR(30) NOT NULL DEFAULT 'Activo'
);

CREATE TABLE `empleados` (
`id_empleado` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
`emp_nombre` VARCHAR(30) NOT NULL,
`emp_cedula` VARCHAR(13) NOT NULL,
`id_departamento` int NOT NULL, 
FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento),
`emp_tipo_persona` VARCHAR(10) NOT NULL DEFAULT 'Fisica',
`emp_fecha_ingreso` date NOT NULL,
`emp_estado` VARCHAR(30) NOT NULL DEFAULT 'Activo'
);

CREATE TABLE `activos_fijos` (
`id_activos_fijos` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
`act_descripcion` VARCHAR(60) NOT NULL,
`id_departamento` int NOT NULL, 
FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento),
`id_tipo_activo` int NOT NULL,
FOREIGN KEY (id_tipo_activo) REFERENCES tipo_activos(id_tipo_activo),
`act_fecha_registro` date NOT NULL,
`act_valor_compra` DECIMAL NOT NULL,
`act_depreciacion_acumulada` DECIMAL NOT NULL
);

CREATE TABLE `calculo_depreciacion` (
`id_registro` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
`cd_ano_proceso` YEAR NOT NULL,
`cd_mes_proceso` VARCHAR(15) NOT NULL,
`id_activos_fijos` int NOT NULL,
FOREIGN KEY (id_activos_fijos) REFERENCES activos_fijos(id_activos_fijos),
`cd_fecha_proceso` date NOT NULL,
`cd_monto_depreciado` DECIMAL NOT NULL,
`cd_depreciacion_acumulada` DECIMAL NOT NULL,
`cd_cuenta_compra` VARCHAR(30) NOT NULL,
`cd_cuenta_depreciacion` VARCHAR(30) NOT NULL
);

CREATE TABLE `asientos_contables` (
`id_asiento` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
`ac_descripcion` VARCHAR(60) NOT NULL,
`ac_tipo_inventario` VARCHAR(30) NOT NULL,
`ac_cuenta_contable` VARCHAR(30) NOT NULL,
`ac_tipo_movimiento` VARCHAR(20) NOT NULL,
`ac_fecha_asiento` date NOT NULL,
`ac_monto_asiento` DECIMAL NOT NULL,
`ac_estado` VARCHAR(30) NOT NULL DEFAULT 'Activo'
);