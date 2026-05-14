# Stack tecnológico

- Python 3
- Requests
- Beautiful Soup 4
- lxml
- threading (biblioteca estándar de Python)

# Temporary Number Scraper

Este proyecto es un scraper en Python que consume la web pública `online-sms.org` para listar números temporales disponibles y revisar los mensajes recibidos en cada número.

La lógica principal hace lo siguiente:

1. Obtiene la lista de números publicados en la página principal.
2. Entra a cada número y recorre sus páginas de mensajes.
3. Cuenta cuántas veces aparece el remitente `Twitter`.
4. Ejecuta el análisis de varios números en paralelo usando hilos.

En la práctica, el script sirve para inspeccionar rápidamente la actividad asociada a números temporales expuestos por el sitio fuente.

# Requisitos previos

- Python 3.10 o superior recomendado.
- Conexión a internet, porque el proyecto consulta un sitio web externo en tiempo real.

# Instalación local

1. Clona el repositorio.
2. Entra a la carpeta del proyecto.
3. Crea un entorno virtual.
4. Activa el entorno virtual.
5. Instala las dependencias.

```bash
git clone <URL-del-repositorio>
cd temporary-number-scraper
python3 -m venv .venv
source .venv/bin/activate
pip install requests beautifulsoup4 lxml
```

# Cómo ejecutar

1. Asegúrate de tener el entorno virtual activo.
2. Ejecuta el script principal.

```bash
python main.py
```

Al ejecutarlo, el programa descargará la lista de números disponibles y mostrará en consola el conteo de coincidencias para cada uno.

# Estructura del proyecto

- `main.py`: contiene el scraper, el recorrido de páginas y la ejecución multihilo.
- `colours.py`: define helpers simples para imprimir mensajes con color en la terminal.

# Notas importantes

- El proyecto depende de la estructura HTML del sitio `online-sms.org`. Si la web cambia, el scraper puede dejar de funcionar.

