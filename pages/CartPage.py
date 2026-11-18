from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CartPage(BasePage):
    
    # definimod nuestros locator 
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    
    # Selector para agregar el primer producto del inventario (por si el test arranca desde ahí)
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".inventory_item:first-child button")

    def __init__(self, driver):
        super().__init__(driver)

    def agregar_primer_producto_al_carrito(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def ir_al_carrito(self):
        self.click(self.CART_BUTTON)

    def hacer_checkout(self):
        self.click(self.CHECKOUT_BUTTON)