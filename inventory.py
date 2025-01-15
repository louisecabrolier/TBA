"""classe inventaire"""
class Inventory:
    """
    Classe pour représenter un inventaire d'objets et de PNJ.
    """


    def __init__(self):
        self.items = {}  # Dictionnaire associant des items à leur nom
        self.npcs = {}   # Dictionnaire associant des PNJ à leur nom

    def add_item(self, item, hidden=False):
        """
        Ajoute un item à l'inventaire.
        :param item: Instance de la classe Item
        :param hidden: Indique si l'objet est caché
        """
        self.items[item.name.lower()] = {"item": item, "hidden": hidden}

    def get_visible_items(self):
        """
        Retourne uniquement les objets visibles dans l'inventaire.
        """
        return {name: data["item"] for name, data in self.items.items()
                if not data["hidden"]}

    def remove_item(self, item_name):
        """
        Retire un item de l'inventaire.
        :param item_name: Nom de l'item à retirer
        :return: L'item retiré ou None s'il n'existe pas
        """
        if item_name.lower() in self.items:
            return self.items.pop(item_name.lower())["item"]
        return None

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
                result += f" - {item.name} : {item.description} ({item.poids} kg)\n"
        # Ajout des PNJ
        for key, npc in self.npcs.items():
            result += f" - {key} : {npc.description}\n"
        return result.rstrip()

    def __setitem__(self, key, value):
        """Permet l'ajout d'un item avec la syntaxe de dictionnaire."""
        if hasattr(value, 'name'):
            self.items[value.name.lower()] = {"item": value, "hidden": False}
        else:
            self.items[key.lower()] = {"item": value, "hidden": False}

    def __getitem__(self, key):
        """Permet d'accéder à un item avec la syntaxe de dictionnaire."""
        return self.items[key.lower()]["item"]

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

    def reveal_item(self, item_name):
        """
        Révèle un item caché dans l'inventaire.
        :param item_name: Nom de l'item à révéler (en minuscules)
        """
        # Chercher l'item en ignorant la casse
        item_name_lower = item_name.lower()
        if item_name_lower in self.items:
            if self.items[item_name_lower]["hidden"]:
                self.items[item_name_lower]["hidden"] = False
                return True
            return False  # L'item n'était pas caché
        return False  # L'item n'existe pas dans l'inventaire
