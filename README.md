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

## Documentación

### models.py

En este archivo se encuentran los tres modelos de datos utilizados.

#### 1) Modelo Pasajero

Campos:

- nombre(CharField, nombre del pasajero)
- apellido(CharField, apellido del pasajero)
- email(EmailField, email del pasajero)
- telefono(CharField, teléfono del pasajero)
- profesion(CharField, profesión del pasajero)

#### 2) Modelo Habitacion

Campos:

- nombre(CharField, nombre indentificatorio de la habitación)
- numero(IntegerField, número identificatorio de la habitación)
- capacidad(IntegerField, capacidad -en cantidad de personas- de la habitación)

#### 3) Modelo Reserva

Campos:

- Nombre(CharField, nombre del pasajero)
- apellido(CharField, apellido del pasajero)
- fecha_in(DateField, fecha de ingreso)
- fecha_out(DateField, fecha de salida)

### forms.py

En este archivo se encuentran los tres formularios (uno para cada modelo) usados para cargar los datos que quedan guardados en la base de datos.

### urls.py

Contiene cada una de las rutas de las vistas de la app.


### views.py

Aparecen todas las vistas que se utilizan en la app, desde el formulario para la creación de nuevos registros en la BBDD hasta la consulta individual y el listado de todos los registros existentes.

### templates

En las carpetas **templates** de ambas apps se encuentran todos los archivos HTML utilizados, para los cuales se adaptó una plantilla de Bootstrap descargada de [Start Bootstrap](https://startbootstrap.com/), aplicando el concepto de herencia entre archivos para eficientizar el código.

--------------------------------------------------------------------------------------------------

## Instalación

Podrás instalar el software necesario de la siguiente manera:

### Verificar la versión de Python

Este proyecto fue escrito con Python 3.10.8, en base a eso sugerimos que lo pruebes con esta versión o una superior con el fin de  evitar posibles incompatibilidades.

Mac:

```bash
> python --version
> Python 3.10.8
```

in windows:

```bash
c:\> python3 --version
c:\> Python 3.10.8
```

## Instalar dependencias

Para instalar dependencias, necesitas ejecutar `pip install`, asegurándote de estar dentro de la carpeta del archivo y de poder visualizar el archivo `requirements.txt` cuando ejecutes `ls` o en su defecto `dir`.

```bash
> pip install -r requirements.txt
```

### Crear la base de datos

Para realizar las migraciones de los modelos a la BBDD, deberás ejecutar los siguientes comandos:

```bash
> python manage.py makemigrations
> python manage.py migrate
```

### Ejecutar el servidor

Mac:

```bash
> python3 mananage.py runserver
```

windows:

```bash
c:\> python mananage.py runserver
```

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