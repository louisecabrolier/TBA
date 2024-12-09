from item import Item


class Beamer(Item):
    def __init__(self, name="beamer", description="un objet magique de téléportation", poids=1, teleport_room = None):
       super().__init__(name, description, poids)
       self.teleport_room = teleport_room


    def charge(self, current_room):
       self.teleport_room= current_room
       print(f"Le beamer est chargé avec la salle : {current_room.name}")


    def use(self, player):
        if self.teleport_room is None:
            print("Vous êtes téléporté dans la salle : '{self.teleport_room.name}.")
            game.player.current_room = self.teleport_room
            game.player.history.append(game.player.current_room)
            print(game.player.current_room.get_long_description())
            game.player.print_history()
            return True
        else:
            print("Le beamer n'est pas chargé avec une destination spécifique.")
            return False

