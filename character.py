class Character:
    """
    Classe pour représenter les personnages non joueurs (PNJ).
    """
    def __init__(self, name, description, current_room, msgs):
        """
        Initialise un personnage.

        :param name: Nom du personnage
        :param description: Description du personnage
        :param current_room: La pièce où se trouve le personnage
        :param msgs: Liste de messages associés au personnage
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        """
        Représentation textuelle du personnage.
        
        :return: Chaîne de caractères représentant le personnage
        """
        return f"{self.name} : {self.description}"
