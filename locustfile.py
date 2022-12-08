from locust import HttpUser, task


class HelloWorldUser(HttpUser):

    def on_start(self):
        print("starting Locust tests...\n")

    @task
    def get_tests(self):
        self.client.get("/misc/stats")
        self.client.get("/")
        self.client.get("/rest/api/pages")
        self.client.get("/rest/api/pages/")
        self.client.get("/rest/api/stats/pages")


