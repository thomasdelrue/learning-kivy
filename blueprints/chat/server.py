from twisted.internet import protocol, reactor
from kivy.utils import escape_markup


transports = set()

colors = ['7F8C8D', 'C0392B', '2C3E50', '8E44AD', '27AE60']

class Chat(protocol.Protocol):
    def connectionMade(self):
        self.color = colors.pop()
        colors.insert(0, self.color)

    def dataReceived(self, data):
        transports.add(self.transport)
        
        s = data.decode()
        if ':' not in s:
            return
        
        user, msg = s.split(':', 1)
        
        for t in transports:
            if t is not self.transport:
                t.write('[b][color={}]{}:[/color][/b] {}'.format(self.color, user, escape_markup(msg)).encode())
                
class ChatFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Chat()
    
reactor.listenTCP(9096, ChatFactory())
reactor.run()