# Jakob West
# Phase 1 
# Project 2 - Basic UI with multiple screens
# November 23rd, 2024


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Define the Login Screen
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        label = Label(text="Login Screen")
        button = Button(text="Go to Dashboard")
        
        # Bind the button to switch to the dashboard screen
        button.bind(on_press=self.go_to_dashboard)
        
        layout.add_widget(label)
        layout.add_widget(button)
        
        self.add_widget(layout)
        
    def go_to_dashboard(self, instance):
        self.manager.current = 'dashboard'
            
# Define the Dashboard Screen
class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
    
        label = Label(text="Welcome to the Dashboard!")
        button = Button(text="Back to Login")
        
        # Bind the button to switch to the login screen
        button.bind(on_press=self.go_to_login)
        
        layout.add_widget(label)
        layout.add_widget(button)
        
        self.add_widget(layout)
        
    def go_to_login(self, instance):
        self.manager.current = 'login'
                
# The main app
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        
        # Add screens to the ScreenManager
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        
        return sm
    
if __name__ == "__main__":
    MyApp().run()