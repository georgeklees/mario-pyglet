import pyglet

import save
import worlds
import level
import graphics

# Current location
location = 1 # 0 - World Map, 1 - Level

# Update event loop
def update(dt):
    if location == 0:
        worlds.update(dt)
    elif location == 1:
        level.update(dt)
    else:
        print("Invalid location")
        
        while True:
            pass

# Initialize the savefiles, worlds, levels, and graphics
save.init_savefiles()
worlds.init_worlds()
level.init_levels()
graphics.init_graphics()

# Begin playing the title screen
worlds.worlds[0]["title"].play()

# Start the event loop
pyglet.clock.schedule_interval(level.update, 1/120)
pyglet.app.run()
    
