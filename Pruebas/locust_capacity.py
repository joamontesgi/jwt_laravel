from locust import HttpUser, task

class CapacityTestUser(HttpUser):
    @task
    def get_home(self):
        self.client.get("/api/categories_all")  

    @task
    def post_data(self):
        self.client.post("/api/categories", json={"name": "value"}) 
