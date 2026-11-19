# Framework de Pruebas Automatizadas (QA Automation)

## 📌 Propósito del proyecto
Este proyecto es un framework de automatización de pruebas híbrido desarrollado en **Python**. Permite ejecutar pruebas de interfaz de usuario (**UI**) utilizando **Selenium WebDriver** bajo el patrón **Page Object Model (POM)**, y pruebas de servicios web (**API**) utilizando la librería **Requests**. Cuenta además con generación automática de reportes HTML, registro de logs y capturas de pantalla automáticas ante fallos.

## 🛠️ Tecnologías utilizadas
* **Python** (Lenguaje de programación principal)
* **Pytest** (Framework de ejecución de pruebas)
* **Selenium WebDriver** (Automatización de pruebas UI)
* **Requests** (Automatización de pruebas API)
* **Faker** (Generación de datos dinámicos para pruebas)
* **Pytest-HTML & Pytest-Metadata** (Generación de reportes HTML y metadatos)
* **Git & GitHub** (Control de versiones y repositorio remoto)

## 📂 Estructura del proyecto
> Nota: En el árbol siguiente se omiten `.pytest_cache/` y las carpetas `__pycache__/` generadas automáticamente durante la ejecución.

```text
proyecto-final-automation-testing-Hector Vicente Paez/
│   .gitignore
│   conftest.py
│   pytest.ini
│   README.md
│
├───automatizacionApi
│   │   metodos_http.py
│   │   validaciones.py
│   │   __init__.py
│   │
│   └───tests
│           test_post.py
│           __init__.py
│
├───data
│       login_data_parametrize.json
│       login_data_unusuario.json
│
├───logs
│       suite.log
│
├───pages
│       BasePage.py
│       CartPage.py
│       CheckoutPage.py
│       InventoryPage.py
│       LoginPage.py
│
├───reports
│   ├───assets
│   │       style.css
│   └───screenshots
│
├───tests
│       test_checkout_completo.py
│       test_inventory_page.py
│       test_login.py
│
└───utils
        helpers.py


⚙️ Cómo instalar dependencias y ejecutar
Asegurate de tener Python instalado y ejecutá los comandos en la terminal dentro de la raíz del proyecto.

1. Instalar dependencias
Bash
py -m pip install pytest pytest-html pytest-metadata selenium requests Faker
(Si tenés un archivo requirements.txt en la raíz, podés instalar todo con py -m pip install -r requirements.txt).

2. Comandos de ejecución
Ejecutar todas las pruebas (UI + API) y generar reporte HTML:

Bash
py -m pytest
Ejecutar únicamente las pruebas de UI (Checkout completo):

Bash
py -m pytest -v tests/test_checkout_completo.py
Ejecutar únicamente las pruebas de API:

Bash
py -m pytest -v automatizacionApi/tests/test_post.py
Ejecutar pruebas filtradas por marcas / marcadores (ej. regresión):

Bash
py -m pytest -m regression
📊 Cómo interpretar los reportes
Gracias a la configuración en pytest.ini, cada vez que se ejecutan las pruebas se genera o actualiza automáticamente el reporte visual en reports/reports_final.html.

Visualización: Abrí reports/reports_final.html en cualquier navegador web.

Contenido: Muestra el resumen de las pruebas ejecutadas, su estado (Passed / Failed), duración y, en caso de que alguna prueba de UI falle, la captura de pantalla guardada en reports/screenshots/ (con nombre descriptivo incluyendo fecha/hora y test) adjunta de manera automática.

Logs de ejecución: El detalle de cada paso y depuración queda registrado en logs/suite.log.

✅ Cobertura de pruebas
UI — SauceDemo
Login exitoso y parametrización con datos externos (data/login_data_parametrize.json y data/login_data_unusuario.json).

Escenarios de usuario bloqueado / validaciones de login.

Verificación de título, productos y elementos de la interfaz de inventario.

Ordenamiento de productos por precio.

Flujo completo de compra (Checkout End to End).

API — JSONPlaceholder
GET de publicación y validación de estructura y contenido JSON.

POST de publicación y validación de código HTTP (201) y datos devueltos.

DELETE de publicación y validación de respuesta.

Escenario de error (404) ante endpoint inexistente.

Flujo encadenado entre peticiones (POST -> DELETE).

📈 Resultado de ejecución
Última ejecución:

15 tests ejecutados | 15 tests aprobados | 0 pruebas fallidas

👨‍💻 Autor
Hector Vicente Paez

Proyecto Final Integrador — Automation Testing con Python