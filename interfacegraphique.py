"""interface graphique"""
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from game import Game

class GameGUI:
    """classe pour l'interface"""
    def __init__(self, game=None):
        self.window = tk.Tk()
        self.window.title("Jeu d'aventure")

        # Initialiser le jeu
        if game is None:
            self.game = Game()
            self.game.setup()
        else:
            self.game = game

        # Créer le canvas pour l'image
        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack(pady=10)

        # Zone de texte pour afficher les descriptions
        self.text_display = tk.Text(self.window, height=10, width=60)
        self.text_display.pack(pady=10)

        # Zone de saisie pour les commandes
        self.command_entry = tk.Entry(self.window, width=50)
        self.command_entry.pack(pady=5)
        self.command_entry.bind('<Return>', self.process_command)

        # Bouton pour envoyer la commande
        self.submit_button = tk.Button(self.window, text="Envoyer", command=self.send_command)
        self.submit_button.pack(pady=5)

        self.update_view()

    def display_message(self, message):
        """Affiche un message dans la zone de texte"""
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, message)

    def process_command(self):
        """Traite la commande entrée par l'utilisateur"""
        command = self.command_entry.get()
        try:
            self.game.process_command(command)
            self.update_view()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
        self.command_entry.delete(0, tk.END)

    def send_command(self):
        """Appelé quand le bouton Envoyer est cliqué"""
        self.process_command()

    def update_view(self):
        """Mettre à jour l'interface graphique en fonction de l'état du jeu"""
        # Afficher la description de la pièce actuelle
        room_description = self.game.player.current_room.get_long_description()
        self.display_message(room_description)

        # Mettre à jour l'image d'arrière-plan
        image_path = self.game.player.current_room.image
        if image_path:  # Vérifiez si une image est définie pour cette pièce
            try:
                background_image = Image.open(image_path)
                # Redimensionner l'image pour qu'elle rentre dans le canvas
                background_image = background_image.resize((800, 600), Image.Resampling.LANCZOS)
                background_photo = ImageTk.PhotoImage(background_image)

                # Supprimer l'ancienne image s'il y en a une
                self.canvas.delete("all")

                # Afficher la nouvelle image
                self.canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)
                # Garder une référence pour éviter la collecte de déchets
                self.canvas.image = background_photo
            except Exception as e:
                print(f"Erreur lors du chargement de l'image: {e}")

    def run(self):
        """Démarre l'interface graphique"""
        self.window.mainloop()
