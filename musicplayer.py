import tkinter as tk
from tkinter import filedialog
import pygame
class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.listbox = None  # Define listbox as an instance variable

    def add_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
            self.listbox.insert(tk.END, file_path)  # Update listbox reference

    def play_song(self):
        selected_index = self.listbox.curselection()  # Update listbox reference
        if selected_index:
            song_path = self.listbox.get(selected_index)
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

    def stop_song(self):
        pygame.mixer.music.stop()

def create_music_player():
    pygame.init()

    root = tk.Tk()
    root.title("Music Player")

    music_player = MusicPlayer()

    add_button = tk.Button(root, text="Add Song", command=music_player.add_song)
    add_button.pack()

    music_player.listbox = tk.Listbox(root)  # Assign listbox to instance variable
    music_player.listbox.pack()

    play_button = tk.Button(root, text="Play", command=music_player.play_song)
    play_button.pack()

    stop_button = tk.Button(root, text="Stop", command=music_player.stop_song)
    stop_button.pack()

    root.mainloop()

create_music_player()
