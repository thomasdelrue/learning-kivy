from kivy.app import App
from kivy.support import install_twisted_reactor
from kivy.utils import escape_markup

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
        
		
class ChatApp(App):
    def connect(self):
		host = self.root.ids.server.text
		self.nick = self.root.ids.nickname.text
		reactor.connectTCP(host, 9096, ChatClientFactory(self))
		
    def on_connect(self, conn):
		self.conn = conn
		self.root.current = 'chatroom'
		
    def send_msg(self):
		msg = self.root.ids.message.text
		self.conn.write(('%s:%s' % (self.nick, msg)).encode())
		self.root.ids.chat_logs.text += ('[b][color=2980B9]{}:[/color][/b] {}\n'.format(self.nick, escape_markup(msg)))
		self.root.ids.message.text = ''
		
    def on_message(self, msg):
		self.root.ids.chat_logs.text += msg +'\n'
		
    def disconnect(self):
		if self.conn:
			self.conn.loseConnection()
			del self.conn
		self.root.current = 'login'
		self.root.ids.chat_logs.text = ''
	

if __name__ == '__main__':
    ChatApp().run()