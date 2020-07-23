import random
import uuid

from locust import HttpUser, task, between

apiUrl = "/webhooks/rest/webhook"  # Rasa Core REST API endpoint
# apiUrl = "/core/webhooks/rest/webhook" # Rasa X REST API endpoint


class RasaRestExplodeBrainUser(HttpUser):
    wait_time = between(3, 10)

    def on_start(self):
        self.name = str(uuid.uuid1())
        with open("questions.txt") as f:
            self.questions = f.readlines()

        with open("messages.txt") as f:
            self.messages = f.readlines()

    @task(1)
    def sayHello(self):
        payload = {"sender": self.name, "message": "Hello!"}
        self.client.post(apiUrl, json=payload)

    @task(2)
    def askQuestion(self):
        questionNumber = random.randint(0, len(self.questions)-1)
        question = self.questions[questionNumber]
        payload = {"sender": self.name, "message": question}
        self.client.post(apiUrl, json=payload)

    @task(3)
    def saySomethingRandom(self):
        messageNumber = random.randint(0, len(self.messages)-1)
        message = self.messages[messageNumber]
        payload = {"sender": self.name, "message": message}
        self.client.post(
            apiUrl, json=payload)
