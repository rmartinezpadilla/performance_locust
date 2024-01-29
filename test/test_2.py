import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/api/users/2")
        #self.client.get("/world")
    
    @task
    def register_successful(self):
        self.client.post("/api/register", json={"email":"eve.holt@reqres.in", "password":"pistol"})


    @task      
    def register_unsuccessful(self):
        self.client.post("/api/login", json={"email":"sydney@fife"})
    
    @task
    def login_successful(self):
        self.client.post("/api/login", json={"email":"eve.holt@reqres.in", "password":"cityslicka"})


    @task      
    def login_unsuccessful(self):
        self.client.post("/api/register", json={"email":"peter@klaven"})
        
    @task
    def delayed_response(self):
        self.client
        for item_id in range(4):
            self.client.get(f"/api/users/?delay={item_id}")
            time.sleep(1) 