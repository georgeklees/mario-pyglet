import pyglet

# Music sample names
music = {'title':'../music/ending_credits.mp3'}

class MusicPlayer(pyglet.media.Player):
    def __init__(self, name):
        # Initialize the Player class
        super().__init__()

        # Load the sample and queue it on our player
        source = pyglet.media.load(music[name])
        self.queue(source)

        # Set our sample name
        self.sample_name = name
        
        
