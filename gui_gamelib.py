#!/usr/bin/python3
# Rob Blocker
#2/11/2020
# gui_gamelib.py

#Imports
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import pickle 


'''Program to create a user-friendly interface for the interconnected game library program. 
   Go Full Screen for best experience. Buttons lead to other screens, except for Add Game.'''

#Constants
TITLE_FONT = ("Times New Roman", 30)
FONT = ("Courier", 15)

#Classes
class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, pady = 20)
        
        self.btn_add = tk.Button(self, text = " Add Game ", command = self.raise_add, font = FONT)
        self.btn_add.grid(row = 1, column = 0)
        
        self.btn_edit = tk.Button(self, text = "   Edit   ", command = self.raise_edit, font = FONT)
        self.btn_edit.grid(row = 2, column = 0)
        
        self.btn_search = tk.Button(self, text = "  Search  ", command = self.raise_search, font = FONT)
        self.btn_search.grid(row = 3, column = 0)
        
        self.btn_remove = tk.Button(self, text = "  Remove  ", command = self.raise_remove, font = FONT)
        self.btn_remove.grid(row = 4, column = 0)
        
        self.btn_save = tk.Button(self, text = "   Save   ", command = self.save, font = FONT)
        self.btn_save.grid(row = 5, column = 0)
    
    def raise_add(self):
        frm_add_or_edit.tkraise()
    
    def raise_edit(self):
        frm_edit.tkraise()
    
    def raise_search(self):
        frm_search.tkraise()
        
    def raise_remove(self):
        frm_remove.tkraise()
    
    def save(self):
        messagebox.showinfo("Save", "File Saved")
    


