



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
       
        player = game.player
        current_room = room.Room
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
   
    def look(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Récupérer la pièce actuelle
        current_room = game.player.current_room

        # Afficher la pièce sans répétition du nom
        print(f"Vous êtes dans {current_room.name}")

        # Afficher l'inventaire de la pièce (objets et PNJ)
        print(current_room.inventory.get_inventory())  # Utilisation de la méthode get_inventory pour afficher

        return True






      


    def take(game, list_of_words, number_of_parameters):
        if len(list_of_words) == 1:
            print("Que voulez-vous prendre ?")
            return False
        
        item_name = list_of_words[1]
        current_room = game.player.current_room
        
        # Vérifier si l'item existe dans l'inventaire de la pièce
        if item_name in current_room.inventory.items:
            item = current_room.inventory.items[item_name]  # Récupérer l'item de la pièce
            if game.player.get_current_weight() + item.poids > game.player.max_poids:
                print(f"Vous ne pouvez pas prendre '{item_name}'. Vous dépassez la limite de poids autorisée ({game.player.max_poids} kg).")
                return
            else: 
                # Ajouter l'item à l'inventaire du joueur en utilisant get_inventory
                game.player.get_inventory().add_item(item)  # Ajout dans l'inventaire du joueur
                current_room.inventory.remove_item(item_name)  # Retirer l'item de l'inventaire de la pièce
                print(f"Vous avez pris l'objet '{item_name}'.")
                # Si c'est un Beamer, afficher son explication
                if isinstance(item, Beamer):
                    print(item.explain_usage())
                return True
        else:
            print(f"L'item '{item_name}' n'est pas présent dans la pièce.")
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



    def check(game, list_of_words, number_of_parameters):
        """ Affiche le contenu de l'inventaire du joueur """
        if len(list_of_words) == 1:  # Si seul le mot 'check' est présent
            game.player.check()  # Appelle la méthode check() du joueur
        else:
            print("Commande incorrecte. Utilisez simplement 'check' pour voir votre inventaire.")

    

    def charge(game, list_of_words, number_of_parameters):
        player = game.player
        beamer = player.inventory.get("beamer")
        if not beamer:
            print("Vous ne posséder pas de beamer pour le charger.")
            return
        
        beamer.charge(player.current_room)
    
        #if len(list_of_words)!= number_of_parameters +1:
            #command_word = list_of_words[0]
            #print(MSG1.format(command_word=command_word))
            #return False
       
        #item_name = list_of_words[1]
        #item = game.player.inventory.get(item_name, None)
       
        #print(item_name)
        #if item_name in game.player.inventory:
            #item[2].charge(game.player.current_room)
            #return True
        #else:
            #print(f"L'objet '{item_name}' ne peut pas être chargé ou n'est pas un beamer")
            #return False

    def teleporte(game, list_of_words, number_of_parameters):
            player = game.player
            beamer = player.inventory.get("beamer")

            if not beamer:
                print("Vous ne possédez pas de beamer pour l'utiliser.")
                return

            beamer.teleporte(player)


    #def teleporte(game, list_of_words, number_of_parameters):
        #if len(list_of_words)!= number_of_parameters +1:
            #command_word = list_of_words[0]
            #print(MSG1.format(command_word=command_word))
            #return False
       
        #item_name = list_of_words[1]
        #item = game.player.inventory.get(item_name, None)


        #if item_name in game.player.inventory:
            #if isinstance(item[2],Beamer):
                #return item[2].use(game)
            #else:
                #print(f"L'objet '{item_name}' ne peut pas vous téléporter ou n'est pas un beamer")
                #return False
    