# Curso de Python - Coderhouse

- Curso: Python
- Comisión: 44470
- Alumnos: Alejandro Lucas Gallo y Emiliano Scarfó
- Entrega del Proyecto Final
- 6 de diciembre de 2022

--------------------------------------------------------------------------------------------------

## Acerca del Proyecto

El trabajo corresponde a la entrega final del Proyecto Final del curso de Python dictado por Coderhouse y está desarrollado íntegramente en Python y Django. En este caso, se desarrolló una **WEB Django con patrón MVT** para una empresa orientada a ofrecer servicios de intermediación para la inversión en activos de renta fija. Específicamente, se desarrollaron dos apps, una para administrar todo lo relativo a los diferentes activos ofrecidos, permitiendo acceder, una vez correctamente logueado el usuario, a los formularios para crear especies en cada tipo de activo y, posteriormente, editarlas o borrarlas. Además, se incluyó una función de búsqueda por código de especie para ir directamente a la información contenida en cada una de ellas. La otra app se construyó para ofrecer un blog donde el usuario puede postear mensajes, los cuales quedan listados por fecha para ser vistos por todos los usuarios.

--------------------------------------------------------------------------------------------------

## Características y funcionalidades

La aplicación se desarrolló aplicando los conceptos vistos en el curso. En particular, se utilizó el patrón de diseño web utilizado por Django, denominado Modelo-Template-View (MTV) ó Modelo-View-Template (MVT). El modelo (model) permite administrar la base de datos, la plantilla (template) es una capa de presentación que se encarga completamente de la interfaz de usuario y la vista (view) se utiliza para ejecutar la lógica del negocio e interactuar con el modelo para transportar datos y renderizar la plantilla (template). El flujo de control basado en MVT funciona de la siguiente manera: 1) el usuario solicita un recurso a Django; 2) Django verifica el recurso disponible en la URL; 3) la URL asignada llama a una vista (view) que interactúa con el modelo (model) y renderiza una plantilla (template) como respuesta al usuario.

--------------------------------------------------------------------------------------------------

## Estilos

En las carpetas **templates** de ambas apps se encuentran todos los archivos HTML utilizados, para los cuales se adaptó una plantilla de Bootstrap descargada de [Start Bootstrap](https://startbootstrap.com/), aplicando el concepto de herencia entre archivos para eficientizar el código.

--------------------------------------------------------------------------------------------------

## Requisitos

Deberá tener instalado:

- python version 3.10.8
- django version 4.1.4
- pillow version 9.3.0

### Ejecutar los comandos

Para realizar las migraciones,este proyecto usa SQLite3

1) python manage.py makemigrations
2) python manage.py migrate

--------------------------------------------------------------------------------------------------

## Pruebas

Las pruebas realizadas fueron:

- Se creó un usuario desde el formulario que solicita los datos.
- Se creó un dato de literatura desde el formulario que solicita los datos.
- Se creó un dato de musica desde el formulario que solicita los datos.
- Se creó un dato de cine desde el formulario que solicita los datos.
- Se buscaron datos de literaturas ya cargadas desde el formulario que solicita los datos, donde realiza la búsqueda con al menos un dato ingresado coincidente.
- Se buscaron datos de musica ya cargadas desde el formulario que solicita los datos, donde realiza la búsqueda con al menos un dato ingresado coincidente.
- Se buscaron datos de cine ya cargadas desde el formulario que solicita los datos, donde realiza la búsqueda con al menos un dato ingresado coincidente.
