from room import Room

class Character:
    """
    Classe pour représenter les personnages non joueurs (PNJ).
    """
    def __init__(self, name, description, current_room, msgs):
        """
        Initialise un PNJ.

        :param name: Nom du personnage
        :param description: Description du personnage
        :param current_room: La pièce où se trouve le personnage
        :param msgs: Liste de messages associés au personnage
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs if msgs is not None else []

    def __str__(self) -> str:
        """
        Représentation textuelle du personnage.
        
        :return: Chaîne de caractères représentant le personnage
        """
        return f"{self.name} : {self.description}"

    def add_message(self, msg: str) -> None:
            """
            Ajoute un message à la liste des messages du personnage.
            
            Args:
                msg: Message à ajouter
            """
            self.msgs.append(msg)
    
    def get_messages(self) -> list:
        """
        Retourne la liste des messages du personnage.
        
        Returns:
            Liste des messages
        """
        return self.msgs
    