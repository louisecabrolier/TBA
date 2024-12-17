
class Item:
    def __init__(self, name, description, poids, hidden=False):
        self.name = name
        self.description = description
        self.poids = poids
        self.hidden = hidden
   
    def __str__(self):
        return f"{self.name} : {self.description} ({self.poids} kg)"

