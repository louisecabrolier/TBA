#Définir les conditions de défaite
#si tu vas dans endroitinconnu

class CheckDefeat:

    
    

    def __init__(self):
        self.CONDITIONS_DEF = [
            self.endroitinconnu, self.talk_to_villageois
        ]
        self.is_in_endroitinconnu = False
        self.has_talked_to_villageois = False
        
    def endroitinconnu(self):
        """Vérifie si le joueur est dans un endroit inconnu"""
        return self.is_in_endroitinconnu
    
    def talk_to_villageois(self):
        """ Vérifie si le joueur a parlé au villageois"""
        return self.has_talked_to_villageois
    
    def update_condition(self, is_lost):
        """Met à jour l'état de la condition de défaite"""
        self.is_in_endroitinconnu = is_lost
        self.has_talked_to_villageois = is_lost
