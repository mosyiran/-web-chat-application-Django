from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send('{"type":"accept", "status":"accepted"}')
        print(self.scope.get("user"))
        print(self.scope.get("session"))

    def receive(self,text_data):
        print(text_data)
        self.send('{"type":"event_arrive", "status":"arrived"}')


    def disconnect(self, code):
        print("Hello , the connection is disconnected")