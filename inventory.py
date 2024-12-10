class Inventory:
    """
    Classe pour représenter un inventaire d'objets et de PNJ.
    """
    def __init__(self):
        self.items = {}  # Dictionnaire associant des items à leur nom
        self.npcs = {}   # Dictionnaire associant des PNJ à leur nom

    def __setitem__(self, key, value):
        """Permet l'ajout d'un item avec la syntaxe de dictionnaire."""
        self.items[key] = value

    def __getitem__(self, key):
        """Permet d'accéder à un item avec la syntaxe de dictionnaire."""
        return self.items[key]

    def add_item(self, item):
        """
        Ajoute un item à l'inventaire.
        :param item: Instance de la classe Item
        """
        self.items[item.name] = item

    def add_npc(self, npc):
        """
        Ajoute un PNJ à l'inventaire.
        :param npc: Instance de la classe NPC
        """
        self.npcs[npc.name] = npc

    def remove_item(self, item_name):
        """
        Retire un item de l'inventaire.
        :param item_name: Nom de l'item à retirer
        :return: L'item retiré ou None s'il n'existe pas
        """
        return self.items.pop(item_name, None)

    def remove_npc(self, npc_name):
        """
        Retire un PNJ de l'inventaire.
        :param npc_name: Nom du PNJ à retirer
        :return: Le PNJ retiré ou None s'il n'existe pas
        """
        return self.npcs.pop(npc_name, None)

    def get_inventory(self):
        """
        Produit une description des items et PNJ présents dans l'inventaire.
        :return: Une chaîne de caractères listant les items et PNJ.
        """
        if not self.items and not self.npcs:
            return "Il n'y a rien ici."

        result = "On voit:\n"
        
        # Ajout des items
        for key, item in self.items.items():
            result += f"        - {key} : {item.description} ({item.poids} kg)\n"
            
        # Ajout des PNJ
        for key, npc in self.npcs.items():
            result += f"        - {key} : {npc.description}\n"
            
        return result.rstrip()  # Enlève le dernier retour à la ligne
