import items.objects
import items.sprites

class Powerup(items.objects.ItemObject):
    def __init__(self, x, y, batch, name, description, internal_name, powerup_id):
        # Initialize the ItemObject class
        super().__init__(img=items.sprites.powerups[internal_name][0], x=x, y=y, batch=batch, name=name, description=description, points=1000, type=0)

        # Images
        self.images = items.sprites.powerups[internal_name]

class FireFlower(Powerup):
    def __init__(self, x, y, batch):
        # Initialize the Powerup class
        super().__init__(x=x, y=y, batch=batch, name="Fire Flower", description="Transform into Fire Mario! Press 1 to shoot fireballs!", internal_name="fire_flower", powerup_id=1)

class IceFlower(Powerup):
    def __init__(self, x, y, batch):
        # Initialize the Powerup class
        super().__init__(x=x, y=y, batch=batch, name="Ice Flower", description="Transform into Ice Mario! Press 1 to shoot ice balls!", internal_name="ice_flower", powerup_id=2)

class SuperLeaf(Powerup):
    def __init__(self, x, y, batch):
        # Initialize the Powerup class
        super().__init__(x=x, y=y, batch=batch, name="Super Leaf", description="Transform into Racoon Mario! Press 1 to swing your tail, press 2 while in midair to float down, and press 2 repeatedly after dashing to fly!", internal_name="super_leaf", powerup_id=3)

class TanookiSuit(Powerup):
    def __init__(self, x, y, batch):
        # Initialize the Powerup class
        super().__init__(x=x, y=y, batch=batch, name="Tanooki Suit", description="Transform into Tanooki Mario! Press 1 to swing your tail, press 2 while in midair to float down, press 2 repeatedly after dashing to fly, and press down to become an invincible statue!", internal_name="tanooki_suit", powerup_id=4)        

class PropellerMushroom(Powerup):
    def __init__(self, x, y, batch):
        # Initialize the Powerup class
        super().__init__(x=x, y=y, batch=batch, name="Propeller Mushroom", description="Transform into Propeller Mario! Shake the Wii Remote to fly!", internal_name="propeller_mushroom", powerup_id=5)

class PenguinSuit(Powerup):
    def __init__(self, x, y, batch):
        # Initialize the Powerup class
        super().__init__(x=x, y=y, batch=batch, name="Penguin Suit", description="Transform into Penguin Mario! Press 1 to shoot ice balls, and slide on the ground by pressing down while dashing!", internal_name="penguin_suit", powerup_id=6)

class BlueShell(Powerup):
    def __init__(self, x, y, batch):
        # Initialize the Powerup class
        super().__init__(x=x, y=y, batch=batch, name="Blue Shell", description="Transform into Blue Shell Mario! Start dashing in order to perform a shell dash, and press down to duck into your shell!", internal_name="blue_shell", powerup_id=7)
