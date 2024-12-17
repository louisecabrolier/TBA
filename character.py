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
        #self.msgs = msgs if msgs is not None else []
        self.msgs = msgs.copy()  # Liste originale des messages
        self._current_msgs = msgs.copy()  # Liste des messages courants
        self.has_spoken = False  # Par défaut, le joueur n'a pas encore parlé

    def __str__(self):
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

    def get_msg(self):
        """
        Retourne cycliquement les messages du PNJ.
        """
        if not self._current_msgs:
            self._current_msgs = self.msgs.copy()
        
        if self._current_msgs:
            return self._current_msgs.pop(0)
        else:
            return "..."
    #déplacer les PNJ

    def move(self):
        """
        Déplace le PNJ avec une chance sur deux vers une pièce adjacente.
        Affiche des informations détaillées sur le déplacement.
        """
        if random.choice([True, False]):
            if DEBUG:
                print(f"DEBUG: {self.name} tente de se déplacer depuis {self.current_room.name}")
            
            possible_exits = []
            for direction, room in self.current_room.exits.items():
                if room is not None:
                    possible_exits.append((direction, room))
            
            if possible_exits:
                direction, new_room = random.choice(possible_exits)
                old_room = self.current_room.name
                
                if self.name.lower() in self.current_room.inventory.npcs:
                    del self.current_room.inventory.npcs[self.name.lower()]
                
                self.current_room = new_room
                new_room.inventory.add_npc(self)
                
                print(f"\n{'-'*50}")
                print(f"Déplacement de {self.name}:")
                print(f"- Départ de : {old_room}")
                print(f"- Direction : {direction}")
                print(f"- Arrivée à : {new_room.name}")
                print(f"{'-'*50}")
                
                return True
            if DEBUG:
                print(f"DEBUG: {self.name} ne peut pas se déplacer - aucune sortie disponible")
            return False
            
        print(f"\n{self.name} reste dans {self.current_room.name}")
        return False