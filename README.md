# Nombre del proyecto:
Sprint 8
## Problemática:
1. OBTENER DATOS DE UN CLIENTE: Un cliente autenticado puede consultar sus propios datos.
2. OBTENER SALDO DE CUENTA DE UN CLIENTE: Un cliente autenticado puede obtener el tipo de cuenta y su saldo.
3. OBTENER MONTO DE PRESTAMOS DE UN CLIENTE: Un cliente autenticado puede obtener el tipo de préstamo y total del mismo.
4. OBTENER MONTO DE PRESTAMOS DE UNA SUCURSAL: Un empleado autenticado puede obtener el listado de préstamos otorgados de una sucursal determinada.
5. OBTENER TARJETAS ASOCIADAS A UN CLIENTE: Un empleado autenticado puede obtener el listado de tarjetas de crédito de un cliente determinado.
6. GENERAR UNA SOLICITUD DE PRESTAMO PARA UN CLIENTE: Un empleado autenticado puede solicitar un préstamo para un cliente, registrado el mismo y acreditando el saldo en su cuenta.
7. ANULAR SOLICITUD DE PRESTAMO DE CLIENTE: Un empleado autenticado puede anular un préstamo para un cliente, revirtiendo el monto correspondiente.
8. MODIFICAR DIRECCION DE UN CLIENTE: El propio cliente autenticado o un empleado puede modificar las direcciones.
9. LISTADO DE TODAS LAS SUCURSALES: Un endpoint público que devuelve el listado todas las sucursales con la información correspondiente.
## Dependencias:
Python 3 https://www.python.org/downloads/

## Librerías requeridas:
Django (pip install django) <br >
Django-Bootstrap-Forms (pip install django-bootstrap-form) <br>
pip install djangorestframework
## Comandos para la ejecución del programa:
python manage.py runserver

## Vistas
  En la url '/cuenta/registerEmpleado' los superusers pueden crear nuevos empleados. Tanto los empleados como los superusers pueden analizar y manipular la api en su totalidad
  




