# Curso de Python - Coderhouse

- Curso: Python
- Comisión: 44470
- Alumnos: Alejandro Lucas Gallo y Emiliano Scarfó
- Entrega del Proyecto Final
- 7 de diciembre de 2022

--------------------------------------------------------------------------------------------------

## Acerca del Proyecto

El trabajo corresponde a la entrega final del Proyecto Final del curso de Python dictado por Coderhouse y está desarrollado íntegramente en Python y Django. En este caso, se desarrolló una **WEB Django con patrón MVT** para una empresa orientada a ofrecer servicios de intermediación para la inversión en activos de renta fija. Específicamente, se desarrollaron dos apps, una para administrar todo lo relativo a los diferentes activos ofrecidos, permitiendo acceder, una vez correctamente logueado el usuario, a los formularios para crear especies en cada tipo de activo y, posteriormente, editarlas o borrarlas. Además, se incluyó una función de búsqueda por código de especie para ir directamente a la información contenida en cada una de ellas. La otra app se construyó para ofrecer un Blog donde el usuario puede postear mensajes, los cuales quedan listados por fecha para ser vistos por todos los usuarios.

--------------------------------------------------------------------------------------------------

## Características y funcionalidades

La aplicación se desarrolló aplicando los conceptos vistos en el curso. En particular, se utilizó el patrón de diseño web utilizado por Django, denominado Modelo-Template-View (MTV) ó Modelo-View-Template (MVT). El modelo (model) permite administrar la base de datos, la plantilla (template) es una capa de presentación que se encarga completamente de la interfaz de usuario y la vista (view) se utiliza para ejecutar la lógica del negocio e interactuar con el modelo para transportar datos y renderizar la plantilla (template). El flujo de control basado en MVT funciona de la siguiente manera: 1) el usuario solicita un recurso a Django; 2) Django verifica el recurso disponible en la URL; 3) la URL asignada llama a una vista (view) que interactúa con el modelo (model) y renderiza una plantilla (template) como respuesta al usuario.

--------------------------------------------------------------------------------------------------

## Documentación

### models.py

En este archivo se encuentran los cinco modelos de datos utilizados.

#### 1) Modelo Dolar

Campos:

- codigo(CharField, código de la especie)
- denominacion(CharField, denóminacion de la especie)
- emisor(EmailField, emisor de la especie)
- fecha_emision(DateField, fecha de emisión de la especie)
- fecha_vencimiento(DateField, fecha de vencimiento de la especie)
- amortizacion(CharField, amortización de la especie)
- interes(CharField, interés de la especie)
- ley(CharField, ley de la especie)

#### 2 a 5) Modelo Peso, Pesobd, Pesodl y Especie

Se repiten los mismos campos que en el modelo 1) Dolar. En el caso del modelo Especie, se creó para registrar todas las especies en una misma tabla, la cual luego es recorrida por la función buscar.

### forms.py

En este archivo se encuentran los dos formularios usados para crear un usuario (UserRegisterForm) y para editar su perfil (UserEditionForm), los cuales son ofrecidos por Django como sistema de autenticación de usuario integrado. Esta configuración cumple con los requisitos más comunes de los proyectos, maneja una amplia gama de tareas y contraseñas y permisos válidos.

### urls.py

Contiene cada una de las rutas de las vistas de las apps. En el caso del logout, se utilizó la vista predefinida por Django LogoutView para renderizar la página AppBonos/logout.html

### views.py

Aparecen todas las vistas que se utilizan en las apps, desde el formulario para la creación de nuevos registros en las bases de datos hasta la consulta individual y el listado de los registros existentes. Para simplificar algunos procesos, se crearon tres clases basadas en vistas: UpdateView, DeleteView y DetailView. Además, se creó el login aplicando AuthenticationForm, el sistema de autenticación de Django. Finalmente, se utilizaron los mixin y decoradores de Django para que sólo usuarios logueados puedan ver el sitio o para que puedan acceder a una sección determinada estando logueados.

### templates

En las carpetas **templates** de ambas apps se encuentran todos los archivos HTML utilizados, para los cuales se adaptó una plantilla de Bootstrap descargada de [Start Bootstrap](https://startbootstrap.com/), aplicando el concepto de herencia entre archivos para eficientizar el código.

--------------------------------------------------------------------------------------------------

## Instalación

Podrás instalar el software necesario de la siguiente manera:

### Verificar la versión de Python

Este proyecto fue desarrollado con Python 3.10.8, por lo que sugerimos que lo pruebes con esta versión o una superior con el fin de  evitar posibles incompatibilidades.

```bash
> python3 --version
> Python 3.10.8
```

## Instalar dependencias

Para instalar dependencias, necesitás instalar pip:

```bash
> python -m pip install
```

### Crear las bases de datos

Para transformar los modelos en bases de datos y para generar sus estructuras, deberás ejecutar los siguientes comandos:

```bash
> python manage.py makemigrations
> python manage.py migrate
```

### Ejecutar el servidor

Para ejecutar el servidor y poder desplegar el sitio en tu explorador, deberás ejecutar este comando:

```bash
> python mananage.py runserver
```

--------------------------------------------------------------------------------------------------

## Acceso a las bases de datos

Se utilizaron SQLite y DB Browser para acceder a la información de las bases de datos.

--------------------------------------------------------------------------------------------------

## Pruebas

Se realizaron 28 pruebas unitarias y se documentaron en el archivo casos_de_prueba.xls

--------------------------------------------------------------------------------------------------

## Video

En este [video](https://youtu.be/bq0vWNbHN_E/) se puede ver el sitio web funcionando.
