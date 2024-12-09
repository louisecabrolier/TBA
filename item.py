import item
class Item:
    def __init__(self, name, description, poids):
        self.name = name
        self.description = description
        self.poids = poids
   
    def __str__(self):
        return f"{self.name} : {self.description} ({self.poids} kg)"
