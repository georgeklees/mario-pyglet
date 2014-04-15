import pickle

import heroes

# Save files
savefiles = [None, None, None, None]
current_savefile = None

class SaveFile:
    def __init__(self, filename, mode):
        # Read
        if mode == 0:
            self.filename = filename
            self.read()
        # Create
        elif mode == 1:
            self.filename = filename
            self.create()
    def read(self):
        # Open and read the pickle
        try:
            data = pickle.load(open(self.filename, 'rb'))
        except IOError:
            raise IOError
            return

        # Read the data
        self.world = data[0]
        self.level = data[1]
        
        self.completed_levels = data[2]

        self.unlocked_characters = data[3]
        self.character = data[4]

        self.x = data[5]
        self.y = data[6]

        self.items = data[7]
    def write(self):
        # Create the data list
        data = [self.world, self.level, self.completed_levels, self.unlocked_characters, self.character, self.x, self.y, self.items]

        # Open and write to the pickle
        pickle.dump(data, open(self.filename, 'wb'))
    def create(self):
        # Create blank save data
        self.world = 0
        self.level = 0
        
        self.completed_levels = []

        self.unlocked_characters = [heroes.Mario]
        self.character = self.unlocked_characters[0]
        
        self.x = 0
        self.y = 0

        self.items = []

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

# Initialize savefiles
def init_savefiles():
    global savefiles

    for num in range(0, 4):
        try:
            savefiles[num] = SaveFile("../save/file_0" + str(num + 1) + ".pkl", 0)
        except IOError:
            savefiles[num] = None
