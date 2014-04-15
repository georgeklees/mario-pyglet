import pyglet

# Mario
super_mario = {'walk':\
               [pyglet.image.load('../sprites/heroes/mario/super/walk_0.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/walk_1.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/walk_2.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/walk_3.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/walk_4.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/walk_5.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/walk_6.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/walk_7.png')],\
               'jump':\
               [pyglet.image.load('../sprites/heroes/mario/super/jump_0.png')],\
               'attack':\
               [pyglet.image.load('../sprites/heroes/mario/super/attack_0.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/attack_1.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/attack_2.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/attack_3.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/attack_4.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/attack_5.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/attack_6.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/attack_7.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/attack_8.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/attack_9.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/attack_10.png')],\
               'dash':\
               [pyglet.image.load('../sprites/heroes/mario/super/dash_0.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/dash_1.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/dash_2.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/dash_3.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/dash_4.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/dash_5.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/dash_6.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/dash_7.png')],\
               'swim':\
               [pyglet.image.load('../sprites/heroes/mario/super/swim_0.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/swim_1.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/swim_2.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/swim_3.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/swim_4.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/swim_5.png'),\
                pyglet.image.load('../sprites/heroes/mario/super/swim_6.png')],\
               'duck':\
               [pyglet.image.load('../sprites/heroes/mario/super/duck_0.png')]}

fire_mario = {}

ice_mario = {}

racoon_mario = {}

tanooki_mario = {}  

propeller_mario = {}

penguin_mario = {}

blue_shell_mario = {}

mario = [super_mario, fire_mario, ice_mario, racoon_mario, tanooki_mario, propeller_mario, penguin_mario, blue_shell_mario]
