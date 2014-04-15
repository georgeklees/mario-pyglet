import pyglet

colors = {"black":(0, 0, 0, 255)}

class Text(pyglet.text.Label):
    def __init__(self, text, size, color, x, y, batch, group):
        # Initialize the Label class
        super().__init__(text=text, font_name="Hey Gorgeous", font_size=size, color=colors[color], x=x, y=y, batch=batch, group=group)
    def on_load(self):
        pass
    def on_unload(self):
        pass

    
