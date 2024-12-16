#Définition de toutes les conditions de victoires
#si t'arrives au chateau
#tu dois avoir un objet specifique
#tu dois le donner à un garde
#que si t'as parlé à l'annonceur

class CheckVictory:

    
    
    def __init__(self):
        # Liste des méthodes qui vérifient chaque condition
        #changer aussi specific object par l'objet
        self.CONDITIONS_VICT = [
            self.in_the_right_room,
            self.has_specific_object,
            self.talk_to_garde,
            self.has_talked_to_annonceur
        ]
        # État des conditions au début
        self.is_in_chateau = False          # Le joueur est dans le château
        self.has_required_object = False   # Le joueur a l'objet requis (changer par le nom de l'objet)
        self.garde_talked = False          # Le joueur a parlé au garde
        self.annonceur_talked = False      # Le joueur a parlé à l'annonceur

    def in_the_right_room(self):
        """Vérifie si le joueur est dans le château"""
        return self.is_in_chateau
    
#remplacer specific_objet par l'objet de notre choix et pour required_object remplacer par objet_item
    def has_specific_object(self):
        """Vérifie si le joueur a l'objet spécifique"""
        return self.has_required_object

    def talk_to_garde(self):
        """Vérifie si le joueur a parlé au garde"""
        return self.garde_talked

    def has_talked_to_annonceur(self):
        """Vérifie si le joueur a parlé à l'annonceur"""
        return self.annonceur_talked

    def update_condition(self, condition_name, value):
        """Met à jour l'état d'une condition spécifique"""
        if condition_name == "chateau":
            self.is_in_chateau = value
        elif condition_name == "object": #remplacer object par l'objet choisi et required_object comme avant
            self.has_required_object = value
        elif condition_name == "garde":
            self.garde_talked = value
        elif condition_name == "annonceur":
            self.annonceur_talked = value