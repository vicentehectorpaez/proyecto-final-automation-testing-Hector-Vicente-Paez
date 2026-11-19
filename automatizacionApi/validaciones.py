def validaciones(respuesta,status_code):
    assert respuesta.status_code == status_code, (f"Se esperaba el codigo http:{status_code},"f"pero, se recibio {respuesta.status_code}"
    )
    
