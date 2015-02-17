import os

import pyglet

import save
import graphics
import objects
import music

import heroes
import villains
import enemies
import npc
import items
import ui

# Current level and area
current_level = None
current_area = None

def str2list(string):
    string = string.replace('[','')
    string = string.replace(']','')

    return string.split(',')

class Background(pyglet.sprite.Sprite):
    def __init__(self, img, x, y, batch, group):
        # Initialize the Sprite class
        super().__init__(img=img, x=x, y=y, batch=batch, group=group)
    def on_load(self):
        pass
    def on_unload(self):
        pass

class Area:
    def __init__(self, filename, mode):
        # Read
        if mode == 0:
            # Create an object list and graphics batch for the area
            self.objects = []
            self.batch = pyglet.graphics.Batch()
            self.music = None
            
            self.background = pyglet.graphics.OrderedGroup(0)
            self.foreground = pyglet.graphics.OrderedGroup(1)
            
            self.read(filename)
        # Create
        elif mode == 1:
            pass
    def read(self, filename):
        """Read area data from a data file into an Area object"""
        # Open the area file
        fin = open(filename, 'r')

        # Read each object from the file
        for line in fin.readlines():
            line = line.split(' ')

            # Get the name, coordinates, and properties of the object
            name = line[0]
            x = float(line[1])
            y = float(line[2])
            properties = ''.join(line[3:]).strip('\n')

            # Create a blank object
            obj = None

            # Audio/visual stuff
            if name == "Background":
                obj = Background(img=pyglet.image.load(properties), x=x, y=y, batch=self.batch, group=self.background)
            if name == "MusicPlayer":
                self.music = music.MusicPlayer(name=properties)
                continue
            
            # Heroes
            if name == "Player":
                pass

            # Villains

            # Enemies

            # NPCs

            # Items

            # UI
            if name == "Text":
                properties = str2list(properties)

                print(properties)

                obj = ui.Text(text=properties[0], size=int(properties[1]), color=properties[2], x=x, y=y, batch=self.batch, group=self.foreground)
            if name == "Button":
                properties = str2list(properties)

                click_mod_func = properties[1].split('.')
                module = __import__(click_mod_func[0])
                on_click = eval("module." + click_mod_func[1])
                
                obj = ui.Button(img=pyglet.image.load(properties[0]), x=x, y=y, on_click=on_click, batch=self.batch, group=self.foreground)

            self.objects.append(obj)
    def play(self):
        """Switch to this area"""
        global current_area

        old_area = current_area
        current_area = self

        window = graphics.get_current_window()

        # Pop all the old handlers
        if old_area:
            for obj in old_area.objects:
                obj.on_unload()
                window.remove_handlers(obj)

        # Push all the new handlers
        for obj in self.objects:
            obj.on_load()
            window.push_handlers(obj)

        # Switch to the new graphics
        graphics.set_current_batch(self.batch)

        # If the old music is different, stop it and begin ours from 0
        if old_area:
            if self.music.sample_name != old_area.music.sample_name:
                old_area.music.pause()
                self.music.seek(0.0)
                self.music.play()
        else:
            self.music.play()
    def end(self):
        """End gameplay of this area"""
        window = graphics.get_current_window()
        
        for obj in self.objects:
            obj.on_unload()
            window.remove_handlers(obj)        

class Level:
    def __init__(self, filename, mode):
        # Read
        if mode == 0:
            # Create an areas list for the level
            self.areas = []
            
            self.read(filename)
        # Create
        elif mode == 1:
            pass
    def read(self, filename):
        """Read each area into memory"""
        # Open the area file
        fin = open(filename, 'r')

        # Read each object from the file
        for line in fin.readlines():
            # Create a new area
            area = Area(os.path.dirname(filename) + '/' + line.strip('\n'), 0)
            self.areas.append(area)
    def play(self):
        """Switch to the first area of this level"""
        global current_level
        
        current_level = self
        self.areas[0].play()
    def end(self):
        for area in self.areas:
            area.end()

# Key dictionary
keydict = {'left':False, 'right':False, 'up':False, 'down':False, 'select':False, 'back':False}

# Level update event loop
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

# Get the current level
def get_current_level():
    return current_level

# Get the current area
def get_current_area():
    return current_area

# Initialize levels
def init_levels():
    pass

            
