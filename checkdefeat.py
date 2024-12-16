#Définir les conditions de défaite
#si tu vas dans endroitinconnu

class CheckDefeat:

    
    

    def __init__(self):
        self.CONDITIONS_DEF = [
            self.endroitinconnu
        ]
        self.is_in_endroitinconnu = False
        
    def endroitinconnu(self):
        """Vérifie si le joueur est dans un endroit inconnu"""
        return self.is_in_endroitinconnu
    
    def update_condition(self, is_lost):
        """Met à jour l'état de la condition de défaite"""
        self.is_in_endroitinconnu = is_lost
