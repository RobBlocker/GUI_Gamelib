#!/usr/bin/python3
# game_library.py
# Rob Blocker
# 1/27/2020

import pickle
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

'''GUI app for our Game Library Konsole Program '''

class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        lbl_title = tk.Label(text="Game Library", font=("Arial","20"))
        lbl_title.grid(row=0, column=0, columnspan=3, sticky="news")
        btn_add = tk.Button(text="add")
        btn_add.grid(row=1, column=1)
        btn_edit = tk.Button(text="edit")
        btn_edit.grid(row=2, column=1)
        btn_search = tk.Button(text="search")
        btn_search.grid(row=3, column=1)
        btn_remove = tk.Button(text="remove")
        btn_remove.grid(row=4, column=1)    
        btn_save = tk.Button(text="save")
        btn_save.grid(row=5, column=1)
        btn_quit = tk.Button(text="quit")
        btn_quit.grid(row=6, column=1)        

class AddEdit(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)        
        lbl_title = tk.Label(text="Game Info", font=("Arial","20"))
        lbl_title.grid(row=0, column=0, columnspan=3, sticky="news")
        entry_genre = tk.Entry()
        entry_genre.grid(row=1, column=1)
        entry_title = tk.Entry()
        entry_title.grid(row=2, column=1)
        entry_dev= tk.Entry()
        entry_dev.grid(row=3, column=1)
        entry_pub= tk.Entry()
        entry_pub.grid(row=4, column=1)        
        entry_sys= tk.Entry()
        entry_sys.grid(row=5, column=1)        
        entry_ryear= tk.Entry()
        entry_ryear.grid(row=6, column=1)
        entry_rate= tk.Entry()
        entry_rate.grid(row=1, column=2)        
        entry_sme= tk.Entry()
        entry_sme.grid(row=2, column=2)
        entry_price= tk.Entry()
        entry_price.grid(row=3, column=2)
        entry_beat= tk.Entry()
        entry_beat.grid(row=4, column=2)
        entry_pdate= tk.Entry()
        entry_pdate.grid(row=5, column=2) 
        entry_notes= tk.Entry()
        entry_notes.grid(row=6, column=2)         

class Edit(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)        
        lbl_title = tk.Label(text="Search for Games", font=("Arial","20"))
        lbl_title.grid(row=0, column=0, columnspan=3, sticky="news")        

class SearchGame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)        
        lbl_title = tk.Label(text="Search for Games", font=("Arial","20"))
        lbl_title.grid(row=0, column=0, columnspan=3, sticky="news")
        
class FileSaved(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)        
        lbl_title = tk.Label(text="File Saved!", font=("Arial","20"))
        lbl_title.grid(row=0, column=0, columnspan=3, sticky="news")
        btn_okay = tk.Button(text="OK")
        btn_okay.grid(row=1, column=1)  

class FileSaved(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)        
        lbl_title = tk.Label(text="File Saved!", font=("Arial","20"))
        lbl_title.grid(row=0, column=0, columnspan=3, sticky="news")
        btn_okay = tk.Button(text="OK")
        btn_okay.grid(row=1, column=1) 
        

#Main
if __name__ == "__main__":
    pickle_file = open("gamelib.pickle", "rb")
    games = pickle.load(pickle_file)
    pickle_file.close()
    
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Game Library by Rob Blocker")
    main_menu = MainMenu()
    main_menu.grid(row=0, column=0, sticky="news")
    add_edit = AddEdit()
    add_edit.grid(row=0, column=0, sticky="news")
    edit = Edit()
    edit.grid(row=0, column=0, sticky="news")
    
    root.grid_columnconfigure(0, weight=1, sticky="news")
    root.grid_rowconfigure(0, weight=1, sticky="news")
    root.mainloop()

