"""Description: Game class"""
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
from interfacegraphique import GameGUI 


class Game:
    """classe jeu"""

    # Constructor
    def __init__(self):
        """Initialise les attributs de base de la classe Game"""
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.characters = []
        self.messages_history = []
        self.is_game_over = False
        self.door_opened = False  #porte a déjà été ouverte?
        self.limited_exits = True  #ctrl des sorties limitées début du jeu
        self.carnaval_first_visit = True  #Initialement, Carnaval n'a pas été visité
        self.foret = None
        self.entreecite = None
        self.carnaval = None
        self.chateau = None
        self.alleeprincipale = None
        self.maisonrdc = None
        self.maisonsoussol = None
        self.piedmontagneouest = None
        self.marche = None
        self.piedmonc = None
        self.mono = None
        self.montagnesombre = None
        self.endroitinconnu = None
        self.bordcite = None
        self.victory_checker = None
        self.defeat_checker = None
        self.is_open = False

    # Setup the game
    def setup(self):
        """Configure le jeu en initialisant les commandes, les salles, les objets et les PNJ"""

        # Setup commands
        help = Command("help", " : afficher cette aide", Actions.help,0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit,0)
        self.commands["quit"] = quit
        go = Command("go","<direction>: se déplacer dans une direction (N, E, S, O)", Actions.go,1)
        self.commands["go"] = go
        history = Command("history",":afficher l'historique des pièces visitées", Actions.history,0)
        self.commands["history"] = history
        back = Command("back", " : retourner en arrière", Actions.back,0)
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
        charge = Command("charge", " : charger le beamer", Actions.charge,0)
        self.commands["charge"]= charge
        teleporte = Command("TP",":se TP dans une pièce visitée via le beamer",Actions.teleporte,0)
        self.commands["teleporte"]= teleporte
        talk = Command("talk", " :  parler aux PNJ", Actions.talk, 1)
        self.commands["talk"]= talk
        give = Command("give", " :  donner les objets au garde", Actions.give, 1)
        self.commands["give"]= give

        # Setup rooms
        foret = Room("Forêt", "dans une forêt illuminée", "dessin/foret.png")
        self.rooms.append(foret)
        entreecite = Room("Entrée de la cité", "à l'entrée de la cité")
        self.rooms.append(entreecite)
        carnaval = Room("carnaval", "au carnaval")
        self.rooms.append(carnaval)
        maisonrdc = Room("Rez-de-chaussé de la maison", "au rez-de-chaussée de votre maison")
        self.rooms.append(maisonrdc)
        maisonsoussol = Room("Sous-sol de la maison", "dans le sous-sol de la maison")
        self.rooms.append(maisonrdc)
        alleeprincipale = Room("Allée principale du village", "dans l'allée principale du village")
        self.rooms.append(alleeprincipale)
        piedmontagneouest = Room("Pied de la montagne (Ouest)", "au pied ouest de la montagne")
        self.rooms.append(piedmontagneouest)
        marche = Room("Marché", "au marché")
        self.rooms.append(marche)
        piedmonc = Room("Pied de la montagne (Centre)", "au pied central de la montagne")
        self.rooms.append(piedmonc)
        mono = Room("Montagne (chemin Ouest)", "sur la montagne coté ouest")
        self.rooms.append(mono)
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
        entreecite.exits = {"N" : alleeprincipale, "E" : maisonrdc, "S" : None, "O" : carnaval}
        carnaval.exits = {"N" : piedmontagneouest, "E" : entreecite, "S" : bordcite, "O" : None}
        maisonrdc.exits = {"N":marche,"E":None,"S":None,"O":entreecite,"U":None,"D":maisonsoussol}
        maisonsoussol.exits = {"N":None, "E":None, "S":None, "O":None, "U":maisonrdc, "D":None}
        alleeprincipale.exits = {"N":piedmonc,"E":marche,"S":entreecite, "O":piedmontagneouest}
        piedmontagneouest.exits = {"N" : mono, "E" : alleeprincipale, "S" : carnaval, "O" : None}
        marche.exits = {"N" : maisonrdc, "E" : None, "S" : None, "O" : alleeprincipale}
        piedmonc.exits = {"N" : mono, "E" : None, "S" : alleeprincipale, "O" : mono}
        mono.exits = {"N" : chateau, "E" : piedmonc, "S" : piedmontagneouest, "O" : None}
        chateau.exits = {"N" : None, "E":montagnesombre, "S" : None, "O" : None}
        montagnesombre.exits = {"N":None, "E":endroitinconnu, "S" : piedmonc, "O" : chateau}
        endroitinconnu.exits = {"N" :None, "E" : None, "S" : None, "O" : montagnesombre}
        bordcite.exits = {"N" : carnaval, "E" : None, "S" : None, "O" : None}




        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = foret


        self.foret = foret
        self.entreecite = entreecite
        self.carnaval = carnaval
        self.chateau = chateau
        self.alleeprincipale = alleeprincipale
        self.maisonrdc = maisonrdc
        self.maisonsoussol = maisonsoussol
        self.piedmontagneouest = piedmontagneouest
        self.marche = marche
        self.piedmonc = piedmonc
        self.mono = mono
        self.montagnesombre = montagnesombre
        self.endroitinconnu = endroitinconnu
        self.bordcite = bordcite



        pierre = Item("Pierre", "une étrange pierre scintillante aux lueurs violettes", 2)
        branche = Item("Branche", "une lourde branche d'arbre", 3)
        potion = Item("Potion", "une potion magique qui va t'aider", 1)
        beamer = Beamer("Beamer", "un objet magique qui vous permet de vous téléporter", 3)
        mushroom = Item("Champignon", "un champignon doré très rare", 1)
        key = Item("Clef", "la clef qui permet d'ouvrir les portes de la cité", 1)
        tapis = Item("Tapis", "Un tapis lourd et poussiereux", 5)
        bague = Item("Bague", "Une belle bague précieuse", 1)



        # Ajout des items à l'inventaire des lieux directement via le dictionnaire
        foret.inventory["pierre"] = pierre
        foret.inventory["branche"] = branche
        maisonsoussol.inventory["beamer"] = beamer
        carnaval.inventory.items["potion"] = {"item": potion, "hidden": True}
        foret.inventory["champignon"] = mushroom
        foret.inventory["clef"] = key
        carnaval.inventory.items["tapis"] = {"item": tapis, "hidden": True} #vendeuse carnaval
        marche.inventory["bague"] = {"item": bague, "hidden": True} #marchand cachée au début

        #PNJ
        bouffon = Character("Bouffon", "Le bouffon du roi", carnaval, [
            "Le roi m'a envoyé dans la ville pour me ressourcer",
            "Le roi est si gentil.",
            "Ce carnaval est superbe ! Je me sens inspiré"
        ], visible = False)
        medecin = Character("Médecin", "Un médecin", carnaval, [
            "Tiens toi! Prends la potion que j'ai mise sur la table !",
            "Je dois aller guérir les nouveaux malades ! Dépêche toi !",
            "Satanée infection!!"
        ], visible = False)
        vendeuse = Character("Vendeuse", "Une vendeuse", carnaval, [
            "Prends ce tapis",
            "Tu peux me faire confiance, il est superbe et de grande valeur!"
        ], visible = False)
        annonceur = Character(
            "Annonceur", 
            "Un annonceur qui arrive sur la place du Carnaval", 
            carnaval,
            ["Que tout le monde aille se réfugier au château! Un terrible virus va nous tuer!"],
            visible = True
        )
        villageois = Character("Villageois", "Un villageois à l'apparence décrépite", entreecite,[
            "Hgrhh...Je me sens mal..."
        ], visible = True)
        garde = Character("Garde", "Le garde du chateau", chateau, [
            "Il y a trop de monde, je ne peux vous laisser passer, " 
            "à moins que vous ayez quelque chose pour me convaincre?"
        ], visible = True)
        marchand = Character("Vieux marchand", "Un marchand", marche, [
            "Un objet qui te seras utile est pour toi, il se trouve dans cette pièce"
        ], visible = True)

        # Liste des personnages pour le jeu
        self.characters = [bouffon, medecin, vendeuse, annonceur, villageois, garde, marchand]

        # Ajout des PNJ à la pièce
        self.carnaval.inventory.add_npc(bouffon)
        self.carnaval.inventory.add_npc(medecin)
        self.carnaval.inventory.add_npc(vendeuse)
        self.carnaval.inventory.add_npc(annonceur)
        self.entreecite.inventory.add_npc(villageois)
        self.chateau.inventory.add_npc(garde)
        self.marche.inventory.add_npc(marchand)

        #Faire bouger les PNJ
        villageois.move()

    def play(self):
        """Lance et gère la boucle principale du jeu"""
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
                    print("DEBUG: Début du déplacement du villageois")
                # Chercher uniquement le PNJ mobile dans toutes les pièces
                for room in self.rooms:
                    if "villageois" in room.inventory.npcs:
                        villageois = room.inventory.npcs["villageois"]
                        villageois.move()
                        break  # On sort dès qu'on a trouvé et déplacé le PNJ
                if DEBUG:
                    print("DEBUG: Fin du déplacement du villageois")

    def check_game_state(self):
        """Vérifie l'état du jeu et retourne un message si le jeu est terminé"""
        # Vérification des conditions de défaite
        defeat_conditions = [
            (self.defeat_checker.endroitinconnu, "\nDÉFAITE: Vous êtes tombé de la falaise!\n"),
            (
                self.defeat_checker.talk_to_villageois,
                "\nDÉFAITE: Vous avez été infecté par le villageois!\n"
            ),
            ]
        for condition, message in defeat_conditions:
            if condition():  # Si la condition de défaite est remplie
                return message
        # Mise à jour des conditions de victoire basées sur l'état actuel
        self.update_victory_conditions()
        # Vérification des conditions de victoire
        if all(condition() for condition in self.victory_checker.CONDITIONS_VICT):
            return "\nVICTOIRE: Félicitations, vous avez accompli votre quête!"
        return None

    def update_victory_conditions(self, show_validation=True):
        """Met à jour les conditions de victoire basées sur l'état actuel du jeu"""
        # Vérifie si le joueur est dans le château
        if self.player.current_room == self.chateau:
            in_the_right_room = self.chateau
            self.victory_checker.update_condition("Château", in_the_right_room)
        # Vérifie les objets dans l'inventaire
        inventory_items = [item.lower() for item in self.player.inventory.items]
        has_potion = "potion" in inventory_items
        self.victory_checker.update_condition("potion", has_potion)
        has_pierre = "pierre" in inventory_items
        self.victory_checker.update_condition("pierre", has_pierre)
        has_bague = "bague" in inventory_items
        self.victory_checker.update_condition("bague", has_bague)
        # Vérifie les dialogues
        has_talked_to_annonceur = getattr(self.player, 'has_talked_to_annonceur', False)
        self.victory_checker.update_condition("annonceur", has_talked_to_annonceur)

    def process_command(self, command_string):
        """Traite la commande entrée par le joueur"""
        command_string = command_string.strip()
        if command_string == "":
            return
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]
        # Gérer la commande "talk annonceur" avant le reste
        if (command_word == "talk" and len(list_of_words) > 1
        and list_of_words[1].lower() == "annonceur"):
            if self.player.current_room.name.lower() == "carnaval":
                print(
                    "\nAnnonceur (dans carnaval) : Que tout le monde aille vite "
                    "se réfugier au château ! Un terrible virus va nous tuer!"
                )
                print(
                    "\n* Les autres visiteurs du carnaval commencent à apparaître "
                    "autour de toi... *"
                )
                print(
                    "\nN'hésite pas à interagir avec les habitants, ce qu'ils ont "
                    "à t'offrir sera peut-être utile dans ta quête vers le château."
                )
                # Mettre à jour l'attribut du joueur
                self.player.has_talked_to_annonceur = True
                # Mettre à jour la condition dans le victory checker
                self.victory_checker.update_condition("annonceur", True)
                #Mettre à jour les sorties limitées = plus obligé d'aller à l'ouest après entreecite
                self.limited_exits = False
                # Rendre les PNJ visibles dans la salle du carnaval
                for character in self.characters:#use liste des perso de la classe Game
                    if (character.current_room.name.lower() == "carnaval"
                    and character.name.lower() != "annonceur"):
                        character.visible = True
                #Afficher les PNJ maintenant visibles
                visible_npcs = [char for char in self.characters
                            if char.current_room.name.lower() == "carnaval"
                            and char.visible
                            and char.name.lower() != "annonceur"]
                if visible_npcs:
                    print("\nPersonnages :")
                    for npc in visible_npcs:
                        print(f"- {npc.name} : {npc.description}")
                return
            else:
                print("\nL'annonceur n'est pas ici.\n")
                return
