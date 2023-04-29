# rest_api_iaInteractive
## IA – Examen Backend Python Developer

**Caso Práctico:** Sistema de registro y asignación de Grimorios para la academia de magia del Reino del Trébol.

Este proyecto consiste en la construcción de un API Rest para la academia de magia del Reino del Trébol, que permita el registro de solicitudes de ingreso de estudiantes y la asignación aleatoria de Grimorios. Los Grimorios se clasifican según el tipo de trébol en la portada y su nivel de poder varía desde el trébol de una hoja hasta el trébol de cinco hojas.

**Herramientas utilizadas:**

Este proyecto se ha construido utilizando Python y Flask como framework para el desarrollo del API Rest. Se ha utilizado también una base de datos alojada en Postgresql para almacenar la información de las solicitudes de ingreso y las asignaciones de Grimorios. Ademas de el uso de Visual Studio Code editor de codigo fuente y Postman como plataforma para la prueba de la API.

**Endpoints:**

A través de Postman se pueden acceder a los siguientes endpoints necesarios para soportar las operaciones requeridas:

-- POST /solicitudes: permite enviar una solicitud de ingreso con los datos del aspirante.

-- PUT /solicitudes/<id>: permite actualizar los datos de una solicitud de ingreso existente.

-- PATCH /solicitudes/<id>: permite actualizar el estatus de una solicitud de ingreso (aprobada o rechazada).

-- GET /solicitudes: permite consultar todas las solicitudes de ingreso registradas.

-- GET /grimorios: permite consultar todas las asignaciones de Grimorios realizadas.

-- DELETE /solicitudes/<id>: permite eliminar una solicitud de ingreso existente.

**Datos requeridos en una solicitud de ingreso:**

Para poder registrar una solicitud de ingreso, se requiere que el aspirante proporcione los siguientes datos:

1. Nombre (solo letras, máximo 20 caracteres).
2. Apellido (solo letras, máximo 20 caracteres).
3. Identificación (números y letras, máximo 10 caracteres).
4. Edad (solo números, 2 dígitos).
5. Afinidad Mágica (Ls tipos de magia se encuentran dentro del archivo Excel alojado en la carpeta "documentos").
Cualquier solicitud que no cumpla con estos criterios será automáticamente rechazada y no se le asignará un Grimorio.

**Auto asignación de Grimorios y portadas:**

Una vez que una solicitud de ingreso ha sido aprobada, se procederá a la asignación aleatoria de un Grimorio y su respectiva portada según el nivel de poder del Grimorio. Este proceso se realiza automáticamente y no requiere intervención manual.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Instrucciones para ejecutar el proyecto:

1. En Postgresql, crear una base de datos con el nombre: *"escuela_magica"* y dentro de ella crear una tabla con el query que se encuentra en el archivo **"Database.txt"**.

2. Descargar el proyecto **rest_api_iaInteractive-master.zip** y utilizando *Visual Studio Code*, abrir la carpeta **rest_api_iaInteractive-master**.
  
3. Una vez abierta la carpeta, abrir una nueva terminal y crear un entorno virtual: **py -m virtualenv venv**
  
4. Activar el entorno virtual: **.\venv\Scripts\activate**
  
5. Una vez activado, instalar las paqueterias a utilizar: **pip install -requerimientos.txt**
  
6. Ya instalados los requerimientos, editar la conexion a la base de datos *# Establecer conexion con la base de datos* (host, database, user, password) en el archivo **app.py** (en la parte de *database*, colocar: **escuela_magica**).
  
7. En la terminal corremos la aplicacion: **py .\app.py**
  
8. Esta nos dara un link como este: *Running on http://127.0.0.1:5000* lo que indica que estamos utilizando el servidor local con el puerto *5000*.
  
9. **Abrir Postman y en la parte de *Workspace*, crear un nuevo espacio de trabajo y empezar a probar los endpoints:**
  
