
# RooMe

RooMe es una plataforma diseñada para facilitar a los usuarios extranjeros la búsqueda y reserva de habitaciones compartidas. Los usuarios pueden filtrar sus búsquedas según su nacionalidad, número de personas, y otros criterios, haciendo que encontrar roomates y habitaciones sea mucho más sencillo.

## Tecnologías Utilizadas

- **Backend**: Python (Django)
- **Frontend**: HTML, CSS (Bootstrap)
- **Base de Datos**: MySQL

## Características

- **Búsqueda Avanzada**: Filtra habitaciones según la nacionalidad, número de personas, y otros criterios relevantes.
- **Reservas en Línea**: Realiza reservas directamente desde la plataforma.
- **Panel de Administrador**: Administra las habitaciones, reservas, y usuarios desde un panel dedicado.
- **Interfaz Amigable**: Diseño responsive utilizando Bootstrap para asegurar una experiencia de usuario óptima en todos los dispositivos.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tuusuario/RooMe.git
   cd RooMe

2. Crea y activa un entorno virtual:

    ```bash
   python3 -m venv env
    source env/bin/activate

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt

4. Configura la base de datos en settings.py y aplica las migraciones:

    ```bash
    python manage.py migrate

5. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver

6. Accede a la plataforma en http://127.0.0.1:8000.

## Uso

- **Usuario Final**: Puede buscar habitaciones, aplicar filtros, y realizar reservas.
- **Administrador**: Accede al panel de administración para gestionar habitaciones, usuarios, y reservas.

## Contribución

¡Contribuciones son bienvenidas! Por favor, sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature-nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadí nueva funcionalidad'`).
4. Sube tu rama (`git push origin feature-nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE).

