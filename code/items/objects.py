import pyglet

import sys
sys.path.append("..")

import objects

class ItemObject(objects.PhysicalObject):
    def __init__(self, *args, **kwargs):
        # Initialize the PhysicalObject class
        super().__init__(*args, **kwargs)

        # Create the item variables
        self.name = args[4]
        self.description = args[5]
        self.points = args[6]
        self.type = args[7] # 0 - Powerup, 1 - HP item, 2 - Attack item, 3 - Stat item
    def get_description(self):
        return self.description
