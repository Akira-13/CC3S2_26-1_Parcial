# Especificación de requisitos

## Requerimientos funcionales

- RF-01: El usuario debe poder presentar un texto detallando su incidencia de como máximo 1000 caracteres.

- RF-02: El usuario debe poder subir una imagen en formato JPG o PNG de como máximo 5MB junto a la información de incidencia que tenga.

- RF-03: El usuario debe poder ver todas las incidencias que se han reportado en un listado, junto a la evidencia adjuntada.

- RF-04: El usuario debe poder usar su DNI para escribir automáticamente sus datos de nombre, correo de contacto y teléfono.

## Requerimientos de usabilidad

- RU-01: El sistema debe presentar mensajes de error claros cuando el usuario exceda alguno de los límites puestos por seguridad.

- RU-02: El usuario debería poder presentar su queja o incidencia con un solo click.

## Requerimientos de rendimiento

- RR-1: La subida de incidencias y el mostrado de estas no debería demorar más de 100 milisegundos.

## Requerimientos de base de datos

- RBD-1: El sistema de base de datos deberá almacenar una tabla de ciudadanos solo de lectura y una tabla de incidencias de lectura y escritura.

- RBD-2: El sistema de base de datos deberá almacenar en la tabla de incidencias el nombre de la imagen adjuntada.