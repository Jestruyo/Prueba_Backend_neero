# Prueba_Backend_neero
Este repositorio contiene el desarrollo de una Rest Api, basada en los requerimientos funcionales que conforman el enunciado propuesto para las necesidades de una empresa distribuidora de produtos lácteos.

Contexto del ejercicio.
Una empresa de productos lácteos con distribución a nivel nacional ha decidido enviar a su fuerza
de ventas a los diferentes puntos de venta del país a registrar las fotos de las neveras, para poder
identificar los productos exhibidos en cada Punto de Venta. Ante la gran variedad que presentan
las regiones del país, y dependiendo la tipología donde se presenten los productos
(Supermercados, Minimercados, Panaderías), se cuentan con diferentes portafolios de infaltables.
Para ello, se ha decidido desarrollar una aplicación donde los vendedores puedan registrar los
productos y mostrarlos por catálogo, almacenamiento registrado y discriminado por catálogo.

Prueba
1. Realice un diagrama Entidad-Relación donde resuelva este caso, tenga en cuenta el los
productos, el portafolio, el establecimiento y el usuario.
2. Realizar API REST donde se puedan realizar las siguientes acciones:
a. Creación de producto.
b. Creación de establecimiento.
c. Creación de portafolio.
d. Creación de usuario.
3. Se debe hacer uso de JWT para la seguridad y manejo de sesiones, Si se va a usar otro
protocolo de seguridad y manejo de sesiones, se debe especificar y explicar
4. ¿Qué infraestructura utilizará para resolver este caso? (Bases de datos relacionales o
documentales, Servidores dedicados o en la nube, protocolos de comunicación).
5. Si el servicio será utilizado por 12.000 vendedores a nivel nacional, con una disponibilidad
del 99.9999% y el servicio debe funcionar por lo menos de lunes a sábado, ¿Qué medidas
tomaría para garantizar los servicios?
6. El servicio presentado pasa por una etapa de soporte, donde se resuelven los casos de no
reconocimiento y fallas en el servicio en la aplicación. También, se encuentra la etapa de
analítica, donde se realizan mediciones a gran nivel donde con tableros de control se
toman medidas a nivel gerencial. ¿Qué servicios o herramientas se pueden disponibilizar
para facilitar el trabajo de estas áreas?

________________________________________________________________________________________________________________________

DESARROLLO

Diagrama de flujo, basado en base firebase:
URL https://lucid.app/lucidchart/cc3aff26-6f89-4da0-b7c1-5a572966cc77/view?page=0_0&invitationId=inv_31225b5c-c791-4cad-8971-5bb5850b03ed#


Diagrama de entidad relacional, basado en base SQL:
URL https://lucid.app/lucidchart/f2dccb30-63d5-4c4d-8817-89380665c556/view?page=0_0&invitationId=inv_acc3b617-a928-4c81-89c3-f14482e86c11#



Tecnologias implementadas en el desarrollo.
-Lenguaje: Python - Framework Flask.
-Base de datos no relacional: Firebase.
-Librerias: Flask | Firebase_admin, para la conexion con la plataforma.
-Metodos de autenticacion y manejo de sesion: Clave privada con extension .json desde la plataforma, token.

Herramientas
-Herramienta de prueba REST: Insomnia.
-Herramientas de nivel gerencial: Google Analytics, Cloud firestore, RealTime Database, Remote Config, Autenticacion.
*Todas estas herramientas se deben integrar desde la plataforma firebase.


