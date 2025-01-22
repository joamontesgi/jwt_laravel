import requests
import concurrent.futures

endpoint = 'http://127.0.0.1:8000/api/categories_all'

def realizar_solicitud(peticion):
    respuesta = requests.get(endpoint)
    if respuesta.status_code == 200:
        print(f"Solicitud #{peticion} exitosa!")
    else:
        print(f"Error en solicitud #{peticion}: {respuesta.status_code}")

# Número de solicitudes concurrentes (número de hilos)
num_peticiones = 30  

# Crear hilos para realizar solicitudes concurrentes
with concurrent.futures.ThreadPoolExecutor(max_workers=num_peticiones) as ejecutor:
    # Crear la lista (solicitudes)
    tareas_pendientes = []
    for i in range(num_peticiones):
        
        # Enviar la solicitud de manera asíncrona utilizando submit
        tarea_pendiente = ejecutor.submit(realizar_solicitud, i)
        
        # Guardar la tarea pendiente en la lista 'tareas_pendientes'
        tareas_pendientes.append(tarea_pendiente)

    # Se esperae a que todas las solicitudes terminen
    for tarea_pendiente in tareas_pendientes:
    
        # Llamar a result() paa bloquea hasta que la solicitud haya finalizado
        tarea_pendiente.result()
        
print("Todas las solicitudes han sido enviadas.")

