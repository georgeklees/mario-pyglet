import pyglet

class Button(pyglet.sprite.Sprite):
    def __init__(self, img, x, y, on_click, batch, group):
        # Initialize the Sprite class
        super().__init__(img=img, x=x, y=y, batch=batch, group=group)
        
        # On click event
        self.on_click = on_click

        # Internal state
        self.over = False
        self.clicked = False
    def on_load(self):
        pass
    def on_unload(self):
        pass
    def on_mouse_motion(self, x, y, dx, dy):
        # Check for collision
        if (x <= self.x + self.image.width) and (x >= self.x):
            if (y <= self.y + self.image.height) and (y >= self.y):
                self.over = True
                return

        if self.over:
            self.over = False
    def on_mouse_press(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            # Check for collision
            if (x <= self.x + self.image.width) and (x >= self.x):
                if (y <= self.y + self.image.height) and (y >= self.y):
                    self.clicked = True
                    self.on_click()
