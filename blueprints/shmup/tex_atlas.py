from kivy.app import App

from kivy.graphics import Mesh
from kivy.graphics.instructions import RenderContext
from kivy.uix.widget import Widget

from main import load_atlas

class GlslDemo(Widget):
    def __init__(self, **kwargs):
        Widget.__init__(self, **kwargs)
        self.canvas = RenderContext(use_parent_projection=True)
        self.canvas.shader.source = 'tex_atlas.glsl'
        
        fmt = (
            (b'vCenter',        2,  'float'),
            (b'vPosition',      2,  'float'),
            (b'vTexCoords0',    2,  'float'),
        )
        
        texture, uvmap = load_atlas('icons.atlas')
        
        a = uvmap['icon_clock']
        vertices = (
            128, 128, -a.su, -a.sv, a.u0, a.v1,
            128, 128, a.su, -a.sv, a.u1, a.v1,
            128, 128, a.su, a.sv, a.u1, a.v0,
            128, 128, -a.su, a.sv, a.u0, a.v0,
        )
        indices = (0, 1, 2, 2, 3, 0)
        
        b = uvmap['icon_paint']
        vertices += (
            256, 256, -b.su, -b.sv, b.u0, b.v1,
            256, 256, b.su, -b.sv, b.u1, b.v1,
            256, 256, b.su, b.sv, b.u1, b.v0,
            256, 256, -b.su, b.sv, b.u0, b.v0,
        )
        indices += (4, 5, 6, 6, 7, 4)
        
        with self.canvas:
            Mesh(fmt=fmt, mode='triangles', vertices=vertices, indices=indices,
                 texture=texture)
            
class TexAtlasApp(App):
    def build(self):
        return GlslDemo() 

if __name__ == '__main__':
    TexAtlasApp().run()