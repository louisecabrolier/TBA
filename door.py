#Les portes de la cité

class Door:
    def __init__(self):
        self.is_open = False
        self.has_been_opened = False
        self.required_item = "Clef"

    def try_open(self, player_inventory):
        if self.required_item in player_inventory:
            self.is_open = True
            self.has_been_opened = True


        if self.required_item not in player_inventory:
            print("Vous ne pouvez pas entrer dans la cité sans la clé.")
        
        

    def close(self):
        self.is_open = False
