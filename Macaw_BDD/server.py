from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from Macaw_Bot import get_response


class ChatServer(WebSocket):

    def handleMessage(self):
        message = self.data
        response = get_response(message)
        self.sendMessage(response)

    def handleConnected(self):
       print(self.address, 'connected')

    def handleClose(self):
       print(self.address, 'closed')


server = SimpleWebSocketServer('', 8000, ChatServer)
server.serveforever()