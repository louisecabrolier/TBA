"""Actions""" # pylint: disable = too-many-branches

#import inventory
#import room
#from beamer import Beamer
#from player import Player
#from item import Item

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.








# The error message is stored in the MSG0 and MSG1 variables
# and formatted with the command_word variable
# the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"







class Actions:
    """définir les actions possibles dans le jeu"""




    def go(self, game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).




        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.




        Returns:
            bool: True if the command was executed successfully, False otherwise.




        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False




        """

        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False




        # Get the direction from the list of words.
        direction = list_of_words[1]
        # Move the player in the direction specified by the parameter.
        player.move(direction)
        return True




    def quit(self, game, list_of_words, number_of_parameters):
        """
        Quit the game.




        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.




        Returns:
            bool: True if the command was executed successfully, False otherwise.




        Examples:




        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False




        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True




    def help(self, game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.




        Returns:
            bool: True if the command was executed successfully, False otherwise.




        Examples:




        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False




        """




        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True




    def history(self, game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des pièces visitées par le joueur.




        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.




        Returns:
            bool: True if the command was executed successfully, False otherwise.




        Examples:




        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> history(game, ["history"], 0)
        True
        >>> history(game, ["history", "N"], 0)
        False
        >>> history(game, ["history", "N", "E"], 0)
        False
        """
        l = len(list_of_words)
        # Si le nombre de paramètres est incorrect, afficher un message d'erreur et retourner False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Afficher l'historique des pièces visitées.
        history = game.player.get_history()
        print(history)
        return True








    def back(self, game, list_of_words, number_of_parameters):
        """
        Move the player back to the previous position.
           
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.




        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """




        player = game.player
        l = len(list_of_words)

        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Check if there is a previous position to return to.
        if not player.history:
            print("Vous ne pouvez pas revenir en arrière,"
            "aucun déplacement précédent enregistré.")
            return False

        # Pop the last position from the history and move the player back.
        previous_position = player.history.pop()

        player.position = previous_position
        #mettre a jour l'inventaire dune piece avec le back
        player.current_room = previous_position

        print(f"Vous êtes revenu à votre position précédente : {player.position.name}")

        return True




#inventaire
    def inventory(self, game, list_of_words, number_of_parameters):
        """
        Display the player's inventory.


        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.


        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """

        l = len(list_of_words)

        # Vérification du nombre de paramètres
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Utilisation du player directement depuis l'objet game
        print("\nVotre inventaire :")
        print(game.player.get_inventory())
        return True


    # Dans votre fonction look
    def look(self, game):
        """
        Permet au joueur de regarder autour de lui ou un objet spécifique.
        Ne montre que les PNJ visibles (annonceur au début, puis tous après lui avoir parlé).
        """
        current_room = game.player.current_room
        # Description de la pièce
        print(current_room.description)

        if current_room.inventory.get_visible_items():
            print("\nObjets visibles :")
            for item in current_room.inventory.get_visible_items().values():
                print(f" - {item.name} : {item.description}")

        # Afficher uniquement les PNJ visibles
        visible_npcs = [npc for npc in current_room.inventory.npcs.values() if npc.visible]
        if visible_npcs:
            print("\nPersonnages :")
            for npc in visible_npcs:
                print(f" - {npc.name} : {npc.description}")

        return True







    def take(self, game, list_of_words, number_of_parameters):
        """
        Permet au joueur de prendre un objet.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Récupérer l'objet à prendre
        item_name = list_of_words[1].lower()  # Normaliser le nom de l'objet saisi
        current_room = game.player.current_room

        # Chercher l'objet dans l'inventaire de la pièce
        visible_items = current_room.inventory.get_visible_items()

        # Chercher l'item sans tenir compte de la casse
        item_found = None
        for name, item in visible_items.items():
            if name.lower() == item_name:  # Comparaison insensible à la casse
                item_found = item
                break

        if item_found:
            # Vérifier le poids de l'objet
            if game.player.get_current_weight() + item_found.poids > game.player.max_poids:
                print("Vous avez trop de poids, vous ne pouvez pas prendre cet objet.")
                return False

            # Ajouter l'objet à l'inventaire du joueur
            game.player.inventory.add_item(item_found)
            current_room.inventory.remove_item(item_name)
            print(f"Vous avez pris {item_found.name}.")
            return True
        print(f"L'objet '{item_name}' n'est pas dans cette pièce.")
        return False




    def drop(self, game, list_of_words):
        """déposer un objet"""
        if len(list_of_words) < 2:
            print("Que voulez-vous déposer ?")
        item_name = list_of_words[1].lower()  # Normaliser le nom de l'item
        player = game.player
        current_room = player.current_room

        # Pièces autorisées pour drop
        allowed_rooms = ["Forêt", "Rez-de-chaussé de la maison", "Château"]
        current_room_name =  current_room.name.strip()
        if current_room_name not in allowed_rooms:
            print("Vous ne pouvez pas déposer d'objets ici.")
            return


        # Chercher l'item dans l'inventaire du joueur, en prenant en compte la casse
        item_found = None
        name = None
        for name, data in player.inventory.items.items():
            if name.lower() == item_name:  # Comparaison insensible à la casse
                item_found = data["item"]
                break

        if item_found:
            # Retirer l'item de l'inventaire du joueur
            del player.inventory.items[name]  # Utilise le nom trouvé
            # Ajouter l'item à l'inventaire de la pièce
            player.current_room.inventory.add_item(item_found)
            print(f"Vous avez déposé l'objet '{name}'")
        print(f"Vous n'avez pas de '{item_name}' dans votre inventaire.")

    def check(self, game):
        """ Affiche le contenu de l'inventaire du joueur """
        if not game.player.inventory.items:
            print("Votre inventaire est vide")
        print("Votre inventaire contient :")
        for item_name, data in game.player.inventory.items.items():
            # Accède à l'instance de l'objet dans le dictionnaire
            item = data["item"]
            print(f"- {item_name}: {item.description} ({item.poids} kg)")



    def charge(self, game):
        """charger le beamer"""
        player = game.player
        #beamer = player.inventory.get("beamer")
        beamer = player.inventory["beamer"]
        if not beamer:
            print("Vous ne posséder pas de beamer pour le charger.")
        beamer.charge(player.current_room)

    def teleporte(self, game):
        """se téléporter"""
        player = game.player
        beamer = player.inventory["beamer"]
        if not beamer:
            print("Vous ne possédez pas de beamer pour l'utiliser.")

    def talk(self, game, list_of_words):
        """
        Permet au joueur d'interagir avec un PNJ.
        Les PNJ supplémentaires apparaissent après avoir parlé à l'annonceur.
        """
        if len(list_of_words) < 2:
            print("Parler à qui ?")
            return False

        # Récupérer le nom du PNJ avec la casse d'origine
        npc_name = ' '.join(list_of_words[1:])
        current_room = game.player.current_room

        # Chercher le PNJ dans la pièce actuelle en ignorant la casse
        found_npc = None
        for npc in current_room.inventory.npcs.values():
            # Vérifier si le PNJ est visible (s'il a cet attribut)
            if hasattr(npc, 'visible') and not npc.visible:
                continue

            if npc.name.lower() == npc_name.lower():
                found_npc = npc
                break

        if found_npc:
            # Obtenir le message du PNJ
            message = found_npc.get_msg()
            print(f"\n{found_npc.name} (dans {found_npc.current_room.name}) : {message}\n")

            # Si c'est l'annonceur et que c'est la première conversation
            if found_npc.name.lower() == "annonceur" and not hasattr(game, 'talked_to_announcer'):
                game.talked_to_announcer = True

                # Faire apparaître les autres PNJ
                for room in game.rooms:
                    for npc in room.inventory.npcs.values():
                        if hasattr(npc, 'visible'):
                            npc.visible = True

                # Message spécial après avoir parlé à l'annonceur
                print("\n* Les autres visiteurs du carnaval "
                "commencent à apparaître autour de toi... *")
                print("\nN'hésite pas à intéragir avec les habitants,"
                "ce qu'ils ont à t'offrir sera peut être utile dans ta quête vers le château.\n")

            elif found_npc.name.lower() == "médecin":
                # Révéler la potion si elle est présente et cachée
                if "potion" in current_room.inventory.items:
                    current_room.inventory.reveal_item("potion")
                    print("Le médecin te montre une potion cachée dans son sac !")

            elif found_npc.name.lower() == "vendeuse":
                # Révéler le tapis si présent et caché
                if "tapis" in current_room.inventory.items:
                    current_room.inventory.reveal_item("tapis")
                    print("La vendeuse te montre un tapis posé dans un coin du carnaval !")

            elif found_npc.name.lower() == "vieux marchand":
                # Révéler la bague si elle est présente et cachée
                if "bague" in current_room.inventory.items:
                    current_room.inventory.reveal_item("bague")
                    print("Le vieux marchand te montre une bague sur le sol du marché !")


            return True


        # Si le PNJ n'est pas dans la pièce actuelle, chercher dans toutes les pièces
        for room in game.rooms:
            for npc in room.inventory.npcs.values():
                # Ne pas mentionner les PNJ invisibles
                if hasattr(npc, 'visible') and not npc.visible:
                    continue

                if npc.name.lower() == npc_name.lower():
                    print(f"\n{npc.name} n'est pas ici. Il/Elle se trouve dans : {room.name}\n")
                    return False

        print(f"\nIl n'y a personne qui s'appelle '{npc_name}' dans les environs.\n")
        return False


    def give(self, game, list_of_words):
        """donner un objet à un pnj"""
        if len(list_of_words) != 3:
            print("Usage : give <personnage> <objet>")
            return False

        target = list_of_words[1].lower()
        item_name = list_of_words[2].lower()
        current_room = game.player.current_room

        item_found = None
        for name, data in game.player.inventory.items.items():
            if name.lower() == item_name:
                item_found = data["item"]
                break

        if not item_found:
            print(f"Vous n'avez pas de {item_name} dans votre inventaire.")
            return False

        if target == "garde":
            if current_room.name != "Château":
                print("Il n'y a pas de garde ici.")
                return False

            if item_name == "potion":
                game.player.inventory.remove_item("potion")
                game.victory_checker.garde_convinced = True
                chateau_room = next((room for room in game.rooms if room.name == "Château"), None)
                if chateau_room:
                    game.player.current_room = "Château"
                    game.victory_checker.is_in_chateau = True
                    print("Le garde accepte votre potion et vous laisse entrer dans le château.")
                    game.update_victory_conditions(False)  # Mise à jour silencieuse
                    return True

            elif item_name in ["pierre", "bague"]:
                if not hasattr(game.victory_checker, "objects_given"):
                    game.victory_checker.objects_given = set()

                game.victory_checker.objects_given.add(item_name)
                game.player.inventory.remove_item(item_name)

                if game.victory_checker.objects_given == {"pierre", "bague"}:
                    game.victory_checker.garde_convinced = True
                    chateau_room = next((room for room in game.rooms
                    if room.name == "Château"), None)
                    if chateau_room:
                        game.player.current_room = "Château"
                        game.victory_checker.is_in_chateau = True
                        print("Le garde accepte la pierre scintillante"
                        "et la bague et vous laisse entrer dans le château.")
                        game.update_victory_conditions(False)  # Mise à jour silencieuse
                        return True
                    print("Erreur : La salle 'Château' n'existe pas.")
                print(f"Le garde accepte votre {item_name}, mais"
                "il attend un autre objet.")

        return True
