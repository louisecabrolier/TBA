from room import Room
import random
from config import DEBUG

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
    
    def move(self):
        """
        Déplace le personnage aléatoirement dans une pièce adjacente.
        Retourne True si le personnage s'est déplacé, False sinon.
        """
        # Décider si le personnage se déplace (chance sur deux)
        if DEBUG:
            print(f"DEBUG: Tentative de déplacement pour {self.name} dans la salle {self.current_room.name}.")

        if random.choice([True, False]):
            # Si le personnage se déplace, choisir une salle voisine au hasard
            possible_rooms = list(self.current_room.exits.values())  # Liste des salles adjacentes
            if possible_rooms:
                new_room = random.choice(possible_rooms)  # Choisir une salle adjacente au hasard
                self.current_room = new_room  # Déplacer le personnage dans la nouvelle salle
                
                if DEBUG:
                    print(f"DEBUG: {self.name} s'est déplacé dans la salle {new_room.name}.")
                return True  # Le personnage s'est déplacé
            else:
                if DEBUG:
                    print(f"DEBUG: {self.name} n'a pas de salle voisine pour se déplacer.")
        else:
            if DEBUG:
                print(f"DEBUG: {self.name} n'a pas bougé cette fois.")
        
        return False  # Le personnage n'a pas bougé
    