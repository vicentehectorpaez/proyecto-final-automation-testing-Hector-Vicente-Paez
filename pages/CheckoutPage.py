from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class CheckoutPage(BasePage):

    # Locators del formulario de datos
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    # Locators de la confirmación final
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)

    def completar_formulario_envio(self, nombre, apellido, codigo_postal):
        self.escribir(self.FIRST_NAME, nombre)
        self.escribir(self.LAST_NAME, apellido)
        self.escribir(self.POSTAL_CODE, codigo_postal)
        self.click(self.CONTINUE_BUTTON)
      

    def finalizar_compra(self):            
               
        boton_finish = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.FINISH_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", boton_finish)
        boton_finish.click()
        

    def obtener_mensaje_exito(self):
          # 1. Primero esperamos a que la URL actual incluya "checkout-complete.html" 
        # (Esto garantiza que la navegación de la compra terminó de cargar)
        WebDriverWait(self.driver, 15).until(
            EC.url_contains("checkout-complete.html")
        )
        
        # 2. Recién después buscamos y retornamos el texto del mensaje
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text
        