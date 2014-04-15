import heroes.objects
import heroes.sprites

class Mario(heroes.objects.PlayerObject):
    def __init__(self, x, y, player_num, form, hp, attack, defense, jump_height, speed, batch):
        # Initialize the PlayerObject class
        super().__init__(img=heroes.sprites.mario[form]['walk'][0], x=x, y=y, batch=batch)

        # Player number and form
        self.player_num = player_num
        self.form = form # 0 - Super Mario, 1 - Fire Mario, 2 - Ice Mario, 3 - Racoon Mario, 4 - Tanooki Mario, 5 - Propeller Mario, 6 - Penguin Mario, 7 - Blue Shell Mario
        
        # HP and stats
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.jump_height = jump_height
        self.speed = speed

        # Images
        self.images = heroes.sprites.mario
