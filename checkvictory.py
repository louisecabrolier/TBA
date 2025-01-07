"""victoire"""
#Définition de toutes les conditions de victoires
#si t'arrives au chateau
#tu dois avoir un objet specifique
#tu dois le donner à un garde
#que si t'as parlé à l'annonceur


class CheckVictory:
    """classe qui donne les conditions de victoire"""

    def __init__(self):
        # Liste des méthodes qui vérifient chaque condition
        self.conditionvict = [
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
        return all(condition() for condition in self.conditionvict)
