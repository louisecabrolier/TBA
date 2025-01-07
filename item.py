"""items""" # pylint: disable=too-few-public-methods
class Item:
    """classe item"""
    def __init__(self, name, description, poids, hidden=False):
        self.name = name
        self.description = description
        self.poids = poids
        self.hidden = hidden

    def __str__(self):
        """blabla"""
        return f"{self.name} : {self.description} ({self.poids} kg)"
