class Inventory:
    """
    Classe pour représenter un inventaire d'objets et de PNJ.
    """
    def __init__(self):
        self.items = {}  # Dictionnaire associant des items à leur nom
        self.npcs = {}  # Dictionnaire associant des PNJ à leur nom

    def add_item(self, item, hidden=False):
        """
        Ajoute un item à l'inventaire.
        :param item: Instance de la classe Item
        :param hidden: Indique si l'objet est caché
        """
        # Store the item and its hidden status as a dictionary
        self.items[item.name] = {"item": item, "hidden": hidden}

    def get_visible_items(self):
        """
        Retourne uniquement les objets visibles dans l'inventaire (ceux dont 'hidden' est False).
        """
        return {name: data["item"] for name, data in self.items.items() if not data["hidden"]}

    def remove_item(self, item_name):
        """
        Retire un item de l'inventaire.
        :param item_name: Nom de l'item à retirer
        :return: L'item retiré ou None s'il n'existe pas
        """
        return self.items.pop(item_name, None)

    def reveal_item(self, item_name):
        """
        Révèle un item caché.
        :param item_name: Nom de l'item à révéler
        """
        if item_name in self.items:
            self.items[item_name]["hidden"] = False

    def get_inventory(self):
        """
        Produit une description des items et PNJ présents dans l'inventaire.
        :return: Une chaîne de caractères listant les items et PNJ.
        """
        if not self.items and not self.npcs:
            return "Il n'y a rien ici."
        
        result = "On voit:\n"
        # Ajout des items
        for name, data in self.items.items():
            if not data["hidden"]:
                item = data["item"]
                result += f" - {name} : {item.description} ({item.poids} kg)\n"
        
        # Ajout des PNJ
        for key, npc in self.npcs.items():
            result += f" - {key} : {npc.description}\n"
        
        return result.rstrip()  # Enlève le dernier retour à la ligne

    def __setitem__(self, key, value):
        """Permet l'ajout d'un item avec la syntaxe de dictionnaire."""
        self.items[key] = {"item": value, "hidden": False}

    def __getitem__(self, key):
        """Permet d'accéder à un item avec la syntaxe de dictionnaire."""
        return self.items[key]["item"]

    def add_npc(self, npc):
        """
        Ajoute un PNJ à l'inventaire.
        :param npc: Instance de la classe NPC
        """
        self.npcs[npc.name] = npc

    def remove_npc(self, npc_name):
        """
        Retire un PNJ de l'inventaire.
        :param npc_name: Nom du PNJ à retirer
        :return: Le PNJ retiré ou None s'il n'existe pas
        """
        return self.npcs.pop(npc_name, None)