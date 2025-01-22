from locust import HttpUser, task

# Definir una clase de usuario que simula las interacciones de los usuarios en la API
class ApiUser(HttpUser):
    # Definir la tarea a realizar
    @task
    def get_home(self): #self es una referencia a la instancia de la clase
        self.client.get("/api/categories_all")  

    @task
    def post_data(self):
        self.client.post("/api/categories", json={"name": "value"}) 
