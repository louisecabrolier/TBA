import tkinter as tk
from tkinter import ttk, scrolledtext, simpledialog

class GameGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Jeu d'Aventure")

        # Demander le nom du joueur avant de créer la fenêtre principale
        root = tk.Tk()
        root.withdraw()  # Cache la fenêtre temporaire
        player_name = simpledialog.askstring("Nouveau jeu", "Entrez votre nom:", parent=root)
        if player_name is None:  # Si l'utilisateur annule
            player_name = "Joueur"
        root.destroy()
        
        # Créer la fenêtre principale
        self.root = tk.Tk()
        self.root.title("Jeu d'Aventure")
        
        # Configuration de l'interface (le reste du code reste identique)
        self.text_area = scrolledtext.ScrolledText(self.root, height=20, width=60)
        self.text_area.pack(pady=10, padx=10)
        
        # Zone de description avec scrollbar
        self.text_area = scrolledtext.ScrolledText(self.root, height=20, width=60)
        self.text_area.pack(pady=10, padx=10)
        
        # Frame pour la saisie et le bouton
        self.cmd_frame = ttk.Frame(self.root)
        self.cmd_frame.pack(pady=5, padx=10, fill=tk.X)
        
        # Zone de saisie
        self.cmd_entry = ttk.Entry(self.cmd_frame, width=50)
        self.cmd_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.cmd_entry.bind('<Return>', lambda e: self.process_command())
        
        # Bouton d'envoi
        self.cmd_button = ttk.Button(self.cmd_frame, text="Envoyer", command=self.process_command)
        self.cmd_button.pack(side=tk.RIGHT)
        
        # Setup initial
        self.game.setup()
        self.update_display(f"\nBienvenue {self.game.player.name} dans ce jeu d'aventure !\n")
        self.update_display("Entrez 'aide' pour connaître les commandes du jeu.\n")
        self.update_display(self.game.player.current_room.get_long_description() + "\n")
        
    def process_command(self):
        cmd = self.cmd_entry.get()
        if cmd:  # Si la commande n'est pas vide
            self.update_display(f"> {cmd}\n")  # Affiche la commande
            self.cmd_entry.delete(0, tk.END)  # Efface la zone de saisie
            
            # Traite la commande
            self.game.process_command(cmd)
            
            # Met à jour l'affichage avec la description de la pièce actuelle
            if not self.game.finished:
                self.update_display(self.game.player.current_room.get_long_description() + "\n")
        
    def update_display(self, text):
        self.text_area.insert(tk.END, text)
        self.text_area.see(tk.END)  # Défile automatiquement vers le bas
        
    def run(self):
        # Centre la fenêtre
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Lance la boucle principale
        self.root.mainloop()
