from item import Item


class Beamer(Item):

    def __init__(self, name="beamer", description="un objet magique de téléportation", poids=1, teleport_room = None):
       super().__init__(name, description, poids)
       self.teleporte_room = None


    def charge(self, current_room):
       self.teleporte_room= current_room
       print(f"Le beamer est chargé dans le lieu : {current_room.name}")


    def teleporte(self, player):
        if self.teleporte_room:
            print(f"Vous utilisez le beamer et vous vous êtes téléporté dans le lieu : '{self.teleporte_room.name}'.")
            player.current_room = self.teleporte_room
            #game.player.history.append(game.player.current_room)
            #print(game.player.current_room.get_long_description())
            #game.player.print_history()
            #return True
        else:
            print("Le beamer n'est pas chargé avec une destination spécifique. Impossible de l'utiliser.")
            #return False

