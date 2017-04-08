from kivy.app import App
from kivy.clock import Clock
from kivy.loader import Loader

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode
    
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
    

class RemoteDesktopApp(App):
    def connect(self):
        self.url = ('http://%s:7080/desktop.jpeg' %
                    self.root.ids.server.text)
        self.send_url = ('http://%s:7080/click?' %
                    self.root.ids.server.text)
        self.reload_desktop()
        
    def reload_desktop(self, *args):
        desktop = Loader.image(self.url, nocache=True)
        desktop.bind(on_load=self.desktop_loaded)
    
    def desktop_loaded(self, desktop):
        if desktop.image.texture:
            self.root.ids.desktop.texture = desktop.image.texture
            
        Clock.schedule_once(self.reload_desktop, 1)
        
        if self.root.current == 'login':
            self.root.current = 'desktop'
            
    def send_click(self, event):
        params = {'x': int(event.x),
                  'y': int(self.root.ids.desktop.size[1] - event.y)}
        urlopen(self.send_url + urlencode(params))
    
if __name__ == '__main__':
    RemoteDesktopApp().run()