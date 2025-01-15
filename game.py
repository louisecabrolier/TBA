"""Description: Game class"""  # pylint: disable = too-many-instance-attributes
# pylint: disable = too-many-locals
# pylint: disable = too-many-statements
# pylint: disable = too-many-branches
# pylint: disable = too-many-nested-blocks
# pylint: disable = import-outside-toplevel

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
from pathlib import Path
from door import Door


# Au début du fichier game.py
try:
    import tkinter as tk
    from gui_tkinter import GameGUI
except ImportError:
    pass


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
        self.door = Door()
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
        self.carnaval_npcs_revealed = False  # Pour suivre si les PNJ du carnaval ont été révélés

    # Setup the game
    def setup(self):
        """Configure le jeu en initialisant les commandes, les salles, les objets et les PNJ"""

        # Setup commands
        aide = Command("aide", " : afficher cette aide", Actions.aide,0)
        self.commands["aide"] = aide
        quitter = Command("quitter", " : quitter le jeu", Actions.quitter, 0)
        self.commands["quitter"] = quitter
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
        teleporte = Command("teleporte"," : se téléporter dans une pièce visitée via le beamer",Actions.teleporte,0)
        self.commands["teleporte"]= teleporte
        talk = Command("talk", " :  parler aux PNJ", Actions.talk, 1)
        self.commands["talk"]= talk
        give = Command("give", " :  donner les objets au garde", Actions.give, 1)
        self.commands["give"]= give
        
        # Création des salles avec leurs images
        image_dir = Path("dessin")  # Dossier pour les images sur GitHub
        
        # Setup rooms
        foret = Room("Forêt", "dans une forêt illuminée", "foret.jpg")
        self.rooms.append(foret)
        entreecite = Room("Entrée de la cité", "à l'entrée de la cité", "entree-de-la-cite.jpg")
        self.rooms.append(entreecite)
        carnaval = Room("carnaval", "au carnaval", "carnaval.jpg")
        self.rooms.append(carnaval)
        maisonrdc = Room("Rez-de-chaussé de la maison", "au rez-de-chaussée de votre maison", "rdcmaison.jpg")
        self.rooms.append(maisonrdc)
        maisonsoussol = Room("Sous-sol de la maison", "dans le sous-sol de la maison", "maisonsoussol.jpg")
        self.rooms.append(maisonsoussol)
        alleeprincipale = Room("Allée principale du village", "dans l'allée principale du village", "alleeprincipale.jpg")
        self.rooms.append(alleeprincipale)
        piedmontagneouest = Room("Pied de la montagne (Ouest)", "au pied ouest de la montagne", "piedouest.jpg")
        self.rooms.append(piedmontagneouest)
        marche = Room("Marché", "au marché", "marche.jpg")
        self.rooms.append(marche)
        piedmonc = Room("Pied de la montagne (Centre)", "au pied central de la montagne", "piedcentre.jpg")
        self.rooms.append(piedmonc)
        mono = Room("Montagne (chemin Ouest)", "sur la montagne coté ouest", "mono.jpg")
        self.rooms.append(mono)
        chateau = Room("Château", "au château", "chateau.jpg")
        self.rooms.append(chateau)
        montagnesombre = Room("Montagne sombre", "sur une montagne sombre", "montagnesombre2.jpg")
        self.rooms.append(montagnesombre)
        endroitinconnu = Room("Endroit inconnu", "au bord d'une falaise", "falaise.jpg")
        self.rooms.append(endroitinconnu)
        bordcite = Room("Bord de la cité","au bord de la cité", "bordcite.jpg")
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
        self.player.history.append(foret)


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
        #foret.inventory["pierre"] = pierre
        foret.inventory.add_item(pierre, hidden=False)
        #foret.inventory["branche"] = branche
        foret.inventory.add_item(branche, hidden=False)
        #maisonsoussol.inventory["beamer"] = beamer
        maisonsoussol.inventory.add_item(beamer, hidden=False)
        #carnaval.inventory.items["potion"] = {"item": potion, "hidden": True}
        carnaval.inventory.add_item(potion, hidden=True)
        #foret.inventory["champignon"] = mushroom
        foret.inventory.add_item(mushroom, hidden=False)
        #foret.inventory["clef"] = key
        foret.inventory.add_item(key, hidden=False)
        print("\nDEBUG - Après ajout de la clef:")
        print("Clés dans l'inventaire:", list(foret.inventory.items.keys()))
        print("Items dans l'inventaire:", [(k, v["item"].name) for k, v in foret.inventory.items.items()])
        #carnaval.inventory.items["tapis"] = {"item": tapis, "hidden": True} #vendeuse carnaval
        carnaval.inventory.add_item(tapis, hidden=True)
        #marche.inventory["bague"] = {"item": bague, "hidden": True} #marchand cachée au début
        marche.inventory.add_item(bague, hidden=True)


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
        if all(condition() for condition in self.victory_checker.conditionvict):
            return "\nVICTOIRE: Félicitations, vous avez accompli votre quête!"
        return None

    def update_victory_conditions(self):
        """Met à jour les conditions de victoire basées sur l'état actuel du jeu"""
        # Vérifie si le joueur est dans le château
        if self.player.current_room == self.chateau:
            in_the_right_room = self.chateau
            self.victory_checker.update_condition("Château", in_the_right_room)
        # Vérifie les objets dans l'inventaire
        #inventory_items = [item.lower() for item in self.player.inventory.items]
        inventory_items = [name for name in self.player.inventory.items.keys()]
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
            return False
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]
        # Gérer la commande "talk annonceur" avant le reste
        # Gestion spéciale des dialogues
        #villageois talk
                # Si c'est l'annonceur au carnaval
# Ajoutez cette partie pour gérer l'interaction avec le garde
        #if command_word == "go":
            #reste dans action.py avec def go
        if command_word not in self.commands:
            print(f"\nCommande '{command_word}' non reconnue."
             "Entrez 'help' pour voir la liste des commandes disponibles.\n")
            return False
        command = self.commands[command_word]
        command.action(self, list_of_words, command.number_of_parameters)
        return True

    # Print the welcome message
    def print_welcome(self):
        """Affiche le message de bienvenue au début du jeu"""
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'aide' pour connaître les commandes du jeu.")
        print(self.player.current_room.get_long_description())

    @staticmethod
    def main():
        """Point d'entrée principal du jeu"""
        print("Bienvenue dans le jeu !")
        print("Entrez 'aide' pour connaître les commandes du jeu.")
        mode = input("Choisissez un mode : 'console' ou 'gui' : ").strip().lower()
        
        game = Game()
        
        if mode == "gui":
            print("Lancement de l'interface graphique...")
            try:
                from gui_tkinter import GameGUI  # Nouveau fichier avec l'interface Tkinter
                app = GameGUI(game)
                app.run()
            except Exception as e:
                print(f"Erreur lors du lancement de l'interface graphique : {e}")
                print("Lancement en mode console...")
                game.play()
        else:
            print("Lancement en mode console...")
            game.play()

if __name__ == "__main__":
    Game.main()
