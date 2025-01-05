



# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.








# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"


import inventory
import room
from beamer import Beamer
from player import Player
from item import Item




class Actions:




    def go(game, list_of_words, number_of_parameters):
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




    def quit(game, list_of_words, number_of_parameters):
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




    def help(game, list_of_words, number_of_parameters):
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




    def history(game, list_of_words, number_of_parameters):
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








    def back(game, list_of_words, number_of_parameters):
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
                print("Vous ne pouvez pas revenir en arrière, aucun déplacement précédent enregistré.")
                return False

            # Pop the last position from the history and move the player back.
            previous_position = player.history.pop()

            player.position = previous_position
            #mettre a jour l'inventaire dune piece avec le back
            player.current_room = previous_position
            
            print(f"Vous êtes revenu à votre position précédente : {player.position.name}")

            return True




#inventaire
    def inventory(game, list_of_words, number_of_parameters):
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
        
        # Affichage de l'inventaire
        #print(player.get_inventory())
        #print(current_room.get_inventory())
        #return True
   
    # Dans votre fonction look
    def look(game, list_of_words, number_of_parameters):
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







    def take(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de prendre un objet.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Récupérer l'objet à prendre
        item_name = list_of_words[1]
        current_room = game.player.current_room

        # Chercher l'objet dans l'inventaire de la pièce
        visible_items = current_room.inventory.get_visible_items()
        if item_name in visible_items:
            item = visible_items[item_name]  # Now this is the actual Item object
            
            # Vérifier le poids de l'objet
            if game.player.get_current_weight() + item.poids > game.player.max_poids: 
                print("Vous avez trop de poids, vous ne pouvez pas prendre cet objet.")
                return False
            
            # Ajouter l'objet à l'inventaire du joueur
            game.player.inventory.add_item(item)
            current_room.inventory.remove_item(item_name)
            print(f"Vous avez pris {item.name}.")
            return True
        else:
            print(f"L'objet '{item_name}' n'est pas dans cette pièce.")
            return False






    def drop(game, list_of_words, number_of_parameters):
        if len(list_of_words) < 2:
            print("Que voulez-vous déposer ?")
        else:
            item_name = list_of_words[1]
            player = game.player
           
            # Chercher l'item dans l'inventaire du joueur
            if item_name in player.inventory.items:
                item_to_drop = player.inventory.items[item_name]
           
                # Retirer du dict du joueur
                del player.inventory.items[item_name]
                # Ajouter au set de la pièce
                player.current_room.inventory.add_item(item_to_drop)
                print(f"Vous avez déposé l'objet '{item_name}'")
            else:
                print(f"Vous n'avez pas de '{item_name}' dans votre inventaire.")

    #def drop(game, list_of_words, number_of_parameters):
        #if len(list_of_words) < 2:
            #print("Que voulez-vous déposer ?")
        #else:
           # item_name = list_of_words[1]
           # player = game.player
            #current_room = player.current_room

            # Vérifiez si le dépôt est autorisé dans la pièce actuelle
            #if not current_room.allows_dropping:
            # print(f"Vous ne pouvez pas déposer d'objets dans cette pièce ({current_room.name}).")
                #return

            # Chercher l'item dans l'inventaire du joueur
            #if item_name in player.inventory.items:
                #item_to_drop = player.inventory.items[item_name]

                # Retirer l'objet de l'inventaire du joueur
                #del player.inventory.items[item_name]

                # Ajouter l'objet à l'inventaire de la pièce
               # current_room.inventory.add_item(item_to_drop)
               # print(f"Vous avez déposé l'objet '{item_name}' dans {current_room.name}.")
           # else:
               # print(f"Vous n'avez pas de '{item_name}' dans votre inventaire.")



    def check(game, list_of_words, number_of_parameters):
        """ Affiche le contenu de l'inventaire du joueur """
        if len(list_of_words) == 1:  # Si seul le mot 'check' est présent
            game.player.check()  # Appelle la méthode check() du joueur
        else:
            print("Commande incorrecte. Utilisez simplement 'check' pour voir votre inventaire.")

    

    def charge(game):
        player = game.player
        #beamer = player.inventory.get("beamer")
        beamer = player.inventory["beamer"]
        if not beamer:
            print("Vous ne posséder pas de beamer pour le charger.")
            return
        
        beamer.charge(player.current_room)
    
    def teleporte(game):
            player = game.player
            beamer = player.inventory["beamer"]

            if not beamer:
                print("Vous ne possédez pas de beamer pour l'utiliser.")
                return

            beamer.teleporte(player)

    def talk(game, list_of_words, number_of_parameters):
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
                print("\n* Les autres visiteurs du carnaval commencent à apparaître autour de toi... *")
                print("\nN'hésite pas à intéragir avec les habitants, ce qu'ils ont à t'offrir sera peut être utile dans ta quête vers le château.\n")

            elif found_npc.name.lower() == "médecin":
                # Révéler la potion si elle est présente et cachée
                if "potion" in current_room.inventory.items:
                    current_room.inventory.reveal_item("potion")
                    print("Le médecin te montre une potion cachée dans cette pièce !")

            elif found_npc.name.lower() == "vendeuse":
                # Révéler le tapis si présent et caché
                if "tapis" in current_room.inventory.items:
                    current_room.inventory.reveal_item("tapis")
                    print("La vendeuse te montre un tapis caché dans cette pièce !")


            return True

        else:
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
        