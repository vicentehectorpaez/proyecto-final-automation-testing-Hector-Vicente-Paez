from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import logging



class LoginPage(BasePage):

    URL = "https://www.saucedemo.com"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    MENSAJE_ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)
    

    def open_page(self):
        self.driver.get(self.URL)
        
    def login_page(self, username, password):      
        self.escribir(self.USERNAME, username)
        self.escribir(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        
    def obtener_mensaje_error(self):
        """espera a que aparezca el mensaje de error y retorna su texto"""
        #usando el metodo heredado de BasePage para obtener el texto del elemento 
        return self.obtener_texto(self.MENSAJE_ERROR)


