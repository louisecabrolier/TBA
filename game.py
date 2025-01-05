# Description: Game class

#accès carnaval à simplifier pour commencer le jeu sinon tu sais pas où tu vas ni ce qu'il faut faire
#dire le but du jeu assez tôt
#bloquer l'accès au chateau avant d'avoir les objets


# Import modules
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from beamer import Beamer
from config import DEBUG
from checkvictory import CheckVictory
from checkdefeat import CheckDefeat
from door import Door
from interfacegraphique import GameGUI 
#from CheckVictory import CONDITIONS_VICT
#from CheckDefeat import CONDITIONS_DEF

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.characters = []
        self.messages_history = []
        self.is_game_over = False
        self.door = Door()
        self.door_opened = False  # Pour suivre si la porte a déjà été ouverte
        self.limited_exits = True  # Contrôle des sorties limitées au début du jeu
        self.carnaval_first_visit = True  # Initialement, le Carnaval n'a pas été visité


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
        inventory = Command("inventory", " : inventaire", Actions.inventory, 0)
        self.commands["inventory"]= inventory
        look = Command("look", " : regarder dans la pièce", Actions.look, 0)
        self.commands["look"]= look
        take = Command("take", " : prendre l'objet", Actions.take, 1)
        self.commands["take"]= take
        drop = Command("drop", " : poser l'objet", Actions.drop, 0)
        self.commands["drop"]= drop
        check = Command("check", " : regarder dans son inventaire", Actions.check, 0)
        self.commands["check"]= check
        #beamer
        charge = Command("charge", " : charger le beamer", Actions.charge, 0)
        self.commands["charge"]= charge
        teleporte = Command("teleporte", " :  se téléporter dans une pièce déjà visitée avec le beamer", Actions.teleporte, 0)
        self.commands["teleporte"]= teleporte
        talk = Command("talk", " :  parler aux PNJ", Actions.talk, 1)
        self.commands["talk"]= talk
        
        


        # Setup rooms
        foret = Room("Forêt", "dans une forêt illuminée", "dessin/foret.png")
        self.rooms.append(foret)
        entreecite = Room("Entrée de la cité", "à l'entrée de la cité")
        self.rooms.append(entreecite)
        carnaval = Room("carnaval", "au carnaval")
        self.rooms.append(carnaval)
        maisonRDC = Room("Rez-de-chaussé de la maison", "au rez-de-chaussée de votre maison")
        self.rooms.append(maisonRDC)
        maisonsoussol = Room("Sous-sol de la maison", "dans le sous-sol de la maison")
        self.rooms.append(maisonRDC)
        alleeprincipale = Room("Allée principale du village", "dans l'allée principale du village")
        self.rooms.append(alleeprincipale)
        piedmontagneouest = Room("Pied de la montagne (Ouest)", "au pied ouest de la montagne")
        self.rooms.append(piedmontagneouest)
        marche = Room("Marché", "au marché")
        self.rooms.append(marche)
        piedmonC = Room("Pied de la montagne (Centre)", "au pied central de la montagne")
        self.rooms.append(piedmonC)
        monO = Room("Montagne (chemin Ouest)", "sur la montagne coté ouest")
        self.rooms.append(monO)
        chateau = Room("Château", "au château")
        self.rooms.append(chateau)
        montagnesombre = Room("Montagne sombre", "sur une montagne sombre")
        self.rooms.append(montagnesombre)
        endroitinconnu = Room("Endroit inconnu", "au bord d'une falaise")
        self.rooms.append(endroitinconnu)
        bordcite = Room("Bord de la cité","au bord de la cité")
        self.rooms.append(bordcite)




        # Create exits for rooms
        foret.exits = {"N" : entreecite, "E" : None, "S" : None, "O" : None}
        entreecite.exits = {"N" : alleeprincipale, "E" : maisonRDC, "S" : None, "O" : carnaval}
        carnaval.exits = {"N" : piedmontagneouest, "E" : entreecite, "S" : bordcite, "O" : None}
        maisonRDC.exits = {"N" : marche, "E" : None, "S" : None, "O" : entreecite, "U" : None, "D": maisonsoussol}
        maisonsoussol.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : maisonRDC, "D" : None}
        alleeprincipale.exits = {"N" : piedmonC, "E" : marche, "S" : entreecite, "O" : piedmontagneouest}
        piedmontagneouest.exits = {"N" : monO, "E" : alleeprincipale, "S" : carnaval, "O" : None}
        marche.exits = {"N" : maisonRDC, "E" : None, "S" : None, "O" : alleeprincipale}
        piedmonC.exits = {"N" : monO, "E" : None, "S" : alleeprincipale, "O" : monO}
        monO.exits = {"N" : chateau, "E" : piedmonC, "S" : piedmontagneouest, "O" : None}
        chateau.exits = {"N" : None, "E" : montagnesombre, "S" : None, "O" : None}
        montagnesombre.exits = {"N" : None, "E" : endroitinconnu, "S" : piedmonC, "O" : chateau}
        endroitinconnu.exits = {"N" : None, "E" : None, "S" : None, "O" : montagnesombre}
        bordcite.exits = {"N" : carnaval, "E" : None, "S" : None, "O" : None}




        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = foret


        self.foret = foret
        self.entreecite = entreecite
        self.carnaval = carnaval
        self.chateau = chateau
        self.alleeprincipale = alleeprincipale
        self.maisonRDC = maisonRDC
        self.maisonsoussol = maisonsoussol
        self.piedmontagneouest = piedmontagneouest
        self.marche = marche
        self.piedmonC = piedmonC
        self.monO = monO
        self.montagnesombre = montagnesombre
        self.endroitinconnu = endroitinconnu
        self.bordcite = bordcite



        shield = Item("shield", "un bouclier léger et résistant", 5)
        helmet = Item("helmet", "un casque en métal", 6)
        branche = Item("branche", "une branche d'arbre", 1)
        potion = Item("potion", "une potion magique qui va t'aider", 1)
        beamer = Beamer("beamer", "un objet magique qui permet la téléportation", 1)
        mushroom = Item("mushroom", "un champignon doré très rare", 1)
        key = Item("key", "la clé qui permet d'ouvrir les portes de la cité", 1)


        # Ajout des items à l'inventaire des lieux directement via le dictionnaire
        foret.inventory["shield"] = shield
        foret.inventory["helmet"] = helmet
        entreecite.inventory["branche"] = branche
        foret.inventory["beamer"] = beamer
        marche.inventory.items["potion"] = {"item": potion, "hidden": True} #potion cachée au début avant de parler au marchand
        foret.inventory["mushroom"] = mushroom
        foret.inventory["key"] = key


        #PNJ

        # Création des personnages

        bouffon = Character("bouffon", "Le bouffon du roi", carnaval, ["J'ai quelque chose pour toi."])
        medecin = Character("medecin", "Un médecin random", carnaval, ["J'ai quelque chose pour t'aider dans ta quête"])
        vendeuse = Character("vendeuse", "Une vendeuse", carnaval, ["T'as fait tes affaires"])
        annonceur = Character("annonceur", "Un annonceur qui arrive sur la place du Carnaval", carnaval, ["Infection !"," Il faut se réfugier au château"])
        pnj = Character("pnj", "Un pnj qui sert à rien", entreecite, ["Tu perds ton temps à me parler", "on espère que la démo vous plaît"])
        garde = Character("garde", "Le garde du chateau", chateau, ["Peux-tu me donner l'objet nécessaire pour entrer?"])
        marchand = Character("marchand", "Un marchand", marche, ["Un objet utile pour toi se trouve dans cette pièce"])

        # Liste des personnages pour le jeu

        self.characters = [bouffon, medecin, vendeuse, annonceur, pnj, garde, marchand]


        # Ajout des PNJ à la pièce
        self.carnaval.inventory.add_npc(bouffon)
        self.carnaval.inventory.add_npc(medecin)
        self.carnaval.inventory.add_npc(vendeuse)
        self.carnaval.inventory.add_npc(annonceur)
        self.entreecite.inventory.add_npc(pnj)
        self.chateau.inventory.add_npc(garde)
        self.marche.inventory.add_npc(marchand)

        #Faire bouger les PNJ
        pnj.move()

    def play(self):
        self.setup()
        self.print_welcome()
        
        # Initialisation des vérificateurs de victoire et défaite
        self.victory_checker = CheckVictory()
        self.defeat_checker = CheckDefeat()
        
        while not self.finished:
            # Vérification des conditions de victoire/défaite
            game_state = self.check_game_state()
            if game_state:
                print(game_state)
                self.finished = True
                break

            # Récupérer la commande
            command = input("> ")
            
            # Vérifier si c'est une commande "go" avant de déplacer le PNJ
            should_move_npcs = command.strip().startswith("go")
            
            # Traiter la commande du joueur
            self.process_command(command)
            
            # Déplacer uniquement le PNJ mobile si c'était une commande "go"
            if should_move_npcs:
                if DEBUG:
                    print("DEBUG: Début du déplacement du PNJ")
                # Chercher uniquement le PNJ mobile dans toutes les pièces
                for room in self.rooms:
                    if "pnj" in room.inventory.npcs:
                        pnj = room.inventory.npcs["pnj"]
                        pnj.move()
                        break  # On sort dès qu'on a trouvé et déplacé le PNJ
                if DEBUG:
                    print("DEBUG: Fin du déplacement du PNJ")

    def check_game_state(self):
        """Vérifie l'état du jeu et retourne un message si le jeu est terminé"""
        # Vérification des conditions de défaite
        for condition in self.defeat_checker.CONDITIONS_DEF:
            if condition():
                return "\nDÉFAITE: Vous êtes tombé de la falaise!\n"

        # Mise à jour des conditions de victoire basées sur l'état actuel
        self.update_victory_conditions()

        # Vérification des conditions de victoire
        if all(condition() for condition in self.victory_checker.CONDITIONS_VICT):
            return "\nVICTOIRE: Félicitations, vous avez accompli votre quête!\n"

        return None

    def update_victory_conditions(self):
        """Met à jour les conditions de victoire basées sur l'état actuel du jeu"""
        # Vérifie si le joueur est dans le château
        self.victory_checker.update_condition("chateau", 
            self.player.current_room.name == "chateau")
        
        # Vérifie si le joueur a parlé à l'annonceur
        # Supposons que nous gardons une trace des interactions dans player
        if hasattr(self.player, 'has_talked_to_annonceur'):
            self.victory_checker.update_condition("annonceur", 
                self.player.has_talked_to_annonceur)
        
        # Vérifie si le joueur a l'objet requis
        required_object = "objet_spécifique"  # À adapter selon votre jeu
        if hasattr(self.player, 'inventory'):
            self.victory_checker.update_condition("object",
                required_object in self.player.inventory.items)
        

        # Vérifie si le joueur a parlé au garde
        if hasattr(self.player, 'has_talked_to_garde'):
            self.victory_checker.update_condition("garde",
                self.player.has_talked_to_garde)

    def process_command(self, command_string) -> None:
        # Code existant...
        command_string = command_string.strip()
        if command_string == "":
            return
            
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]
        
        if DEBUG:
            print(f"DEBUG: Liste des mots de la commande: {list_of_words}")

        if command_word == "go":
            if len(list_of_words) < 2:
                print("\nVeuillez spécifier une direction.\n")
                return

            directions_values = {"N", "S", "E", "O", "U", "D"}
            direction = list_of_words[1][0].upper()

            if direction not in directions_values:
                print("\nDirection invalide.\n")
                return

            list_of_words[1] = direction
            if self.limited_exits == True:
                # Restriction des sorties
                if self.player.current_room == self.entreecite and direction not in {"O"}:
                    print("Vous ne pouvez aller qu'à l'ouest pour l'instant.")
                    return

            # Vérifier si on est dans la forêt et qu'on va vers la cité
            if self.player.current_room == self.foret and direction == "N":
                if not self.door_opened:  # Si la porte n'a pas encore été ouverte
                    # Vérifier si le joueur a la clé
                    has_key = "key" in self.player.inventory.items  # items est un dictionnaire, pas une méthode
                    if not has_key:
                        print("\nVous ne pouvez pas entrer dans la cité sans la clé.\n")
                        return
                    else:
                        print("\nVous utilisez la clé pour ouvrir les portes de la cité.")
                        self.door_opened = True  # La porte est maintenant ouverte

            
            directions_valides = set()
            for direction_possible, next_room in self.player.current_room.exits.items():
                if next_room is not None:
                    directions_valides.add(direction_possible)

            if direction not in directions_valides:
                print("\nVous ne pouvez pas aller dans cette direction.\n")
                return

           # Vérifier si le déplacement mène à "endroitinconnu" (condition de défaite)
            next_room = self.player.current_room.exits.get(direction)
            if next_room and next_room.name == "Endroit inconnu":  # Vérifie le nom de la salle
                self.defeat_checker.update_condition(True)

            # Levée des restrictions une fois au carnaval
            if next_room.name == "Carnaval":
                    self.limited_exits = False

            if next_room == self.carnaval and self.carnaval_first_visit:
                print("\nBienvenue au Carnaval ! Utilisez 'look' pour observer autour de vous.")
                print("Parlez aux différentes personnes que vous verrez pour en savoir plus sur le jeu.")
                self.carnaval_first_visit = False  # Mettre à jour le drapeau

        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)




    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' pour connaître les commandes du jeu.")
        print(self.player.current_room.get_long_description())
   


    def main():
        print("Bienvenue dans le jeu !")
        mode = input("Choisissez un mode : 'console' ou 'gui' : ").strip().lower()

        if mode == "gui":
            print("Lancement de l'interface graphique...")
            from interfacegraphique import GameGUI
            game = Game()  # Create a new game instance
            app = GameGUI(game)  # Pass the game instance to GameGUI
            app.run()
        else:
            print("Lancement en mode console...")
            game = Game()
            game.play()

if __name__ == "__main__":
    Game.main()  # Call the static main method directly


#def main():
    # Create a game object and play the game
    #Game().play()
#if __name__ == "__main__":

    #main()



