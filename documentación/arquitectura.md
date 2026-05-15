# Arquitectura - Modelo Vista Plantilla

La arquitectura utilizada para este proyecto será una variación de Modelo-Vista-Controlador: Modelo-Vista-Plantilla, la cual es implementada por el framework de desarrollo web Django.

Esta arquitectura se distingue de MVC de forma que la Plantilla es el análogo al Controlador, la cual solo se encarga de renderizar los datos, mientras que la Vista maneja la lógica de negocios. Django simplifica el trabajo del desarrollador al actuar como Controlador, manejando las solicitudes que el usuario envía. El Modelo mantiene su mismo propósito: definir los datos que el sistema manejará