# Ajoutez cette partie pour gérer l'interaction avec le garde
        if command_word == "give" and len(list_of_words) > 2:
            item_name = list_of_words[2].lower()
            if self.player.current_room.name.lower() == "Château":
                if any(npc.name.lower() == "garde"
                       for npc in self.player.current_room.inventory.npcs.values()):
                    if item_name in ["potion", "pierre", "bague"]:
                        if item_name in self.player.inventory.items:
                            if item_name == "potion":
                                print("\nVous donnez la potion au garde."
                                        "Il l'examine et vous laisse passer.")
                                self.player.inventory.items.remove("potion")
                                self.victory_checker.garde_convinced = True
                            elif item_name in ["pierre", "bague"]:
                                if all(item in self.player.inventory.items
                                for item in ["pierre","bague"]):
                                    print("\nVous montrez la pierre et la bague au garde.")
                                    print("\nImpressionné et conquis, il vous laisse passer.")
                                    self.victory_checker.garde_convinced = True
                                else:
                                    print("\nLe garde demande des objets pour être convaincu.")
                            return
                        else:
                            print(f"\nVous n'avez pas {item_name} dans votre inventaire.")
                    else:
                        print("\nLe garde n'est pas intéressé par cet objet.")
                else:
                    print("\nIl n'y a pas de garde ici.")
            else:
                print("")
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
            if self.limited_exits:
                # Restriction des sorties
                if self.player.current_room == self.entreecite and direction not in {"O"}:
                    print("Vous ne pouvez aller qu'à l'ouest pour l'instant.")
                    return
            # Vérifier si on est dans la forêt et qu'on va vers la cité
            if self.player.current_room == self.foret and direction == "N":
                # Si la porte n'a pas encore été ouverte
                if not self.door_opened:
                    # Vérifier si le joueur a la clé
                    has_key = "Clef" in self.player.inventory.items
                    # items est un dictionnaire, pas une méthode
                    if not has_key:
                        print("\nVous ne pouvez pas entrer dans la cité sans la clé.\n")
                        return
                    else:
                        print("\nVous ouvrez les portes de la cité avec la clé "
                        "et celles-ci se referment derrière vous.")
                        self.is_open = True  # La porte est maintenant ouverte
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
                print("Parlez aux différentes personnes"
                "que vous verrez pour en savoir plus sur le jeu.")
                self.carnaval_first_visit = False  # Mettre à jour le drapeau
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue."
             "Entrez 'help' pour voir la liste des commandes disponibles.\n")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)
        return False  #Si la commande n'est pas reconnue ou traitée
    # Print the welcome message
    def print_welcome(self):
        """Affiche le message de bienvenue au début du jeu"""
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' pour connaître les commandes du jeu.")
        print(self.player.current_room.get_long_description())

    @staticmethod
    def main():
        """Point d'entrée principal du jeu"""
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
    Game.main()
