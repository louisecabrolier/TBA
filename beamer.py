"""beamer pour la téléportation"""
from item import Item


class Beamer(Item):
    """classe Beamer"""

    def __init__(self, name="beamer", description="un objet magique de téléportation", poids=1):
        """init"""
        super().__init__(name, description, poids)
        self.teleporte_room = None


    def charge(self, current_room):
        """charger le beamer avec la pièce actuelle"""
        self.teleporte_room= current_room
        print(f"Le beamer est chargé dans le lieu : {current_room.name}")


    def teleporte(self, player):
        """se téléporter en utilisant le beamer"""
        if self.teleporte_room:
            print("Vous utilisez le beamer pour vous téléporter"
            f"dans le lieu: '{self.teleporte_room.name}'.")
            player.current_room = self.teleporte_room
            self.teleporte_room = None  # Réinitialisation après utilisation
        else:
            print("Le beamer n'est pas chargé avec une destination spécifique."
            "Impossible de l'utiliser.")


    def explain_usage(self):
        """Fournit une explication sur ce qu'est le beamer et comment l'utiliser."""
        return (
            f"{self.description}.\n"
            "Comment l'utiliser :\n"
            "- Chargez-le avec une pièce en utilisant la commande 'charge'.\n"
            "- Utilisez-le pour vous téléporter dans cette pièce avec la commande 'teleporte'.\n"
            "Attention : il doit être rechargé après chaque utilisation."
        )

    