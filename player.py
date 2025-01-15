"""classe joueur""" # pylint: disable=too-many-instance-attributes
from inventory import Inventory
from item import Item

class Player():
    """classe joueur"""
    def __init__(self, name):
        """blabla"""
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = Inventory()
        self.max_poids = 10  # Poids maximum en kg
        self.has_spoken_to_merchant = False  # Indique si le joueur a parlé au marchand
        self.has_talked_to_annonceur = False
        self.has_talked_to_garde = False
<<<<<<< HEAD
    """
    # Define the move method.
    def move(self, direction):
        
        direction = direction.lower()
        next_room = self.current_room.exits.get(direction)
=======

    # Define the move method.
    def move(self, direction):
        """ehh"""
        next_room = self.current_room.exits[direction]
>>>>>>> temp
        if next_room is None:
            return False
          # Si la commande est vide, ne rien faire
        if next_room == '':
            return None
        #ajt piece a l'historique avant de se déplacer
        if self.current_room is not None:
            self.history.append(self.current_room)
        # met la piece a la prochaine
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True
<<<<<<< HEAD
    """
=======

>>>>>>> temp
    #Méthode pour revenir en arrière
    def go_back(self):
        """Vérifier si l'historique est vide"""
        if not self.history:
            print("\nVous ne pouvez pas revenir en arrière, il n'y a pas d'historique !\n")
            return False
        # Mettre à jour la pièce actuelle avec la dernière pièce visitée
        self.current_room = self.history.pop()
        print(self.current_room.get_long_description())
        return True

    def get_history(self):
        """avoir lhistorique"""
<<<<<<< HEAD
        #nomsendroits = [room.name for room in self.history]
        #if nomsendroits:
            #return "\n".join(nomsendroits)
        #return "Aucune pièce visitée"
        if not self.history:
            return "Vous n'avez pas encore visité d'autres pièces."
            
        result = "Voici l'historique des pièces visitées :\n"
        for room in self.history:
            result += f"- {room.name}\n"
        return result.rstrip()

=======
        nomsendroits = [room.name for room in self.history]
        if nomsendroits:
            return "\n".join(nomsendroits)
        return "Aucune pièce visitée"
>>>>>>> temp

    def get_inventory(self):
        """
        Récupère l'inventaire du joueur.

        :return: Chaîne de caractères listant les items.
        """
        if not self.inventory.items:
            return "Votre inventaire est vide."
            
        result = "Votre inventaire contient :\n"
        for name, data in self.inventory.items.items():
            item = data["item"]
            result += f"- {item.name} : {item.description} ({item.poids} kg)\n"
        return result.rstrip()

<<<<<<< HEAD

=======
>>>>>>> temp
    def get_current_weight(self):
        """pr pas que l'inventaire nait une val maximum a 10kg"""
        return sum(data["item"].poids for data in self.inventory.items.values())

    def check(self):
        """ Affiche le contenu de l'inventaire du joueur """
        if not self.inventory.items:
            print("Votre inventaire est vide")
        else:
            print("Votre inventaire contient :")
            for item_name, item in self.inventory.items.items():
                print(f"- {item_name}: {item.description} ({item.poids} kg)")
    
    def add(self, item):
        """
        Ajoute un item à l'inventaire du joueur si le poids total ne dépasse pas le maximum.
        :param item: L'item à ajouter
        :return: True si l'ajout est réussi, False sinon
        """
        # Calculer le nouveau poids total
        new_weight = self.get_current_weight() + item.poids
        
        # Vérifier si l'ajout est possible
        if new_weight <= self.max_poids:
            self.inventory.add_item(item, hidden=False)
            return True
        return False
