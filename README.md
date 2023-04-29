# rest_api_iaInteractive
IA – Examen Backend Python Developer

Caso Práctico: Sistema de registro y asignación de Grimorios para la academia de magia del Reino del Trébol.

Este proyecto consiste en la construcción de un API Rest para la academia de magia del Reino del Trébol, que permita el registro de solicitudes de ingreso de estudiantes y la asignación aleatoria de Grimorios. Los Grimorios se clasifican según el tipo de trébol en la portada y su nivel de poder varía desde el trébol de una hoja hasta el trébol de cinco hojas.

Herramientas utilizadas:

Este proyecto se ha construido utilizando Python y Flask como framework para el desarrollo del API Rest. Se ha utilizado también una base de datos alojada en Postgresql para almacenar la información de las solicitudes de ingreso y las asignaciones de Grimorios. Ademas de el uso de Visual Studio Code editor de codigo fuente y Postman como plataforma para la prueba de la API.

Endpoints:

A través de Postman se pueden acceder a los siguientes endpoints necesarios para soportar las operaciones requeridas:

-- POST /solicitudes: permite enviar una solicitud de ingreso con los datos del aspirante.

-- PUT /solicitudes/<id>: permite actualizar los datos de una solicitud de ingreso existente.

-- PATCH /solicitudes/<id>: permite actualizar el estatus de una solicitud de ingreso (aprobada o rechazada).

-- GET /solicitudes: permite consultar todas las solicitudes de ingreso registradas.

-- GET /grimorios: permite consultar todas las asignaciones de Grimorios realizadas.

-- DELETE /solicitudes/<id>: permite eliminar una solicitud de ingreso existente.

Datos requeridos en una solicitud de ingreso:

Para poder registrar una solicitud de ingreso, se requiere que el aspirante proporcione los siguientes datos:

1. Nombre (solo letras, máximo 20 caracteres).
2. Apellido (solo letras, máximo 20 caracteres).
3. Identificación (números y letras, máximo 10 caracteres).
4. Edad (solo números, 2 dígitos).
5. Afinidad Mágica (Ls tipos de magia se encuentran dentro del archivo Excel alojado en la carpeta "documentos").
Cualquier solicitud que no cumpla con estos criterios será automáticamente rechazada y no se le asignará un Grimorio.

Auto asignación de Grimorios y portadas:

Una vez que una solicitud de ingreso ha sido aprobada, se procederá a la asignación aleatoria de un Grimorio y su respectiva portada según el nivel de poder del Grimorio. Este proceso se realiza automáticamente y no requiere intervención manual.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Instrucciones para ejecutar el proyecto:



Autor:
Este proyecto ha sido desarrollado por Uriel Cruz Rodríguez.