class AddEdit(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "  Add Game  ", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 4, pady = 20)
        
        self.lbl_genre = tk.Label(self, text = "Genre:", font = FONT)
        self.lbl_genre.grid(row = 1, column = 0)
        
        self.ent_genre = tk.Entry(self, font = FONT, bd = 3)
        self.ent_genre.grid(row = 1, column = 1)
        
        self.lbl_title = tk.Label(self, text = "Title:", font = FONT)
        self.lbl_title.grid(row = 1, column = 2)
        
        self.ent_title = tk.Entry(self, font = FONT, bd = 3)
        self.ent_title.grid(row = 1, column = 3)
        
        self.lbl_developer = tk.Label(self, text = "Developer:", font = FONT)
        self.lbl_developer.grid(row = 2, column = 0)
        
        self.ent_developer = tk.Entry(self, font = FONT, bd = 3)
        self.ent_developer.grid(row = 2, column = 1)
        
        self.lbl_publisher = tk.Label(self, text = "Publisher:", font = FONT)
        self.lbl_publisher.grid(row = 2, column = 2)
        
        self.ent_publisher = tk.Entry(self, font = FONT, bd = 3)
        self.ent_publisher.grid(row = 2, column = 3)
        
        self.lbl_platform = tk.Label(self, text = "System:", font = FONT)
        self.lbl_platform.grid(row = 3, column = 0)
        
        self.ent_platform = tk.Entry(self, font = FONT, bd = 3)
        self.ent_platform.grid(row = 3, column = 1)
        
        self.lbl_release_date = tk.Label(self, text = "Release Date:", font = FONT)
        self.lbl_release_date.grid(row = 3, column = 2)
        
        self.ent_release_date = tk.Entry(self, font = FONT, bd = 3)
        self.ent_release_date.grid(row = 3, column = 3)
        
        self.lbl_rating = tk.Label(self, text = "Rating:", font = FONT)
        self.lbl_rating.grid(row = 4, column = 0)
        
        self.ent_rating = tk.Entry(self, font = FONT, bd = 3)
        self.ent_rating.grid(row = 4, column = 1)
        
        #Setups the drop-down menu for Gamemode(s)
        gamemodes = ["Single", "Multi", "Either"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(gamemodes[0])        
        
        self.lbl_gamemodes = tk.Label(self, text = "Gamemode(s):", font = FONT)
        self.lbl_gamemodes.grid(row = 4, column = 2)
        
        self.dpdn_gamemodes = tk.OptionMenu(self, self.tkvar, *gamemodes)
        self.dpdn_gamemodes.grid(row = 4, column = 3, sticky = "news")
        
        self.lbl_price = tk.Label(self, text = "Price:", font = FONT)
        self.lbl_price.grid(row = 5, column = 0)
        
        self.ent_price = tk.Entry(self, font = FONT, bd = 3)
        self.ent_price.grid(row = 5, column = 1)
        
        self.lbl_purchase_date = tk.Label(self, text = "Purchase Date:", font = FONT)
        self.lbl_purchase_date.grid(row = 5, column = 2)
        
        self.ent_purchase_date = tk.Entry(self, font = FONT, bd = 3)
        self.ent_purchase_date.grid(row = 5, column = 3)
        
        self.chk_completed = tk.Checkbutton(self, text = "Completed?", font = FONT)
        self.chk_completed.grid(row = 6, column = 0, columnspan = 4, sticky = "news")
        
        self.lbl_notes = tk.Label(self, text = "Notes:", font = FONT)
        self.lbl_notes.grid(row = 7, column = 0,  columnspan = 4, sticky = "news")
        
        self.scl_notes = ScrolledText(self, width = 40, height = 8)
        self.scl_notes.grid(row = 8, column = 0, columnspan = 4)
        
        #Buttons to cancel adding/editing, reset the changes, or to confirm changes
        frm_add_edit_buttons = AddEditButtons(self)
        frm_add_edit_buttons.grid(row = 9, column = 0, columnspan = 4, sticky = "news")
        
        
class AddEditButtons(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.btn_cancel = tk.Button(self, text = "Cancel", command = self.cancel, font = FONT)
        self.btn_cancel.grid(row = 0, column = 0)
        
        self.btn_reset = tk.Button(self, text = "Reset", font = FONT)
        self.btn_reset.grid(row = 0, column = 1, padx = 50)
        
        self.btn_confirm = tk.Button(self, text = "Confirm", font = FONT)
        self.btn_confirm.grid(row = 0, column = 2)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
    
    def cancel(self):
        frm_menu.tkraise()


class Edit(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.lbl_which_title = tk.Label(self, text = "Which Title would you like to edit?", font = TITLE_FONT)
        self.lbl_which_title.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        titles = ["Title1", "Title2"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(titles[0])
        
        self.dpdn_titles = tk.OptionMenu(self, self.tkvar, *titles)
        self.dpdn_titles.grid(row = 1, column = 0, columnspan = 2, pady = 50, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", command = self.cancel, font = FONT)
        self.btn_cancel.grid(row = 2, column = 0, sticky = "news")
        
        self.btn_confirm = tk.Button(self, text = "Confirm", command = self.confirm, font = FONT)
        self.btn_confirm.grid(row = 2, column = 1, sticky = "news")
        
    def cancel(self):
        frm_menu.tkraise()
        
    def confirm(self):
        frm_add_or_edit.tkraise()

class Search(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        #Setup for the "Search By:" drop-down menu
        options = ["Genre", "Title", "Developer", "Publisher", "Platform", "Release Date",
                   "Rating", "Gamemode(s)", "Price", "Completion", "Purchase Date",
                   "Notes"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        #Search Parameters
        self.lbl_title = tk.Label(self, text = "Search", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 5, pady = 20)
        
        self.lbl_search_by = tk.Label(self, text = "Search By:", font = FONT)
        self.lbl_search_by.grid(row = 1, column = 0)
        
        self.dpdn_search_by = tk.OptionMenu(self, self.tkvar, *options)
        self.dpdn_search_by.grid(row = 2, column = 0, sticky = "news")
        
        self.lbl_search_for = tk.Label(self, text = "Search For:", font = FONT)
        self.lbl_search_for.grid(row = 3, column = 0)
        
        self.ent_search_for = tk.Entry(self, font = FONT)
        self.ent_search_for.grid(row = 4, column = 0)
        
        #Check boxes for printing specific catergories
        self.chk_search_filter = SearchParameters(self)
        self.chk_search_filter.grid(row = 1, column = 1, rowspan = 4)
        
        #Scrolled Text Box that shows results
        self.scl_results = ScrolledText(self, width = 40, height = 8)
        self.scl_results.grid(row = 5, column = 0, columnspan = 5)
        
        #Buttons to leave the frame, do the search action, or clear the results
        frm_search_buttons = SearchButtons(self)
        frm_search_buttons.grid(row = 6, column = 0, columnspan = 2, sticky="news")

class SearchButtons(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.btn_back = tk.Button(self, text = "Back", command = self.go_back, font = FONT)
        self.btn_back.grid(row = 0, column = 0)
        
        self.btn_back = tk.Button(self, text = "Clear", font = FONT)
        self.btn_back.grid(row = 0, column = 1, padx = 50)
        
        self.btn_back = tk.Button(self, text = "Submit", font = FONT)
        self.btn_back.grid(row = 0, column = 2)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
    def go_back(self):
        frm_menu.tkraise()

class SearchParameters(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        
        #Choice to print specified catergories
        self.lbl_print_filter = tk.Label(self, text = "Print Filter:", font = FONT)
        self.lbl_print_filter.grid(row = 0, column = 2, columnspan = 3, sticky = "news")
        
        self.chk_genre = tk.Checkbutton(self, text = "Genre", font = FONT)
        self.chk_genre.grid(row = 1, column = 2, sticky = "nsw")
        
        self.chk_title = tk.Checkbutton(self, text = "Title", font = FONT)
        self.chk_title.grid(row = 1, column = 3, sticky = "nsw")
        
        self.chk_developer = tk.Checkbutton(self, text = "Developer", font = FONT)
        self.chk_developer.grid(row = 1, column = 4, sticky = "nsw")
        
        self.chk_genre = tk.Checkbutton(self, text = "Publisher", font = FONT)
        self.chk_genre.grid(row = 2, column = 2, sticky = "nsw")
        
        self.chk_title = tk.Checkbutton(self, text = "Platform", font = FONT)
        self.chk_title.grid(row = 2, column = 3, sticky = "nsw")
        
        self.chk_developer = tk.Checkbutton(self, text = "Release Date", font = FONT)
        self.chk_developer.grid(row = 2, column = 4, sticky = "nsw")

        self.chk_genre = tk.Checkbutton(self, text = "Rating", font = FONT)
        self.chk_genre.grid(row = 3, column = 2, sticky = "nsw")
        
        self.chk_title = tk.Checkbutton(self, text = "Gamemode(s)", font = FONT)
        self.chk_title.grid(row = 3, column = 3, sticky = "nsw")
        
        self.chk_developer = tk.Checkbutton(self, text = "Price", font = FONT)
        self.chk_developer.grid(row = 3, column = 4, sticky = "nsw")

        self.chk_genre = tk.Checkbutton(self, text = "Completed?", font = FONT)
        self.chk_genre.grid(row = 4, column = 2, sticky = "nsw")
        
        self.chk_title = tk.Checkbutton(self, text = "Purchase Date", font = FONT)
        self.chk_title.grid(row = 4, column = 3, sticky = "nsw")
        
        self.chk_developer = tk.Checkbutton(self, text = "Notes", font = FONT)
        self.chk_developer.grid(row = 4, column = 4, sticky = "nsw")

class Remove(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        
        self.lbl_which_title = tk.Label(self, text = "Which Title would you like to remove?", font = TITLE_FONT)
        self.lbl_which_title.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        titles = ["Title1", "Title2"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(titles[0])
        
        self.dpdn_titles = tk.OptionMenu(self, self.tkvar, *titles)
        self.dpdn_titles.grid(row = 1, column = 0, columnspan = 2, pady = 50, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", command = self.cancel, font = FONT)
        self.btn_cancel.grid(row = 2, column = 0, sticky = "news")
        
        self.btn_confirm = tk.Button(self, text = "Confirm", command = self.cancel, font = FONT)
        self.btn_confirm.grid(row = 2, column = 1, sticky = "news")
        
    def cancel(self):
        frm_menu.tkraise()
        
    def confirm(self):
        messagebox.showinfo("Remove", "Title Removed")
        frm_menu.tkraise()

class SubFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        
        self.btn_one=tk.Buton(self, text="Cancel?")
        self.btn_one.grid(row=0, column=0)
        
        self.btn_two=tk.Buton(self, text="Delete?")
        self.btn_two.grid(row=0, column=0)
        
class App(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.btn_one=tk.Button(self, text="Welcome to Game Lib")
        self.btn_one.grid(row=0, column=0)
        
        self.btn_two=tk.Button(self, text="Welcome to Game Lib")
        self.btn_two.grid(row=0, column=0)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=2)

class OptFrame(tk.Frame):
    def __init__(self):
        options=["one","two"]
        
        tkvar= tk.stringvar(self, OptFrame)
        tkvar.set(options[0])
        
        self.menu = tk.optionMenu(self, tkvar, *options)
        self.menu = grid(row=0, column=0)


#Main Function
if __name__ == "__main__":
    pickle_file = open("gamelib.pickle", "rb")
    games = pickle.load(pickle_file)
    pickle_file.close()
    
    #Initializes the frames
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Game Library by Rob Blocker")
    
    app = App()
    app.grid(row=0, column=0)
    #root.grid_columnconfigure(0, weight=1, sticky = "news")
    #root.grid_rowconfigure(0, weight=1, sticky = "news")    
    
    frm_menu = MainMenu()
    frm_menu.grid(row = 0, column = 0, sticky = "news")
    
    frm_add_edit = AddEdit()
    frm_add_edit.grid(row = 0, column = 0, sticky = "news")
    
    frm_search = Search()
    frm_search.grid(row = 0, column = 0, sticky = "news")\
    
    frm_edit = Edit()
    frm_edit.grid(row = 0, column = 0, sticky = "news")
    
    frm_remove = Remove()
    frm_remove.grid(row = 0, column = 0, sticky = "news")
    
    
    frm_menu.tkraise()
    root.mainloop()