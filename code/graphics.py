import pyglet

# Window, objects, and batch
window = pyglet.window.Window(caption="Super Mario", width=640, height=480)
batch = None

# Window events
@window.event
def on_draw():
    window.clear()
    batch.draw()

# Get the current window
def get_current_window():
    return window

# Set the current batch
def set_current_batch(new_batch):
    global batch
    
    batch = new_batch

def init_graphics():
    # Register the window event handlers
    window.push_handlers(on_draw)
