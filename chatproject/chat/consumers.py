from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send('{"type":"accept", "status":"accepted"}')
        print(self.scope.get("user"))
        print(self.scope.get("user"),id)
        print(self.scope.get("user").first_name)
        print(self.scope.get("user").last_name)

        print(self.scope.get("session"))
        self.scope.get("session")["get_me_from_consumer"] = "Hi I am mohsen"
        print(self.scope.get("url_route").get("kwargs").get("name"))

    def receive(self,text_data):
        print(text_data)
        self.send('{"type":"event_arrive", "status":"arrived"}')


    def disconnect(self, code):
        print("Hello , the connection is disconnected")