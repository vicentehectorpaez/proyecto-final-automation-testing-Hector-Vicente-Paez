from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import logging


class InventoryPage:

    TITULO = (By.CLASS_NAME, "title")
    TITULO_SECCION = (By.CLASS_NAME, "title")
    PRIMER_PRODUCTO = (By.CLASS_NAME, "inventory_item_name")
    MENU_HAMBURGUESA = (By.ID, "react-burger-menu-btn")
    FILTRO = (By.CLASS_NAME, "product_sort_container")
    FILTRO_PRODUCTOS = (By.CLASS_NAME, "product_sort_container")
    PRECIO = (By.CLASS_NAME, "inventory_item_price")
    ITEMS_INVENTARIO = (By.CLASS_NAME, 'inventory_item')
    BTN_AGREGAR_CARRITO = (By.TAG_NAME, 'button')


    def __init__(self, driver):
        self.driver = driver


    def obtener_titulo_page(self):        
        return self.driver.title

    def obtener_titulo_seccion(self):        
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.TITULO_SECCION))
        return self.driver.find_element(*self.TITULO_SECCION).text
    
    def obtener_producto(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.PRIMER_PRODUCTO))
        return self.driver.find_elements(*self.PRIMER_PRODUCTO)

    def obtener_menu_hamburguesa(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.MENU_HAMBURGUESA))
        return self.driver.find_element(*self.MENU_HAMBURGUESA).is_displayed()

    def obtener_filtro(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FILTRO))
        return self.driver.find_element(*self.FILTRO).is_displayed()

    
    #metodo para selecionar el elemento del dropdown
    def ordenar_precio_menor_mayor(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FILTRO_PRODUCTOS))
        
        dropdown = Select(self.driver.find_element(*self.FILTRO_PRODUCTOS))

        dropdown.select_by_visible_text("Price (low to high)")

    #metodo para leer los seleccionado 
    def obtener_filtro_seleccionado(self):

        dropdown = Select(self.driver.find_element(*self.FILTRO_PRODUCTOS))

        return dropdown.first_selected_option.text


    # definir metodos para selecionar los precios y asiganrlos a un vector 
    def obtener_precios(self):
        elementos = self.driver.find_elements(*self.PRECIO)   

        precios = []

        for elemento in elementos:

            precio = elemento.text

            precio = precio.replace("$", "")

            precios.append(float(precio))

        return precios
    
    
    
   