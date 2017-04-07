from kivy.support import install_twisted_reactor
install_twisted_reactor()

from twisted.internet import reactor, protocol 

class ChatClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write('CONNECT')
        self.factory.app.on_connect(self.transport)
        
    def dataReceived(self, data):
        self.factory.app.on_message(data)


class ChatClientFactory(protocol.ClientFactory):
    protocol = ChatClient
    
    def __init__(self, app):
        self.app = app
        


        