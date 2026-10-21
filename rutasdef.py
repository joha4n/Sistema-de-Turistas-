# Módulo: rutas.py
# Propósito: Gestión y lógica preliminar de rutas turísticas

def validar_puntos_ruta(origen: str, destino: str) -> tuple:
    """
    Valida que el punto de origen y destino no estén vacíos 
    y sean diferentes entre sí. Retorna (valido: bool, mensaje: str).
    """
    if not origen or not destino:
        return False, "Error: El origen y el destino no pueden estar vacíos."
    
    if origen.strip().lower() == destino.strip().lower():
        return False, "Error: El origen y el destino no pueden ser el mismo lugar."
        
    return True, "Puntos validados correctamente."


def calcular_distancia_preliminar(origen: str, destino: str) -> float:
    """
    Función base para consultar de forma preliminar el trayecto 
    entre dos puntos turísticos de Manabí.
    """
    print(f"Procesando ruta preliminar desde '{origen}' hasta '{destino}'...")
    
    #simulado
    distancia_simulada = 0.0 
    
    return distancia_simulada


def gestionar_consulta_ruta(origen: str, destino: str) -> dict:
    """
    Coordina la validación y el cálculo preliminar de la ruta.
    """
    es_valido, mensaje = validar_puntos_ruta(origen, destino)
    
    if not es_valido:
        print(mensaje)
        return None
        
    distancia = calcular_distancia_preliminar(origen, destino)
    
    resumen = {
        "origen": origen,
        "destino": destino,
        "distancia_estimada": distancia,
        "estado": "Validación superada (Pendiente de integración con grafos)"
    }
    
    return resumen