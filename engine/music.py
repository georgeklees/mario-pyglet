import pyglet

# Music names
music = {'title':'../music/ending_credits.mp3'}

class MusicPlayer(pyglet.media.Player):
    def __init__(self, name):
        # Initialize the Player class
        super().__init__()

        # Load the music file
        source = pyglet.media.load(music[name])
        self.queue(source)
    def on_load(self):
        self.play()
    def on_unload(self):
        self.pause()
        
        
