from kivy.app import App
from kivy.base import EventLoop
from kivy.core.image import Image
from kivy.graphics import Mesh
from kivy.graphics.instructions import RenderContext
from kivy.uix.widget import Widget


class GlslDemo(Widget):
    def __init__(self, **kwargs):
        Widget.__init__(self, **kwargs)
        self.canvas = RenderContext(use_parent_projection=True)
        self.canvas.shader.source = 'basic.glsl'
        
        # Set up geometry here
        fmt = ( # Step 1
            (b'vPosition', 2, 'float'),
            (b'vTexCoords0', 2, 'float')
        )
        
        vertices = ( # Step 2
            0,      0,      0,   1,
            255,    0,      1,   1, 
            255,    255,    1,   0,
            0,      255,    0,   0, 
        )
        
        '''vertices = ( # Step 2
            0,      0,
            510,    0,
            510,    510,
            0,      510,
        )'''

        
        indices = (0, 1, 2, 2, 3, 0) # Step 3
        
        with self.canvas:
            Mesh(fmt=fmt, mode='triangles', # Step 4
                 indices=indices, vertices=vertices,
                 texture=Image('kivy.png').texture)
        
        

class GlslApp(App):
    def build(self):
        EventLoop.ensure_window()
        return GlslDemo()
    
    
if __name__ == '__main__':
    GlslApp().run()