class Room:


    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = set([])
   
    # Define the get_exit method.
    def get_exit(self, direction):


        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
   
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string
 
    def get_inventory(self):
        if len(self.inventory)>=1:
            print("\nLa pièce contient :")
            for v in self.inventory:
                print(f" - {v.name} : {v.description} ({v.poids} kg")
        else:
            print("\n Il n'y a rien ici.")


    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
