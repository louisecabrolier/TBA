"""Actions""" # pylint: disable = too-many-branches
# pylint: disable = unused-argument 
#on ne peut pas les enlever car nécessaire pour le fonctionnement du jeu


from beamer import Beamer

# The error message is stored in the MSG0 and MSG1 variables
# and formatted with the command_word variable
# the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    """définir les actions possibles dans le jeu"""

    def __init__(self):
        """initialisation"""
        self.player = None
        self.foret = None
        self.door = None
        self.entreecite = None
        self.defeat_checker = None
        self.carnaval = None
        self.commands = None
        self.carnaval_npcs_revealed = None
        self.victory_checker = None
        self.rooms = None
        self.carnaval_first_visit = None
        self.limited_exits = None
        self.finished = None


    def go(self, list_of_words, number_of_parameters):
        """
        Faire bouger le joueur dans la direction donnée
        """
        # Vérification du nombre de paramètres
        if len(list_of_words) != number_of_parameters + 1:
            print("\nVeuillez spécifier une direction.\n")
            return False

        # Validation de la direction
        directions_values = {"N", "S", "E", "O", "U", "D"}
        direction = list_of_words[1].upper()
        if direction not in directions_values:
            print("\nDirection invalide.\n")
            return False

        # Cas spécial : Forêt vers Cité
        if self.player.current_room == self.foret and direction == "N":
            # Tenter d'ouvrir la porte avec l'inventaire actuel
            self.door.try_open(self.player.inventory.items)
            if not self.door.is_open:
                return False

            print("\nVous ouvrez les portes de la cité avec la clé"
            "et celles-ci se referment derrière vous.")
            print("Vous êtes maintenant dans l'entrée de la cité")
            self.player.history.append(self.player.current_room)
            self.player.current_room = self.entreecite
            self.door.close()
            return True

        # Vérification des restrictions à l'entrée de la cité
        if self.player.current_room == self.entreecite and self.limited_exits:
            if direction != "O":
                print("\nVous ne pouvez aller qu'à l'ouest pour l'instant.\n")
                return False

        # Obtention de la prochaine salle
        next_room = self.player.current_room.exits.get(direction)
        if next_room is None:
            print("\nVous ne pouvez pas aller dans cette direction.\n")
            return False

        # Ajouter la pièce actuelle à l'historique avant de se déplacer
        self.player.history.append(self.player.current_room)


        # Déplacement du joueur
        self.player.current_room = next_room

        # Gestion des cas spéciaux
        if next_room.name == "Endroit inconnu":
            self.defeat_checker.update_condition(True)
            print(f"\nVous êtes dans {next_room.name}")
        elif next_room == self.carnaval and self.carnaval_first_visit:
            print("\nBienvenue au Carnaval ! Utilisez 'look' pour observer autour de vous.")
            print("Parlez aux différentes personnes"
            "que vous verrez pour en savoir plus sur le jeu.")
            self.carnaval_first_visit = False
            self.limited_exits = False
        else:
            print(f"\nVous êtes dans {next_room.name}")

        return True




    def quitter(self, list_of_words, number_of_parameters):
        """
        Quitter le jeu.

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): La liste des mots dans la commande.
            number_of_parameters (int): Le nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.
        """
        # Vérifie si le nombre de paramètres est correct
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(f"Erreur : la commande '{command_word}'"
            "nécessite {number_of_parameters} paramètre(s).")
            return False

        # Quitter le jeu
        player = self.player
        print(f"\nMerci {player.name} d'avoir joué. Au revoir.\n")
        self.finished = True
        return True




    def aide(self, list_of_words, number_of_parameters):
        """
        Donne la liste des commandes disponibles
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print("\nVoici les commandes disponibles:")
        for command in self.commands.values():
            print("\t- " + str(command))
        print()
        return True




    def history(self, list_of_words, number_of_parameters):
        """
        Affiche l'historique des pièces visitées par le joueur.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Afficher l'historique en utilisant la nouvelle méthode get_history
        print(self.player.get_history())
        return True








    def back(self, list_of_words, number_of_parameters):
        """
        Revenir à la position précédente
        """
        player = self.player
        l = len(list_of_words)

        #Si il n'y a pas le bon nombre de paramètres
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        #Vérifier qu'il y a bien une ancienne position
        if not player.history:
            print("Vous ne pouvez pas revenir en arrière,"
            "aucun déplacement précédent enregistré.")
            return False

        previous_position = player.history.pop()

        player.position = previous_position
        #mettre a jour l'inventaire dune piece avec le back
        player.current_room = previous_position

        print(f"Vous êtes revenu à votre position précédente : {player.position.name}")

        return True




