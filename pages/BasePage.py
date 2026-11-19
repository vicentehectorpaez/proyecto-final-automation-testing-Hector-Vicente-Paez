from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import logger



class BasePage:

    def __init__(self,driver):
        self.driver = driver

          
    # agrego el metodo escribir texto en cualquier input 
    def escribir(self, locator, texto):
        logger.info(f"Escribiendo '{texto}' en {locator}")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(texto)

    # agrego el metodo obtener  texto de cualquier elemento 
    def obtener_texto(self, locator):
        logger.info(f"Obteniendo texto de {locator}")
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    #agrego el metodo evento click de cualquier boton  
    def click(self, locator):
        logger.info(f"Click en Locator {locator}") # agrega logs en el ejecucion del test
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()


    # metodo para subir archivo 
    def subir_archivo(self, locator, ruta):

        logger.info(f"Subiendo archivo {ruta}")

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

        self.driver.find_element(*locator).send_keys(ruta)

# Método para hacer scroll hasta un elemento de forma segura
    def hacer_scroll(self, locator):
        logger.info(f"Haciendo scroll hasta el elemento {locator}")
        elemento = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elemento)
        return elemento