---- **Enviar solicitud de ingreso:** Dar click en el simbolo **+** y seleccionar un request de tipo *POST*, posteriormente, en la parte de la *URL*, colocar: **http://localhost:5000/solicitudes** (el puerto 5000 puede ser diferente, dependiendo de cual se te dio al correr la aplicacion). Una vez hecho esto, en la parte de *body*, seleccionar **raw** y **JSON**. Finalmente el el area de texto colocar un JSON como el siguiente:
  
  {
  
    "nombre": "",
  
    "apellido": "",
  
    "identificacion": "",
  
    "edad": ,
  
    "afinidad_magica": ""
  }
  
 Colocar los datos de la solicitud a registar y dar clic en **SEND**. Si la solicitud cumple con los requerimientos aparecera este mensaje: **"Solicitud insertada correctamente"**, de lo contrario se mostrara este: **"La solicitud ha sido rechazada"**.
 
---- **Actualizar solicitud de ingreso:**  Dar click en el simbolo **+** y seleccionar un request de tipo *PUT*, posteriormente, en la parte de la *URL*, colocar: **http://localhost:5000/solicitudes/id a actualizar(ejemplo: 7)** (el puerto 5000 puede ser diferente, dependiendo de cual se te dio al correr la aplicacion). Una vez hecho esto, en la parte de *body*, seleccionar **raw** y **JSON**. Finalmente el el area de texto colocar un JSON con los datos de la solicitud a actualizar como el siguiente:
  
  {
  
    "nombre": "Marcela",
  
    "apellido": "Monroy",
  
    "identificacion": "019000012g",
  
    "edad": 25,
  
    "afinidad_magica": "Magia de Bronce",
  
    "grimorio": "Esperanza",
  
    "portada": "Trébol de 2 hojas"
}
  
 Cambiar los datos de la solicitud a actualizar y dar clic en **SEND**. Una vez actualizada la solicitud aparecera este mensaje: **"Solicitud actualizada correctamente"**.

---- **Actualizar estatus de solicitud:** Dar click en el simbolo **+** y seleccionar un request de tipo *PATCH*, posteriormente, en la parte de la *URL*, colocar: **http://localhost:5000/estatus/id a actualizar(ejemplo: 7)** (el puerto 5000 puede ser diferente, dependiendo de cual se te dio al correr la aplicacion). Una vez hecho esto, en la parte de *body*, seleccionar **raw** y **JSON**. Finalmente el el area de texto colocar un JSON con el estatus de la solicitud a actualizar como el siguiente:
  
  {
  
    "estatus": "rechazada"
  }
  
 Cambiar el estatus a actualizar y dar clic en **SEND**. Una vez enviado el request aparecera este mensaje: **"Estatus de solicitud actualizado correctamente"**.
  
---- **Consultar todas las solicitudes:** Dar click en el simbolo **+** y seleccionar un request de tipo *GET*, posteriormente, en la parte de la *URL*, colocar: **http://localhost:5000/solicitudes** (el puerto 5000 puede ser diferente, dependiendo de cual se te dio al correr la aplicacion). Dar click en **SEND** y se mostraran todas las solicitudes en formato JSON.
  
---- **Consultar asignaciones de Grimorios:** Dar click en el simbolo **+** y seleccionar un request de tipo *GET*, posteriormente, en la parte de la *URL*, colocar: **http://localhost:5000/grimorios** (el puerto 5000 puede ser diferente, dependiendo de cual se te dio al correr la aplicacion). Dar click en **SEND** y se mostraran todas la asignaciones de grimorios en formato JSON.
  
---- **Eliminar solicitud de ingreso:** Dar click en el simbolo **+** y seleccionar un request de tipo *DELETE*, posteriormente, en la parte de la *URL*, colocar: **http://localhost:5000/solicitudes/id a eliminar(ejemplo: 7)** (el puerto 5000 puede ser diferente, dependiendo de cual se te dio al correr la aplicacion). Dar click en **SEND**, la solicitud se eliminara y se mostrara eeste mensaje: **"Solicitud eliminada correctamente"**.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Autor:**
Este proyecto ha sido desarrollado por Uriel Cruz Rodríguez.
