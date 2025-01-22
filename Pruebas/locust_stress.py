from locust import HttpUser, task

class UsuarioTest(HttpUser):
    @task
    def get_home(self):
        self.client.get("/api/categories_all") 

    @task
    def post_data(self):
        # Realiza una solicitud POST con un cuerpo de JSON
        self.client.post("/api/categories", json={"name": "value"})  