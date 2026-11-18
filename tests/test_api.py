from utils.api_cliente import APIClient

def test_metodo_get_usuario():
    client = APIClient()
    
    # hacemos un peticion GET al usuario con ID 2
    response = client.get("posts/1")
    
    #validamos el status que sea codigo 200
    assert response.status_code == 200, f"Se esperaba codigo 200, se obtuvo {response.status_code}"
    
    #validar la estructura del JSON devuelto 
    data = response.json()
    assert "id" in data
    assert data["id"] == 1 
    assert "title" in data
    
def test_metodo_post_usuario():
    client = APIClient()
    payload = {
        "title" : "Prueba QA",
        "body": "Contenido de  prueba automatizado",
        "userId": 1
    } 
    
    #Hacemos la petision POST para crear un usuario 
    response = client.post("posts", payload)
    
    #validamos el status que el codigo sea 201(Created)
    assert response.status_code == 201, f"Se esperaba codigo 201, se obtiene codigo {response.status_code}"
    
    #validamos  que devuelva los datos enviados y un ID creado
    data = response.json()
    assert data["title"] == "Prueba QA"
    assert "id" in data 
     
     
def test_metodo_delete_usuario():
    client = APIClient()
    
    #Peticion DELETE a un recurso
    response = client.delete("posts/1")
    
    #JSONPlaceholder devuelve 200 al eliminar con exito simulado 
    assert response.status_code in [200, 204], f"Se esperaba codigo de exito, se obtuvo codigo {response.status_code}"
    