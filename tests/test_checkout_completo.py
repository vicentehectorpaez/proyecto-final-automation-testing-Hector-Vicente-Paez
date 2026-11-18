import pytest
from faker import Faker
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
import json

@pytest.mark.regression
def test_flujo_compra_completo(driver, datos_login):
    # Instanciamos Faker para generar datos aleatorios de envío
    fake = Faker("es_ES")
    nombre = fake.first_name()
    apellido = fake.last_name()
    codigo_postal = fake.postcode()

    # 1. Login
    login = LoginPage(driver)
    login.open_page()
    usuario = datos_login["user"]
    password = datos_login["password"]
    login.login_page(usuario, password)

    # 2. Agregar producto y entrar al carrito
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    
    inventory_page.obtener_producto() # Espera a que carguen los productos
    cart_page.agregar_primer_producto_al_carrito()
    cart_page.ir_al_carrito()

    # 3. Iniciar checkout
    cart_page.hacer_checkout()

    # 4. Completar datos con Faker y continuar
    checkout_page = CheckoutPage(driver)
    checkout_page.completar_formulario_envio(nombre, apellido, codigo_postal)

    # 5. Hacer click en Finish (Paso clave en el resumen de compra)
    checkout_page.finalizar_compra()

    # 6. Validar mensaje de éxito
    mensaje_esperado = "Thank you for your order!"
    assert checkout_page.obtener_mensaje_exito() == mensaje_esperado, f"El mensaje no coincide. Se obtuvo: {checkout_page.obtener_mensaje_exito()}"