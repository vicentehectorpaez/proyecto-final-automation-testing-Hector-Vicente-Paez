import pytest
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By
import json


@pytest.mark.regression
def test_verificar_titulo_pagina(driver, datos_login):

    login = LoginPage(driver)
    login.open_page()
    
    usuario = datos_login["user"]
    password = datos_login["password"]   
    login.login_page(usuario, password) 
    inventory = InventoryPage(driver)

    assert inventory.obtener_titulo_page() == "Swag Labs"
    assert inventory.obtener_titulo_seccion() == "Products"

@pytest.mark.regression
def test_verificar_producto(driver, datos_login):

    login = LoginPage(driver)
    login.open_page()
    
    usuario = datos_login["user"]
    password = datos_login["password"]
    login.login_page(usuario, password)

    inventory = InventoryPage(driver)
    cantidad_producto = inventory.obtener_producto()

    assert len(cantidad_producto) > 0  


def test_verificar_elementos_interfaz(driver, datos_login):

    login = LoginPage(driver)
    login.open_page()

    usuario = datos_login["user"]
    password = datos_login["password"]
    login.login_page(usuario, password)

    inventory = InventoryPage(driver)

    assert inventory.obtener_menu_hamburguesa()
    assert inventory.obtener_filtro()

# test para mostrar si los productos estan ordenados de menor a mayor pro precio 
@pytest.mark.smoke
def test_ordenar_por_precio(driver, datos_login):

    Login = LoginPage(driver)
    Login.open_page()

    usuario = datos_login["user"]
    password = datos_login["password"]
    Login.login_page(usuario, password)

    inventory = InventoryPage(driver)
    inventory.ordenar_precio_menor_mayor()

    assert inventory.obtener_filtro_seleccionado() == "Price (low to high)"


# test para ver si esta ordenado los precios de menor a mayor 


@pytest.mark.smoke
def test_ordenar_por_precio_menor_mayor(driver, datos_login):

    Login = LoginPage(driver)
    Login.open_page()
    
    usuario = datos_login["user"]
    password = datos_login["password"]
    Login.login_page(usuario, password)

    inventory = InventoryPage(driver)
    inventory.ordenar_precio_menor_mayor()
    precio = inventory.obtener_precios()

    assert precio == sorted(precio)
    
    
        
    
