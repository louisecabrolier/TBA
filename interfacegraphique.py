"""interface graphique"""
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from game import Game
from player import Player

class GameGUI:
    """interface"""
    def __init__(self, game=None):
        """initialisation"""
        self.window = tk.Tk()
        self.window.title("Jeu d'aventure")
        self.window.geometry("1024x768")
        # Initialisation du joueur
        self.player = Player("Nom du joueur")
        self.player.current_room = game.foret  # Assurer que la première pièce est bien assignée
        # Chargement des images
        self.images = {}
        self.load_images()
        # Configuration de l'interface graphique
        self.canvas = tk.Canvas(self.window, width=1024, height=768)
        self.canvas.pack()

        
        if game is None:
            self.game = Game()
        else:
            self.game = game
            
        self._setup_ui()
        self._load_images()
        self.update_view()
    
    def _setup_ui(self):
        """"setup"""
        main_frame = tk.Frame(self.window)
        main_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        self.canvas = tk.Canvas(main_frame, width=800, height=600, bg='black')
        self.canvas.pack(pady=10)
        
        self.text_display = tk.Text(main_frame, height=5, width=70)
        self.text_display.pack(pady=10)
        
        input_frame = tk.Frame(main_frame)
        input_frame.pack(fill='x', pady=5)
        
        self.command_entry = tk.Entry(input_frame, width=50)
        self.command_entry.pack(side='left', padx=5)
        self.command_entry.bind('<Return>', lambda e: self.process_command())
        
        self.submit_button = tk.Button(input_frame, text="Envoyer",
                                     command=self.process_command)
        self.submit_button.pack(side='left', padx=5)
    
    def _load_images(self):
        """load images"""
        room_images = [
        "foret.jpg", "entree-de-la-cite.jpg", "carnaval.jpg", "rdcmaison.jpg",
        "maisonsoussol.jpg", "alleeprincipale.jpg", "piedouest.jpg", "marche.jpg",
        "piedcentre.jpg", "mono.jpg", "chateau.jpg", "montagnesombre.jpg",
        "endroitinconnu.jpg", "bordcite.jpg"
        ]
        for image_name in room_images:
            try:
                # Ouvre l'image avec Pillow
                image_path = f"dessin/{image_name}"
                img = Image.open(image_path)
                img = img.resize((1024, 768))  # Redimensionner l'image si nécessaire
                img_tk = ImageTk.PhotoImage(img)
                
                # Associer l'image au nom de la pièce dans le dictionnaire
                self.images[image_name] = img_tk
            except Exception as e:
                print(f"Erreur lors du chargement de l'image {image_name}: {e}")

    
    def display_message(self, message):
        """display message"""
        self.canvas.create_text(
            512, 700,  # Placer le texte en bas de la fenêtre
            text=message,
            font=("Helvetica", 16),
            fill="black"
        )
    
    def process_command(self):
        """process command"""
        command = self.command_entry.get().strip()
        if command:
            try:
                # À implémenter: traitement des commandes
                self.update_view()
            except Exception as e:
                messagebox.showerror("Erreur", str(e))
            finally:
                self.command_entry.delete(0, tk.END)
    
    def update_view(self):
        """update view"""
        current_room = self.player.current_room
        if current_room:
            self.display_message(current_room.get_long_description())
            
            # Vérifie si l'image correspondante existe dans self.images
            if current_room.image in self.images:
                self.canvas.delete("all")  # Supprimer l'ancienne image
                self.canvas.create_image(
                    512, 384,  # Placer l'image au centre de la fenêtre
                    anchor='center',
                    image=self.images[current_room.image]
                )
        
        
    
    
    def run(self):
        """run"""
        self.window.mainloop()

if __name__ == "__main__":
    gui = GameGUI()
    gui.run()