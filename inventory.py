class Inventory:
    """
    Classe pour représenter un inventaire d'objets.
    """
    def __init__(self):
        self.items = {}  # Dictionnaire associant des items à leur nom

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

    def remove_item(self, item_name):
        """
        Retire un item de l'inventaire.

        :param item_name: Nom de l'item à retirer
        :return: L'item retiré ou None s'il n'existe pas
        """
        return self.items.pop(item_name, None)

    def get_inventory(self):
        """
        Produit une description des items présents dans l'inventaire.

        :return: Une chaîne de caractères listant les items.
        """
        if not self.items:
            return "Il n'y a rien ici."
        
        inventory_list = [f"- {key} : {item.description} ({item.poids} kg)" for key, item in self.items.items()]
        return "La pièce contient :\n" + "\n".join(inventory_list)


    def get(self, item_name):
        return self.items.get(item_name)