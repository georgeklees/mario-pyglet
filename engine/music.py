import pyglet

# Music sample names
music = {'title':'../music/ending_credits.mp3'}

# Current music player
#current_player = None

class MusicPlayer(pyglet.media.Player):
    def __init__(self, name):
        # Initialize the Player class
        super().__init__()

        # Load the sample and queue it on our player
        source = pyglet.media.load(music[name])
        self.queue(source)

        # Set our sample name
        self.sample_name = name
    def play(self):
        global current_player

        # If other music is playing, switch to our track
        try:
            if self.sample_name != current_player.sample_name:
                current_player.pause()
                self.seek(0.0)
                super().play()
                current_player = self
        except:
            super().play()
            current_player = self
