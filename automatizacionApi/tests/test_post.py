import pytest
from automatizacionApi.metodos_http import (URL, obtener_publicaciones, crear_publicacion, eliminar_publicacion, obtener_endpoint_inexistente)
from utils.helpers import logger
from automatizacionApi.validaciones import validaciones
import requests

#metodo GET para obtener publicacion
def test_obtener_publicacion():
    logger.info("=== INICIO TEST GET PUBLICACION ===")
    respuesta = obtener_publicaciones()
    logger.info(f"Status code obtenido: {respuesta.status_code}")
    validaciones(respuesta, 200)

    datos = respuesta.json()
    logger.info(f"Respuesta JSON: {datos}")
    assert isinstance(datos, dict)
    for campo in ("userId", "id", "title", "body"):
        assert campo in datos, f"Falta el campo '{campo}' en la respuesta"

    assert isinstance(datos["userId"], int)
    assert datos["id"] == 1
    assert isinstance(datos["title"], str) and len(datos["title"]) > 0
    assert isinstance(datos["body"], str) and len(datos["body"]) > 0
    logger.info("GET validado correctamente")
          
    
#test de metodo post para enviar datos 
def test_crear_publicacion():
    logger.info("===INICIO TEST POST PUBLICACION===")
    respuesta = crear_publicacion()
    
    #assert respuesta.status_code == 201
    logger.info(f"Status del code obtenido: {respuesta.status_code}")
    validaciones(respuesta,201)
    
    datos = respuesta.json()
    
    logger.info(f"Respuesta JSON. {datos}")
    assert datos["title"] == "Mi primera vez creando una publicacion"
    assert datos["body"] == "Estoy aprendiendo APIS CON PYTHON Y REQUESTS"
    assert datos["userId"] == 1
    
    logger.info("POST validado correctamente")
    
    
#metodo DELETE para eliminar publicacion    
def test_eliminar_publicacion():
    logger.info("===INICIO TEST DELETE PUBLICACION===")
    respuesta = eliminar_publicacion()
    
    logger.info(f"Status Code obtenido: {respuesta.status_code}")
    validaciones(respuesta, 200)
    datos = respuesta.json()
    
    logger.info(f"Respuesta JSON: {datos}")    
    assert isinstance(datos,dict)
    
    logger.info("DELETE validado correctamente")
    
    
#metodo para obtener error de solicitud de datos     
def test_obtener_endpoint_inexistente():
    logger.info("===INICIO TEST ENDPOINT INEXISTENTE===")
    respuesta = obtener_endpoint_inexistente()
    
    logger.info(f"Status Code Obtenido: {respuesta.status_code}")    
    validaciones(respuesta, 404)
    
    logger.info("Se obtuvo correctamente un error 404")
    
# test para aplicar el flujo encadenado    
def test_flujo_encadenado_crear_y_eliminar():
    logger.info("=== INICIO FLUJO ENCADENADO POST -> DELETE ===")
    respuesta_creacion = crear_publicacion()
    validaciones(respuesta_creacion, 201)

    id_creado = respuesta_creacion.json().get("id")
    assert id_creado is not None, "No se devolvió un 'id' al crear la publicación"
    logger.info(f"Publicación creada con ID: {id_creado}")

    respuesta_eliminacion = requests.delete(f"{URL}/{id_creado}")
    logger.info(f"Status code al eliminar ID {id_creado}: {respuesta_eliminacion.status_code}")
    validaciones(respuesta_eliminacion, 200)
    logger.info("Flujo encadenado completado correctamente")
    

    