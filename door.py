#Les portes de la cité
'''porte de la cité'''
class Door:
    '''porte!!'''
    def __init__(self):
        '''door'''
        self.is_open = False
        self.has_been_opened = False
        self.required_item = "Clef"

    def try_open(self, player_inventory):
        '''essaye douvrir'''
        # Convertir la clé requise en minuscules pour la comparaison
        required_item_lower = self.required_item.lower()
        if required_item_lower in player_inventory:
            self.is_open = True
            self.has_been_opened = True
        else:
            print("Vous ne pouvez pas entrer dans la cité sans la clé.")

    def close(self):
        '''fermer'''
        self.is_open = False
