# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []

    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
      
        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
          # Si la commande est vide, ne rien faire
        if next_room == '':
            return None

        #ajt piece a l'historiqye avant de se déplacer
        if self.current_room is not None:
            self.history.append(self.current_room)
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        #print("Vous avez déjà visité les pièces suivantes :\n", self.get_history())
        return True
    
        

     # Méthode pour revenir en arrière
    def go_back(self):
        # Vérifier si l'historique est vide
        if not self.history:
            print("\nVous ne pouvez pas revenir en arrière, il n'y a pas d'historique !\n")
            return False
        
        # Mettre à jour la pièce actuelle avec la dernière pièce visitée
        self.current_room = self.history.pop()
        print(self.current_room.get_long_description())
        return True
        
    
    def get_history(self) :
        nomsendroits = [room.name for room in self.history]
        if nomsendroits:
            return "\n".join(nomsendroits)
        else:
            return "Aucune pièce visitée"
