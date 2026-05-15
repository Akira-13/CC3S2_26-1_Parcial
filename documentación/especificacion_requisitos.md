Implemente los requisitos del software, la arquitectura, de 3 casos de uso o historias de usuario necesarios para un proyeccto que implemente un registro de incidencias (baches, alumbrado, basura, seguridad ciudadana o emergencia) en la vía pública.
Puede utilizar el modelo gitflow para implemetar el backend y el front end. Define un escenario. Implementar Base de datos y el uso de API.

Puede usar el flujo de trabajo (Workflow) considerado estádnar en la industria para garantizar la trazabilidad entre el negocio y el código. Resalte los patrones de diseño vistos en clase en su implementación y puede usar también el framwe Fastify.
Considerar un API con envío de imágenes, video o audio
Enviar link de su github con código, documentos de requisitos, especificación de casos de uso o de historas y casos de pureba realizadas.

# Especificación de requisitos

## Requerimientos funcionales

- El usuario debe poder presentar un texto detallando su incidencia de como máximo 1000 caracteres.

- El usuario debe poder subir una imagen en formato JPG o PNG de como máximo 5MB junto a las preocupaciones que tenga.

- El usuario debe poder ver todas las incidencias que ha reportado en un listado, junto a la evidencia adjuntada.

- El usuario debe poder usar su DNI para escribir automáticamente sus datos de nombre, residencia y correo de contacto.

## Requerimientos de usabilidad

- El sistema debe presentar mensajes de error claros cuando el usuario exceda alguno de los límites puestos por seguridad.

- El usuario debería poder presentar su queja o incidencia con un solo click.

## Requerimientos de rendimiento

- La subida de incidencias y el mostrado de estas no debería demorar más de 100 milisegundos.

## Requerimientos de base de datos

- El sistema de base de datos deberá almacenar una tabla de ciudadanos solo de lectura y una tabla de incidencias de lectura y escritura.

- El sistema de base de datos almacenará imágenes de evidencia de incidencias en caso el usuario las adjunte en su envío.