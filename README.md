# superlogic-project

NOTA:
Se incluye la versión en Django(/superlogic) y la ejecutable en cmd (/for_console), es así que se brindan
ambas posibilidades según sus adaptaciones al conocimiento que el equipo habría 
adquirido para realización de "superlogic-project".





****** REQUERIMIENTOS DE DJANGO PARA EL CORRIMIENTO DEL PORGRAMA EN LOCALHOST ******


INSTALACIÓN DE PYTHON
Al ser Django un framework basado en python, debe integrarse su instalación:
https://www.python.org/downloads/


INSTALACIÓN DE DJANGO
Debe instalarse el Framework de Django para poder corrrer este proyecto
en servidor local, para esto, se ejecuta:

      MAC & LINUX
      >>>python -m pip install Django

      WINDOWS
      >>>py -m pip install Django

VERIFICAR INSTALACIÓN DE DJANGO
>>> import django
>>> print(django.get_version())
4.0


CORRIMIENTO DE PROYECTO
El proyecto deberá correrse en consola, se abrirá el CMD o Terminal en el caso de MacOS y Linux donde  se ubicara la carpeta donde se aloje 
el proyecto:

>>>cd carpetaArchivo

Posteriormente, se utilizará el siguiente comando para correrse en servidor local:

      MAC & LINUX
      >>>python manage.py runserver

      WINDOWS
      >>>py manage.py runserver

Como último paso, bastará con abrir una pestaña del navegador a elección escribiendo en la URL:

http://127.0.0.1:8000/


NOTA: Para mayores consultas, se recomienda revisar la documentación
oficial del framework de Django en:
https://docs.djangoproject.com/en/4.0/

      




