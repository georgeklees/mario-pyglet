import items.objects
import items.sprites

class HPItem(items.objects.ItemObject):
    def __init__(self, x, y, batch, name, description, points, hp, internal_name):
        # Initialize the ItemObject class
        try:
            super().__init__(img=items.sprites.raw_hp_items[internal_name][0], x=x, y=y, batch=batch, name=name, description=description, points=points, type=1)

            # Images
            self.images = items.sprites.raw_hp_items[internal_name]
        except KeyError:
            super().__init__(img=items.sprites.recipe_hp_items[internal_name][0], x=x, y=y, batch=batch, name=name, description=description, points=points, type=1)

            # Images
            self.images = items.sprites.recipe_hp_items[internal_name]

        # HP
        self.hp = hp
        
