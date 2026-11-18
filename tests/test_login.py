import pytest
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
import json
import os
import csv


# ejecucion con un archivo externo de json 

@pytest.mark.smoke
def test_login_page(driver, datos_login):
       
    #Instanciamos las pagina del login 
    login = LoginPage(driver)
    login.open_page()
    
    #extraemos los datos del JSON de forma dinamica 
    usuario = datos_login["user"]
    password = datos_login["password"]
    login.login_page(usuario, password)
   
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


#funcion auxiliar  para leer los datos del JSON externo 
def cargar_datos_login_parametrize():
    ruta_json = os.path.join(os.path.dirname(__file__), "..", "data", "login_data_parametrize.json")
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        #transformar los datos en una lista de tuplas para que pytest-parameytrize los entienda 
        return [(item["user"], item["password"], item["esperado"]) for item in datos]
    

@pytest.mark.parametrize("usuario, password, esperado", cargar_datos_login_parametrize())
def test_login_parametrizado(driver, usuario, password, esperado):
    login = LoginPage(driver)
    login.open_page()
    
    #intento de hacer login 
    login.login_page(usuario, password)
    
    if esperado == "success":
        #se valida que entre correctamente a saucedemo
        inventory = InventoryPage(driver)
        assert inventory.obtener_titulo_seccion() == "Products"
        
    elif esperado == "locked":
        #como este usuario esta blockeado, verificamos que aparezca el mensaje de error 
        # y al fallar este assert, el hook de paytest levantara la captura de pantalla automaticamente
        
        mensaje_error = login.obtener_mensaje_error()
        #assert "Epic sadface: Sorry, this user has been locked out." in mensaje_error
        assert mensaje_error == "Epic sadface: Sorry, this user has been locked out."
         