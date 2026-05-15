# Sistema de Registro de Incidencias

Proyecto Django para la gestión y registro de incidencias.

## Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación y configuración

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar migraciones de base de datos

```bash
python manage.py migrate
```

### 3. (Opcional) Crear un usuario administrador

```bash
python manage.py createsuperuser
```

Sigue las indicaciones del comando para crear un usuario con acceso al panel de administración.

### 4. Levantar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://localhost:8000/`

## Acceso a la aplicación

- **Sitio principal:** http://localhost:8000/
- **Panel de administración:** http://localhost:8000/admin/
- **API:** http://localhost:8000/api/

## Estructura del proyecto

- `registro_incidencias/` - Aplicación principal del sistema
- `sistema_incidencias/` - Configuración del proyecto Django
- `documentación/` - Documentos de análisis y especificación
- `db.sqlite3` - Base de datos SQLite

## Notas

- El proyecto utiliza SQLite como base de datos por defecto
- La base de datos inicial (`db.sqlite3`) ya viene creada en el repositorio
