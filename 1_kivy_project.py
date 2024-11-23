# Jakob West
# Phase 1 
# Project 1 - Simple Kivy App
# November 19th, 2024

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical') # Create a vertical layout
        
        self.label = Label(text="Hello world!") # Create a label
        button = Button(text="Click Me!") # Create a button 
        
        # Bind the button's on_press event to a method
        button.bind(on_press=self.change_text)
        
        # Add the label and button to the layout
        layout.add_widget(self.label)
        layout.add_widget(button)
        
        return layout
    
    def change_text(self, instance):
        # Update the label text when the button is clicked
        self.label.text = "Button Clicked!" 

if __name__ == "__main__":
    MyApp().run()