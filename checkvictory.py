#Définition de toutes les conditions de victoires
#si t'arrives au chateau
#tu dois avoir un objet specifique
#tu dois le donner à un garde
#que si t'as parlé à l'annonceur


#class CheckVictory:

    #def __init__(self):
        # Liste des méthodes qui vérifient chaque condition
        #self.CONDITIONS_VICT = [
            #self.in_the_right_room,
            #self.has_item,  # Utilise la méthode générique pour vérifier les objets
            #self.talk_to_garde,
            #self.has_talked_to_annonceur
        #]
        
        # État des conditions au début
        #self.is_in_chateau = False  # Le joueur est dans le château
        #self.items_required = {
            #"pierre": False,
            #"bague": False,
            #"potion": False
        #}
        #self.garde_talked = False  # Le joueur a parlé au garde
        #self.annonceur_talked = False  # Le joueur a parlé à l'annonceur

    #def in_the_right_room(self):
        #"""Vérifie si le joueur est dans le château"""
        #return self.is_in_chateau

    #def has_item(self, item_name):
        #"""Vérifie si le joueur possède un objet spécifique"""
        #return self.items_required.get(item_name, False)

    #def talk_to_garde(self):
        #"""Vérifie si le joueur a parlé au garde et l'a convaincu avec un objet"""
        #if "potion" in self.player.inventory.items:  # Vérifie si la potion est dans l'inventaire
            # Simule l'action de donner la potion au garde
            #print("Vous donnez la potion au garde pour le convaincre de vous laisser entrer.")
            #self.garde_talked = True  # Le garde te laisse passer
            # Tu peux aussi retirer la potion de l'inventaire si nécessaire
            #self.player.inventory.items.remove("potion")
        #else:
            #print("Le garde vous dit qu'il ne peut pas vous laisser entrer sans quelque chose pour le convaincre.")

    #def has_talked_to_annonceur(self):
        #"""Vérifie si le joueur a parlé à l'annonceur"""
        #return getattr(self.player, 'has_talked_to_annonceur', False)
    


    #def update_condition(self, condition_name, value):
        #"""Met à jour l'état d'une condition spécifique"""
        #if condition_name == "chateau":
            #self.is_in_chateau = value
        #elif condition_name in self.items_required:
            #self.items_required[condition_name] = value
        #elif condition_name == "garde":
            #self.garde_talked = value
        #elif condition_name == "annonceur":
            #if value:
                #print("Condition validée: Vous avez parlé à l'annonceur.")
            #else:
                #print("Condition non validée: Vous n'avez pas parlé à l'annonceur.")

    #def check_victory(self, player_inventory):
        #"""Vérifie si toutes les conditions de victoire sont remplies"""
        # Vérifie toutes les conditions
        #if all(condition() for condition in self.CONDITIONS_VICT):
            #return "\nVICTOIRE: Félicitations, vous avez accompli votre quête!"
        #return None

class CheckVictory:

    def __init__(self):
        # Liste des méthodes qui vérifient chaque condition
        self.CONDITIONS_VICT = [
            self.in_the_right_room,
            self.has_talked_to_annonceur,
            self.has_convinced_guard
        ]
        
        self.is_in_chateau = False
        self.garde_convinced = False
        self.annonceur_talked = False

    def in_the_right_room(self):
        """Vérifie si le joueur est dans le château"""
        return self.is_in_chateau

    def has_convinced_guard(self):
        """Vérifie si le joueur a convaincu le garde"""
        return self.garde_convinced

    def has_talked_to_annonceur(self):
        """Vérifie si le joueur a parlé à l'annonceur"""
        return self.annonceur_talked

    def update_condition(self, condition_name, value):
        """Met à jour l'état d'une condition spécifique"""
        if condition_name == "chateau":
            self.is_in_chateau = value
        elif condition_name == "garde":
            self.garde_convinced = value
        elif condition_name == "annonceur":
            self.annonceur_talked = value
    

    def check_victory(self):
        """Vérifie si toutes les conditions de victoire sont remplies"""
        return all(condition() for condition in self.CONDITIONS_VICT)