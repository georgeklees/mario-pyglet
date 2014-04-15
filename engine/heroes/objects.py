import pyglet

import sys
sys.path.append("..")

import objects

class PlayerObject(objects.LivingObject):
    def __init__(self, *args, **kwargs):
        # Initialize the LivingObject class
        super().__init__(*args, **kwargs)

        # Create the key dictionary
        self.keys = {'left':False, 'right':False, 'up':False, 'down':False, 'jump':False, 'special':False}

        # Player number and form
        self.player_num = 1
        self.form = 0
        
        # Create the player move variables   
        self.walking = False
        self.jumping = False
        self.dashing = False
        self.swimming = False
        self.ducking = False

        self.walk_image = 0
        self.jump_image = 0
        self.dash_image = 0
        self.swim_image = 0
    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.key.LEFT:
            self.keys['left'] = True
        if symbol == pyglet.key.RIGHT:
            self.keys['right'] = True
        if symbol == pyglet.key.UP:
            self.keys['up'] = True
        if symbol == pyglet.key.DOWN:
            self.keys['down'] = True
        if symbol == pyglet.key.SPACE:
            self.keys['jump'] = True
    def on_key_release(self, symbol, modifiers):
        if symbol == pyglet.key.LEFT:
            self.keys['left'] = False
        if symbol == pyglet.key.RIGHT:
            self.keys['right'] = False
        if symbol == pyglet.key.UP:
            self.keys['up'] = False
        if symbol == pyglet.key.DOWN:
            self.keys['down'] = False
        if symbol == pyglet.key.SPACE:
            self.keys['jump'] = False
    def jump(self):
        pass
    def walk(self, direction):
        pass
    def dash(self, direction):
        pass
    def swim(self, direction):
        pass
    def duck(self):
        pass
    def update(self, dt):
        # Update the LivingObject class
        super().update(dt)
