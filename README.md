# Sistema de Gestion Clinica Veterinaria - Odoo 17

Proyecto conjunto desarrollado en equipo para la gestion integral de una clinica veterinaria utilizando Odoo 17 como plataforma ERP.

Este repositorio contiene los modulos personalizados desarrollados por el grupo para ampliar la funcionalidad base de Odoo y adaptarla a las necesidades especificas de una clinica veterinaria.

---

## Objetivo del proyecto

El objetivo principal es implementar un sistema de gestion que permita:

- Administrar el personal de la clinica
- Gestionar clientes y mascotas
- Controlar servicios veterinarios
- Integrar toda la informacion dentro del entorno Odoo
- Aplicar buenas practicas de desarrollo de modulos

Proyecto realizado como parte del ciclo formativo de Desarrollo de Aplicaciones Multiplataforma (DAM).

---

## Tecnologias utilizadas

- Odoo 17
- Python
- PostgreSQL
- Docker
- XML (vistas y configuracion)
- Git

---

## Estructura del proyecto

```
VETERINARIA_ODOO/
│
├── docker-compose.yml
├── addons/
│   ├── gestion_personal_veterinaria/
│   ├── gestion_productos/
│   ├── gestion_mascotas/
│   └── otros_modulos_del_equipo/
│
└── README.md
```

La carpeta addons contiene todos los modulos personalizados desarrollados por el equipo.

---

## Requisitos previos

Para ejecutar el proyecto es necesario tener instalado:

- Docker Desktop
- Git
- Navegador web

Se recomienda ejecutar el proyecto mediante Docker para evitar problemas de configuracion manual.

---

## Instalacion y puesta en marcha

### 1. Clonar el repositorio

```
git clone https://github.com/TU_USUARIO/VETERINARIA_ODOO.git
cd VETERINARIA_ODOO
```

---

### 2. Levantar los contenedores

Desde la raiz del proyecto ejecutar:

```
docker compose up -d
```

Este comando iniciara:

- Contenedor de PostgreSQL
- Contenedor de Odoo 17

---

### 3. Acceso a la aplicacion

Abrir el navegador y acceder a:

```
http://localhost:8069
```

---

## Creacion de la base de datos

En el primer acceso se solicitara crear una nueva base de datos.

Configuracion recomendada:

- Nombre base de datos: veterinaria
- Usuario administrador: admin
- Contraseña: la que se desee
- Idioma: Español

---

## Instalacion de los modulos del proyecto

1. Activar modo desarrollador:
   - Ir a Ajustes
   - Activar modo desarrollador
   - O añadir ?debug=1 a la URL

2. Ir a Apps

3. Pulsar en Actualizar lista de aplicaciones

4. Buscar los modulos desarrollados por el equipo

5. Instalar los modulos necesarios

---

## Desarrollo de nuevos modulos

Para añadir un nuevo modulo personalizado:

1. Crear carpeta dentro de addons/
2. Incluir obligatoriamente:
   - __manifest__.py
   - __init__.py
   - Carpeta models
   - Carpeta views
3. Reiniciar Odoo
4. Actualizar lista de aplicaciones

---

## Trabajo en equipo

Este proyecto ha sido desarrollado de forma colaborativa.  
Cada modulo puede haber sido implementado por distintos miembros del equipo siguiendo una estructura comun para mantener coherencia y organizacion del codigo.

---

## Uso academico

Proyecto desarrollado con fines educativos dentro del ciclo DAM Jorge, Diego, Aitor y Ruben.

