import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import json
import os


@pytest.fixture
def driver():

    service_chrome = Service(ChromeDriverManager().install())
    #navegador = webdriver.Chrome(service=service_chrome)


    #crear ruta para test de descarga de archivos 
    chrome_options = webdriver.ChromeOptions()

    prefs = {
      "download.default_directory": r"C:\Users\Vicente.Paez\Downloads",
      "download.prompt_for_download": False,
      "download.directory_upgrade": True
    }

    chrome_options.add_experimental_option("prefs", prefs)

    navegador = webdriver.Chrome(service=service_chrome,options=chrome_options)
    

    yield navegador

    navegador.quit()

# fixture para utilizar login en todos mis test 
@pytest.fixture
def datos_login():
    """Lee las credenciales desde el archivo JSON en la carpeta data """
    ruta_json = os.path.join(os.path.dirname(__file__), "data", "login_data_unusuario.json")
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


# crear un hook para hacer screenshot automaticos cuando falla el test 
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:

            fecha = datetime.now().strftime("%Y%m%d_%H%M%S")

            ruta = f"reports/screenshots/{item.name}_{fecha}.png"

            driver.save_screenshot(ruta)

            extras = getattr(report, "extras",[])            

            extras.append(pytest_html.extras.image(f"screenshots/{item.name}_{fecha}.png"))

            report.extras = extras












