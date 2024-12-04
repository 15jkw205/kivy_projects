# Jakob West
# Phase 2
# Project 3 - Basic Video Player
# December 3rd, 2024


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.video import Video

class VideoPlayerApp(App):
    def build(self):
        # Create a vertical layout
        layout = BoxLayout(orientation='vertical')
        
        # Add the video widget
        self.video = Video(source="output.mp4")
        layout.add_widget(self.video)
        
        # Add a Play/Pause button
        self.play_pause_button = Button(text="Play")
        self.play_pause_button.bind(on_press=self.toggle_video)
        layout.add_widget(self.play_pause_button)
        
        return layout
    
    def toggle_video(self, instance):
        # Play or pause the video based on its current state
        if self.video.state == "play":
            self.video.state = "pause"
            self.play_pause_button.text = "Play"
        else:
            self.video.state = "play"
            self.play_pause_button.text = "Pause"
            
if __name__ == "__main__":
    VideoPlayerApp().run() 