#Les portes de la cité

class Door:
    def __init__(self):
        self.is_open = False
        self.has_been_opened = False
        self.required_item = "key"

    def try_open(self, player_inventory):
        if self.has_been_opened:
            return "Les portes de la cité sont maintenant scellées."
        
        if self.required_item not in player_inventory:
            return "Vous ne pouvez pas entrer dans la cité sans la clé."
        
        self.is_open = True
        self.has_been_opened = True
        return "Les portes de la cité s'ouvrent..."

    def close(self):
        self.is_open = False
        return "Les portes se referment derrière vous..."
