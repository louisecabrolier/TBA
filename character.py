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
    
    def get_messages(self):
        """
        Retourne cycliquement les messages du PNJ.
        Si tous les messages ont été utilisés, recommence depuis le début.
        """
        if not self.messages:  # Si la liste des messages actifs est vide
            # Réinitialiser les messages en reprenant ceux de l'historique
            self.messages = self.message_history.copy()
            self.message_history = []
            
        # Prendre le premier message et le déplacer dans l'historique
        message = self.messages.pop(0)
        self.message_history.append(message)
        return message
    
    #déplacer les PNJ

    def move(self):
        """
        Déplace le PNJ selon les règles suivantes:
        - 50% de chance de se déplacer
        - Si déplacement, va dans une pièce adjacente au hasard
        
        Returns:
            bool: True si le PNJ s'est déplacé, False sinon
        """
        if DEBUG:
            print(f"DEBUG: Tentative de déplacement pour {self.name} depuis {self.current_room.name}")
        
        # Filtrer les sorties non-None
        possible_rooms = [room for room in self.current_room.exits.values() if room is not None]
        
        if not possible_rooms:  # Si pas de sorties valides
            if DEBUG:
                print(f"DEBUG: {self.name} ne peut pas se déplacer - aucune sortie disponible")
            return False
        
        # 50% de chance de se déplacer
        will_move = random.choice([True, False])
        
        if will_move:
            # Choisir une pièce au hasard parmi les sorties disponibles
            new_room = random.choice(possible_rooms)
            self.current_room = new_room
            if DEBUG:
                print(f"DEBUG: {self.name} s'est déplacé vers {new_room.name}")
            return True
        
        if DEBUG:
            print(f"DEBUG: {self.name} reste dans la salle {self.current_room.name}")
        return False
    

    #Interagir avec PNJ

    def talk(self):
        """
        Action déclenchée par la commande 'talk'
        Retourne le prochain message du PNJ
        """
        return self.get_messages()