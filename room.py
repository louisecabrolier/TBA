from inventory import Inventory
class Room:



    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = Inventory()
        self.characters = []
   
    # Define the get_exit method.
    def get_exit(self, direction):


        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
   
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string
 
    #def get_inventory(self):
    #   inventory = []
        # Ajouter les items
    #   for item in self.items:
    #        inventory.append(f"- {item.name} : {item.description}")

        # Ajouter les personnages non joueurs
    #    for character in self.characters:
    #        inventory.append(f"- {character.name} : {character.description}")

        # Construire la sortie
     #   return "On voit:\n" + "\n".join(inventory) if inventory else "Il n'y a rien ici."


    def get_inventory(self):
        """
        Récupère l'inventaire de la pièce.

        :return: Chaîne de caractères listant les items.
        """
        return self.inventory.get_inventory()


    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
