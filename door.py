#Les portes de la cité
# inutile en fait
class Door:
    def __init__(self):
        self.is_open = False
        #self.has_been_opened = False
        self.door_opened = False
        self.required_item = "Clef"

    def try_open(self, player_inventory):
        if self.required_item in player_inventory:
            self.is_open = True
            self.door_opened = True
            print("Les portes de la cité s'ouvrent...")
            print("Les portes de la cité sont maintenant scellées.")
        
        if self.required_item not in player_inventory:
            print("Vous ne pouvez pas entrer dans la cité sans la clé.")
        
        

    def close(self):
        if self.door_opened == True:
            self.is_open = False
            print("Les portes se referment derrière vous...")
        
