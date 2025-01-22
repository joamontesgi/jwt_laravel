import requests
import time

endpoint = 'http://127.0.0.1:8000/api/categories_all'

def realizar_solicitud():
    response = requests.get(endpoint)
    if response.status_code == 200:
        return True
    else:
        return False

# Número de solicitudes por nivel de carga
peticiones_nivel = 100
maximo_nivel = 10  # 1000 solicitudes en total

# Incrementar gradualmente la carga
for nivel in range(1, maximo_nivel + 1):
    print(f"Probando con {nivel * peticiones_nivel} solicitudes...")
    ini = time.time()
    # Realizar solicitudes en paralelo 
    cant_respues_exit = 0
    for _ in range(nivel * peticiones_nivel):
        if realizar_solicitud():
            cant_respues_exit += 1

    fin = time.time()

    print(f"Nivel {nivel}: {cant_respues_exit} solicitudes exitosas en {fin - ini:.2f} segundos.")