#inventaire
    def inventory(self, list_of_words, number_of_parameters):
        """
        Affiche l'inventaire du joueur
        Même chose que check
        """
        return Actions.check(self, list_of_words, number_of_parameters)



    # Dans votre fonction look
    def look(self, list_of_words, number_of_parameters):
        """
        Permet au joueur de regarder autour de lui ou un objet spécifique.
        Ne montre que les PNJ visibles (annonceur au début, puis tous après lui avoir parlé).
        """
        # Obtention de la salle courante
        current_room = self.player.current_room

        # Affichage du nom et de la description de la salle
        print(f"\nVous êtes {current_room.description}")

        # Gestion des objets dans la pièce
        all_items = current_room.inventory.items  # Tous les objets de l'inventaire
        if not all_items:
            print("\nIl n'y a aucun objet dans cette pièce.")


        # Gestion des objets visibles
        visible_items = current_room.inventory.get_visible_items()
        if visible_items:
            print("\nObjets visibles :")
            for item in visible_items.values():
                if isinstance(item, dict):  # Vérifie si c'est un dictionnaire
                    item = item["item"]    # Récupère l'objet réel
                print(f" - {item.name} : {item.description}")
        else:
            print("\nIl n'y a aucun objet visible dans cette pièce.")

        # Gestion des PNJ
        visible_npcs = []

        if current_room == self.carnaval:
            # Dans le carnaval : l'annonceur est toujours visible initialement
            for npc in current_room.inventory.npcs.values():
                # Si c'est l'annonceur ou le villageois (s'il est visible)
                if npc.visible and (npc.name == "Annonceur" or
                                (npc.name == "Villageois" and npc.visible) or
                                (self.carnaval_npcs_revealed)):
                    visible_npcs.append(npc)
        else:
            # Pour les autres salles : tous les PNJ visibles
            visible_npcs = [npc for npc in current_room.inventory.npcs.values() if npc.visible]

        # Affichage des PNJ
        if visible_npcs:
            print("\nPersonnages :")
            for npc in visible_npcs:
                print(f" - {npc.name} : {npc.description}")


        return True



    def take(self, list_of_words, number_of_parameters):
        """
        Permet au joueur de prendre un objet.
        """
        if len(list_of_words) != number_of_parameters + 1:
            if len(list_of_words) == 1:
                print("Que voulez-vous prendre?")
                return False
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        item_name = list_of_words[1].lower()
        current_room = self.player.current_room

        # Chercher l'item parmi les items visibles
        item_found = None
        for key, data in current_room.inventory.items.items():
            if data["item"].name.lower() == item_name and not data["hidden"]:
                item_found = data["item"]
                break

        if item_found:
            if self.player.add(item_found):
                # On utilise le nom en minuscules pour le retrait
                current_room.inventory.remove_item(item_name)
                print(f"Vous avez pris {item_found.name}.")
                return True
            else:
                print(f"Vous ne pouvez pas prendre {item_found.name}, poids maximum dépassé.")
                return False
        else:
            print(f"L'item n'est pas dans cette pièce.")
            return False



    def drop(self, list_of_words, number_of_parameters):
        """déposer un objet"""
        if len(list_of_words) < 2:
            print("Que voulez-vous déposer ?")
        item_name = list_of_words[1].lower()  # Normaliser le nom de l'item
        player = self.player
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
        else:
            print(f"Vous n'avez pas de '{item_name}' dans votre inventaire.")

    def check(self, list_of_words, number_of_parameters):
        """ Affiche le contenu de l'inventaire du joueur """
        if not self.player.inventory.items:
            print("Votre inventaire est vide")
        else:
            print("Votre inventaire contient :")
            for item_name, data in self.player.inventory.items.items():
            # Accède à l'instance de l'objet dans le dictionnaire
                item = data["item"]
                print(f"- {item_name}: {item.description} ({item.poids} kg)")



    def charge(self, list_of_words, number_of_parameters):
        """charger le beamer"""
        player = self.player
        #beamer = player.inventory.get("beamer")
        beamer = player.inventory["beamer"]
        if not beamer:
            print("Vous ne posséder pas de beamer pour le charger.")
        beamer.charge(player.current_room)

    def teleporte(self, list_of_words, number_of_parameters):
        """
        Se téléporter en utilisant le beamer.
        """
        try:
            # Vérifier si le beamer est dans l'inventaire
            beamer = self.player.inventory["beamer"]
            if beamer and isinstance(beamer, Beamer):
                # Utiliser le beamer pour la téléportation
                beamer.teleporte(self.player)
                # Afficher la description de la nouvelle pièce
                print(self.player.current_room.get_long_description())
            else:
                print("Vous ne possédez pas de beamer pour l'utiliser.")
        except KeyError:
            print("Vous ne possédez pas de beamer pour l'utiliser.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la téléportation : {str(e)}")

    def talk(self, list_of_words, number_of_parameters):
        """
        Permet au joueur d'interagir avec un PNJ.
        Les PNJ supplémentaires apparaissent après avoir parlé à l'annonceur.
        """
        if len(list_of_words) < 2:
            print("Parler à qui ?")
            return False

        # Récupérer le nom du PNJ avec la casse d'origine
        npc_name = ' '.join(list_of_words[1:])
        current_room = self.player.current_room

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
            """
            # Si c'est l'annonceur et que c'est la première conversation
            if found_npc.name.lower() == "annonceur" and not hasattr(self, 'talked_to_announcer'):
                self.talked_to_announcer = True

                # Faire apparaître les autres PNJ
                for room in self.rooms:
                    for npc in room.inventory.npcs.values():
                        if hasattr(npc, 'visible'):
                            npc.visible = True

                # Message spécial après avoir parlé à l'annonceur
                print("\n* Les autres visiteurs du carnaval "
                "commencent à apparaître autour de toi... *")
                print("\nN'hésite pas à intéragir avec les habitants,"
                "ce qu'ils ont à t'offrir sera peut être utile dans ta quête vers le château.\n")
            """
            if found_npc.name.lower() == "annonceur":
                if self.player.current_room.name.lower() == "carnaval":
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
                    #Mettre à jour les sorties limitées
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
                    return False
                print("\nL'annonceur n'est pas ici.\n")
                return False
            elif found_npc.name.lower() == "médecin":
                # Révéler la potion si elle est présente et cachée
                if "potion" in current_room.inventory.items:
                    potioncachee = current_room.inventory.items["potion"]["hidden"]
                    if potioncachee:
                        current_room.inventory.reveal_item("potion")
                        print("Le médecin te montre une potion cachée dans son sac !")

            elif found_npc.name.lower() == "vendeuse":
                # Révéler le tapis si présent et caché
                if "tapis" in current_room.inventory.items:
                    tapiscache = current_room.inventory.items["tapis"]["hidden"]
                    if tapiscache:
                        current_room.inventory.reveal_item("tapis")
                        print("La vendeuse te montre un tapis posé"
                        "dans un coin du carnaval !")

            elif found_npc.name.lower() == "vieux marchand":
                # Révéler la bague si elle est présente et cachée
                if "bague" in current_room.inventory.items:
                    baguecachee = current_room.inventory.items["bague"]["hidden"]
                    if baguecachee:
                        current_room.inventory.reveal_item("bague")
                        print("Le vieux marchand te montre une bague"
                        "sur le sol du marché !")

            elif found_npc.name.lower() == "villageois":
                self.defeat_checker.has_talked_to_villageois = True
                print("\nDÉFAITE: Vous avez été infecté par le villageois!\n")
                self.finished = True  # Terminer le jeu immédiatement


        # Si le PNJ n'est pas dans la pièce actuelle chercher ailleurs
        for room in self.rooms:
            for npc in room.inventory.npcs.values():
                # Ne pas mentionner les PNJ invisibles
                if hasattr(npc, 'visible') and not npc.visible:
                    continue

        return False

 


    def give(self, list_of_words, number_of_parameters):
        """donner un objet à un pnj"""
        if len(list_of_words) != 3:
            print("Usage : give <personnage> <objet>")
            return False

        target = list_of_words[1].lower()
        item_name = list_of_words[2].lower()
        current_room = self.player.current_room

        item_found = None
        for name, data in self.player.inventory.items.items():
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
                self.player.inventory.remove_item("potion")
                self.victory_checker.garde_convinced = True
                chateau_room = next((room for room in self.rooms if room.name == "Château"), None)
                if chateau_room:
                    self.player.current_room = "Château"
                    self.victory_checker.is_in_chateau = True
                    print("Le garde accepte votre potion et vous laisse entrer dans le château.")
                    self.update_victory_conditions()  # Mise à jour silencieuse
                    return True

            elif item_name in ["pierre", "bague"]:
                if not hasattr(self.victory_checker, "objects_given"):
                    self.victory_checker.objects_given = set()

                self.victory_checker.objects_given.add(item_name)
                self.player.inventory.remove_item(item_name)

                if self.victory_checker.objects_given == {"pierre", "bague"}:
                    self.victory_checker.garde_convinced = True
                    chateau_room = next((room for room in self.rooms
                    if room.name == "Château"), None)
                    if chateau_room:
                        self.player.current_room = "Château"
                        self.victory_checker.is_in_chateau = True
                        print("Le garde accepte la pierre scintillante"
                        "et la bague et vous laisse entrer dans le château.")
                        self.update_victory_conditions()  # Mise à jour silencieuse
                        return True
                    print("Erreur : La salle 'Château' n'existe pas.")
                print(f"Le garde accepte votre {item_name}, mais"
                "il attend un autre objet.")

            else:
                print("\nLe garde n'est pas intéressé par cet objet.")
                return True
