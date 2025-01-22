import requests
import time
import threading

endpoint = 'http://127.0.0.1:8000/api/categories_all'

def realizar_solicitud():
    respuesta = requests.get(endpoint)
    if respuesta.status_code == 200:
        print("Solicitud exitosa!")
    else:
        print(f"Error: {respuesta.status_code}")

# Número de solicitudes 
num_peticiones = 1000 

# Realizar solicitudes en variso hilos
ini = time.time()
hilos = []
for _ in range(num_peticiones):
    hilo = threading.Thread(target=realizar_solicitud)
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

fin = time.time()

print(f"Prueba de estrés completada. Tiempo total: {fin - ini} segundos.")
