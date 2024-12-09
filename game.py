# Description: Game class




# Import modules
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from beamer import Beamer


class Game:




    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.characters = []
       




    # Setup the game
    def setup(self):




        # Setup commands
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : afficher l'historique des pièces visitées", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : retourner en arrière", Actions.back, 0)
        self.commands["back"]= back
        inventory = Command("inventory", " : retourner en arrière", Actions.inventory, 0)
        self.commands["inventory"]= inventory
        look = Command("look", " : regarder dans la pièce", Actions.look, 0)
        self.commands["look"]= look
        take = Command("take", " : prendre l'objet", Actions.take, 0)
        self.commands["take"]= take
        drop = Command("drop", " : poser l'objet", Actions.drop, 0)
        self.commands["drop"]= drop
        check = Command("check", " : regarder dans son inventaire", Actions.check, 0)
        self.commands["check"]= check
        #beamer
        charge = Command("charge", " : charger", Actions.charge, 0)
        self.commands["charge"]= charge
        teleporte = Command("teleporte", " :  se téléporter dans une pièce déjà visitée", Actions.teleporte, 0)
        self.commands["teleporte"]= teleporte


        # Setup rooms
        foret = Room("Forêt", "dans une forêt illuminée, BLABLABLA")
        self.rooms.append(foret)
        entreecite = Room("Entrée de la cité", "entree cite")
        self.rooms.append(entreecite)
        carnaval = Room("carnaval", "carnaval")
        self.rooms.append(carnaval)
        maisonRDC = Room("Rez-de-chaussé de la maison", "rdc maison")
        self.rooms.append(maisonRDC)
        maisonsoussol = Room("Sous-sol de la maison", "sous sol maison")
        self.rooms.append(maisonRDC)
        alleeprincipale = Room("Allée principale du village", "alle principale du village")
        self.rooms.append(alleeprincipale)
        piedmontagneouest = Room("Pied de la montagne (Ouest)", "pied ouest de la montagne")
        self.rooms.append(piedmontagneouest)
        marche = Room("Marché", "marché")
        self.rooms.append(marche)
        piedmonC = Room("Pied de la montagne (Centre)", "pied central de la montagne")
        self.rooms.append(piedmonC)
        MonO = Room("Montagne (chemin Ouest)", "montagne coté ouest")
        self.rooms.append(MonO)
        chateau = Room("Château", "chateau")
        self.rooms.append(chateau)
        Montagnesombre = Room("Montagne sombre", " montagne sombre")
        self.rooms.append(Montagnesombre)
        endroitinconnu = Room("Endroit inconnu","endroit inconnu")
        self.rooms.append(endroitinconnu)
        bordcite = Room("Bord de la cité","bord de la cité")
        self.rooms.append(bordcite)




        # Create exits for rooms
        foret.exits = {"N" : entreecite, "E" : None, "S" : None, "O" : None}
        entreecite.exits = {"N" : alleeprincipale, "E" : maisonRDC, "S" : foret, "O" : None}
        carnaval.exits = {"N" : piedmontagneouest, "E" : entreecite, "S" : bordcite, "O" : None}
        maisonRDC.exits = {"N" : marche, "E" : None, "S" : None, "O" : entreecite, "U" : None, "D": maisonsoussol}
        maisonsoussol.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : maisonRDC, "D" : None}
        alleeprincipale.exits = {"N" : piedmonC, "E" : marche, "S" : entreecite, "O" : piedmontagneouest}
        piedmontagneouest.exits = {"N" : MonO, "E" : alleeprincipale, "S" : carnaval, "O" : None}
        marche.exits = {"N" : maisonRDC, "E" : None, "S" : None, "O" : alleeprincipale}
        piedmonC.exits = {"N" : MonO, "E" : None, "S" : alleeprincipale, "O" : MonO}
        MonO.exits = {"N" : chateau, "E" : piedmonC, "S" : piedmontagneouest, "O" : None}
        chateau.exits = {"N" : None, "E" : Montagnesombre, "S" : None, "O" : None}
        Montagnesombre.exits = {"N" : None, "E" : endroitinconnu, "S" : piedmonC, "O" : chateau}
        endroitinconnu.exits = {"N" : None, "E" : None, "S" : None, "O" : Montagnesombre}
        bordcite.exits = {"N" : carnaval, "E" : None, "S" : None, "O" : None}




        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = foret


        self.foret = foret  # Store room as instance attribute
        self.entreecite = entreecite
        self.carnaval = carnaval


        shield = Item("shield", "un bouclier léger et résistant", 5)
        helmet = Item("helmet", "un casque en métal", 6)
        branche = Item("branche", "une branche d'arbre", 1)
        potion = Item("potion", "une potion magique qui va t'aider", 1)
        beamer = Beamer("beamer", "un objet magique qui permet la téléportation", 1)


        # Ajout des items à l'inventaire des lieux directement via le dictionnaire
        foret.inventory["shield"] = shield
        foret.inventory["helmet"] = helmet
        entreecite.inventory["branche"] = branche
        foret.inventory["beamer"] = beamer
        carnaval.inventory["potion"] = potion

     

        #PNJ

        # Création des personnages

        bouffon = Character("Bouffon", "Le bouffon du roi", carnaval, ["J'ai quelque chose pour toi."])
        medecin = Character("Médecin", "Un médecin random", carnaval, ["J'ai quelque chose pour t'aider dans ta quête"])
        vendeuse = Character("Vendeuse", "Une vendeuse s'approche pour te parler", carnaval, ["T'as fait tes affaires"])
        annonceur = Character("Annonceur", "Un annonceur arrive sur la place du Carnaval", carnaval, ["Infection ! Il faut se réfugier au château"])

        # Liste des personnages pour le jeu

        self.characters = [bouffon, medecin, vendeuse, annonceur]

        #Ajout des personnages aux lieux

        carnaval.characters.append(bouffon)
        carnaval.characters.append(medecin)
        carnaval.characters.append(vendeuse)
        carnaval.characters.append(annonceur)

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None




    # Process the command entered by the player
    def process_command(self, command_string) -> None:
    #Supprimer les espaces avant et après
        command_string = command_string.strip()




        #Si la commande est vide, ne rien faire
        if command_string == "":
            return




        # Split the command string into a list of words
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]




        if command_word == "go":
            if len(list_of_words) < 2:
                print ("\n Veuillez spécifier une direction.\n")
                return

        

            # crea du set des directions possibles
            directions_values = {"N", "S", "E", "O", "U", "D"}
            direction = list_of_words[1][0].upper()
               
            # verif que la direction existe
            if direction not in directions_values:
                print("\nDirection invalide.\n")
                return




            # Modification de la direction dans list_of_words
            list_of_words[1] = direction




            # Création du set des directions valides pour la salle concernée
            directions_valides = set()
            for direction_possible, next_room in self.player.current_room.exits.items():
                if next_room is not None:
                    directions_valides.add(direction_possible)
               
            # Vérifier si la direction est possible depuis cette salle
            if direction not in directions_valides:
                print("\nVous ne pouvez pas aller dans cette direction.\n")
                return




        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)




    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())
   


def main():
    # Create a game object and play the game
    Game().play()
   




if __name__ == "__main__":
    main()



