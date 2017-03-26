'''
Created on 16-okt.-2016

@author: thomas
'''

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')
    
TestApp().run()  
