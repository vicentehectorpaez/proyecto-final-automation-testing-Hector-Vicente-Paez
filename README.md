# Framework de Pruebas Automatizadas (QA Automation)

## 📌 Propósito del proyecto
Este proyecto es un framework de automatización de pruebas híbrido desarrollado en Python. Permite ejecutar pruebas de interfaz de usuario (**UI**) utilizando Selenium WebDriver bajo el patrón Page Object Model (POM), y pruebas de servicios web (**API**) utilizando la librería Requests. Cuenta además con generación automática de reportes HTML e integración con capturas de pantalla automáticas ante fallos.

## 🛠️ Tecnologías utilizadas
* **Python** (Lenguaje de programación)
* **Pytest** (Framework de ejecución de pruebas)
* **Selenium WebDriver** (Automatización de UI)
* **Requests** (Automatización de servicios API)
* **Faker** (Generación de datos dinámicos para formularios)
* **Pytest-HTML & Pytest-Metadata** (Generación y metadatos de reportes HTML)

## 📂 Estructura del proyecto
```text
proyecto-final-automation-testing-Hecto Vicente Paez/
│   conftest.py
│   pytest.ini
│   README.md
│                  
├───data
│       login_data_parametrize.json
│       login_data_unusuario.json
│       
├───logs
│       framework.log
│       
├───pages
│       BasePage.py
│       CartPage.py
│       CheckoutPage.py
│       InventoryPage.py
│       LoginPage.py
│           
├───reports
│   │       
│   └───screenshots
├───tests
│       test_api.py
│       test_checkout_completo.py
│       test_inventory_page.py
│       test_login.py
│           
└───utils
        api_cliente.py
⚙️ Cómo instalar dependencias y ejecutar
Asegurate de tener Python instalado y ejecutá los comandos necesarios en la terminal, dentro de la raíz del proyecto.

🚀 Comandos de ejecución
Ejecutar todas las pruebas (UI + API) y generar reporte automático:

Bash
py -m pytest
Ejecutar únicamente las pruebas de UI (Checkout completo):

Bash
py -m pytest -v tests/test_checkout_completo.py
Ejecutar únicamente las pruebas de API:

Bash
py -m pytest -v tests/test_api.py
Ejecutar pruebas filtradas por marcas / marcadores (ej. regresión):

Bash
py -m pytest -m regression
📊 Cómo interpretar los reportes
Gracias a la configuración en el archivo pytest.ini, cada vez que ejecutas las pruebas, se genera o actualiza automáticamente un reporte visual integrado.

Dónde encontrarlo: El archivo se guarda en la ruta reports/reports_final.html.

Visualización: Hacé doble clic sobre el archivo HTML para abrirlo en cualquier navegador web. Allí verás el resumen detallado de las pruebas ejecutadas (pasadas o falladas), los tiempos de duración de cada test y, en caso de que alguna prueba de UI falle, la captura de pantalla (screenshot) del error adjunta de manera automática.

✅ Cobertura de pruebas
UI - SauceDemo

Login exitoso

Login usuario bloqueado

Verificación de elementos de inventario

Ordenamiento de productos por precio

Flujo completo de compra (Checkout End to End)

API - ReqRes

GET usuario

POST usuario

DELETE usuario

📈 Resultado de ejecución
Última ejecución:

13 tests ejecutados | 13 tests aprobados | 0 pruebas fallidas

👨‍💻 Autor
Vicente Hector Paez

Proyecto Final Integrador Automation Testing con Python