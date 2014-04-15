import pyglet

import level

# Levels in each world
special = {"title":level.Level("../levels/special/title.txt", 0)}
world_1 = {1:level.Level("../levels/world_1_yoshis_island/1.txt", 0)}
world_2 = {}
world_3 = {}
world_4 = {}
world_5 = {}
world_6 = {}
world_7 = {}
world_8 = {}

worlds = [special, world_1, None, None, None, None, None, None, None]

# Key dictionary
keydict = {'left':False, 'right':False, 'up':False, 'down':False, 'select':False, 'back':False}

# World map update event loop
def update(dt):
    pass

# Key press event handlers
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.LEFT:
        keydict['left'] = True
    if symbol == pyglet.window.key.RIGHT:
        keydict['right'] = True
    if symbol == pyglet.window.key.UP:
        keydict['up'] = True
    if symbol == pyglet.window.key.DOWN:
        keydict['down'] = True
def on_key_release(symbol, modifiers):
    if symbol == pyglet.window.key.LEFT:
        keydict['left'] = False
    if symbol == pyglet.window.key.RIGHT:
        keydict['right'] = False
    if symbol == pyglet.window.key.UP:
        keydict['up'] = False
    if symbol == pyglet.window.key.DOWN:
        keydict['down'] = False

# Initialize worlds
def init_worlds():
    pass
