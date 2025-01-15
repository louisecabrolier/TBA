from inventory import Inventory
"""Module gérant les salles du jeu d'aventure"""
from inventory import Inventory

class Room:
    """Classe représentant une salle/pièce du jeu avec ses attributs et méthodes"""

    def __init__(self, name, description, image = None, image_path = None):
        """"Initialise une nouvelle salle
        
        Args:
            name (str): Nom de la salle
            description (str): Description détaillée de la salle
            image (str, optional): Chemin vers l'image de la salle
        """
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = Inventory()
        self.characters = {}
        self.image = image
        self.image_path = image_path
        self.image = f"dessin/{image_path}"


    def get_exit(self, direction):
        """Retourne la salle dans la direction donnée si elle existe
        
        Args:
            direction (str): Direction souhaitée ('N', 'S', 'E', 'O', etc.)
        
        Returns:
            Room: Salle dans la direction donnée ou None si pas de sortie
        """
        return self.exits.get(direction)


    def get_exit_string(self):
        """Retourne une chaîne décrivant les sorties disponibles
        Returns:
            str: Liste des sorties disponibles
        """
        exit_string = "Sorties: "
        for direction in self.exits:
            if self.exits.get(direction) is not None:
                exit_string += direction + ", "
        return exit_string.strip(", ")

    def get_inventory(self):
        """Récupère l'inventaire de la pièce
        
        Returns:
            Inventory: L'inventaire de la pièce
        """
        return self.inventory

    def get_long_description(self):
        """Retourne une description détaillée de la salle
        
        Returns:
            str: Description complète incluant les sorties disponibles
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
