#!/usr/bin/python3
# game_library.py
# Rob Blocker
# 1/27/2020

import pickle 

'''Runs prototype for our Game Library database program'''

#Dictionary for Library
games = {}
datafile = open("gamelib.pickle", "rb")
games = pickle.load(datafile)
datafile.close()

#Functions
def add_and_edit():
    #print("Running add and edit")
    
    while True:
        print('''
        ---------------------
        Changing Your Library
        ---------------------
        
        Editing Options:
        1) Add a game
        2) Edit an already existing game
        ''')
        editing_option = input("What would you like to do? ")
        
        if editing_option == '1':
            add()
            continue_edit = False
            
        elif editing_option == '2':
            edit()
            continue_edit = False
        confirmation = input("Would you like to continue editing? ")
        if confirmation.lower() == "n":
            break
        
def add():
    new_key = len(games) + 1
    valid = False
    while not valid:
        genre = input("What is the genre? ")
        title = input("What is the title? ")
        developer = input("Who is the developer? ")
        publisher = input("Who is the publisher? ")
        system = input("What is the system it is played on? ")
        release = input("What is the release year? ")
        rating = input("What is the rating? ")
        players = input("Is it single player, mulit, or either? ")
        price = input("What is the price? ")
        beat = input("Have you beaten it? ")
        purchase = input("What is the purchase year? ")
        notes = input("Any notes? ")
        entry = [genre, title, developer, publisher, system,
                     release, rating, players, price, beat, purchase,
                     notes]
        print("------------------------")
        print("Genre: ", genre)
        print("Title: ", title)
        print("Developer: ", developer)
        print("Publisher: ", publisher)
        print("System: ", system)
        print("Release Year: ", release)
        print("Rating: ", rating)
        print("Single/multi/either: ", players)
        print("Price: ", price)
        print("Beat it?: ", beat)
        print("Purchase Year: ", purchase)
        print("Notes: ", notes)
        answer = input("Is all of this information correct? ")
        if answer.lower() == "y":
            valid = True
            games[new_key] = new_entry 

def edit():
    valid = False
    while not valid:
        print("Your current library: ")
        for key in games.keys():
            print(key, "-", games[key][1])
        edit_key = input("Which game would you like to edit? ")
        edit_key = int(edit_key)
        edit_entry = games[edit_key]
        if edit_key in games:
            print("Current genre: ", edit_entry[0])
            edit_entry[0] = input("New Genre: ")
            print("")
            print("Current title: ", edit_entry[1])
            edit_entry[1] = input("New title: ")
            print("")
            print("Current developer: ", edit_entry[2])
            edit_entry[2] = input("New developer: ")
            print("")
            print("Current publisher: ", edit_entry[3])
            edit_entry[3] = input("New publisher: ")
            print("")
            print("Current system: ", edit_entry[4])
            edit_entry[4] = input("New system: ")
            print("")
            print("Current release year: ", edit_entry[5])
            edit_entry[5] = input("New release year: ")
            print("Current rating: ", edit_entry[6])
            print("")
            edit_entry[6] = input("New rating: ") 
            print("Current single/multi player/either: ", edit_entry[7])
            edit_entry[7] = input("New single/multi player/either: ")
            print("")
            print("Current price: ", edit_entry[8])
            edit_entry[8] = input("New price: ")
            print("")
            print("Current status(beaten): ", edit_entry[9])
            edit_entry[9] = input("New status: ")
            print("")
            print("Current purchase year: ", edit_entry[10])
            edit_entry[10] = input("New purchase year: ")
            print("")
            print("Current notes: ", edit_entry[11])
            edit_entry[11] = input("New notes: ")
            
            print("------------------------")
            print("Genre: ", edit_entry[0])
            print("Title: ", edit_entry[1])
            print("Developer: ", edit_entry[2])
            print("Publisher: ", edit_entry[3])
            print("System: ", edit_entry[4])
            print("Release Year: ", edit_entry[5])
            print("Rating: ", edit_entry[6])
            print("Single/multi/either: ", edit_entry[7])
            print("Price: ", edit_entry[8])
            print("Beat it?: ", edit_entry[9])
            print("Purchase Year: ", edit_entry[10])
            print("Notes: ", edit_entry[11])
            
            answer = input("Is all of this information correct? Y/N ")
            if answer.lower() == "y":
                valid = True
                edit_entry = games[edit_key]
        else:
            print("UH OH, THERE'S NO MATCHES!") 
            
def print_all():
    #print("Running print all")
    games_key_list = games.keys()
    
    for key in games_key_list:
        print()
        print("Genre: ", games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("System: ", games[key][4])
        print("Release Year: ", games[key][5])
        print("Rating: ", games[key][6])
        print("single/multi player/either: ", games[key][7])
        print("Price: ", games[key][8])
        print("Beat it?: ", games[key][9])
        print("Purchase Year: ", games[key][10])
        print("Notes: ", games[key][11])
        print("-----------")    
    
def search():
    #print("Running search by title")
    while True:
        print('''
        -----------------------
        What's In Your Library?
        -----------------------
        
        Search Options:
        1) Genre
        2) Title
        3) Developer
        4) Publisher 
        5) System 
        6) Release Year
        7) Rating 
        8) single/multi player/either
        9) Price
        10) Beat it?
        11) Purchase Year
        ''')
        search_option = input("How would you like to search for your game? ")
        
        if search_option == '1':
            search_by_genre()
        elif search_option == '2':
            search_by_title()
        elif search_option == '3':
            search_by_developer()
        elif search_option == '4':
            search_by_publisher()
        elif search_option == '5':
            search_by_system()
        elif search_option == '6':
            search_by_release()
        elif search_option == '7':
            search_by_rating()
        elif search_option == '8':
            search_by_players()
        elif search_option == '9':
            search_by_price()
        elif search_option == '10':
            search_by_beat()
        elif search_option == '11':
            search_by_purchaseyear()
        elif search_option == 'Q' or search_option == 'q':
            quit()
        else:
            print("That is not a valid option!")               
        
        search_input = input("Would you like to continue searching? Y/N ")
        
        if search_input.lower() == 'n':
            break

            
def search_by_title():
    found_one = False
    search_results = {}
    title = input("What is the title of the game? ")
    for key in games.keys():
        if title in games[key][1]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("single/multi player/either: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beat it?: ", games[key][9])
            print("Purchase Year: ", games[key][10])
            print("Notes: ", games[key][11])
            print("-----------")
    if not found_one:
        print("NO MATCHES FOUND!") 
        
def search_by_genre():
    found_one = False
    genre = input("What is the genre of the game? ")
    for key in games.keys():
        if genre in games[key][0]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("single/multi player/either: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beat it?: ", games[key][9])
            print("Purchase Year: ", games[key][10])
            print("Notes: ", games[key][11])
            print("-----------") 
                        
    if not found_one:
        print("NO MATCHES FOUND!") 
        
def search_by_developer():
    found_one = False
    developer = input("Who developed the game? ")
    for key in games.keys():
        if developer in games[key][2]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("single/multi player/either: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beat it?: ", games[key][9])
            print("Purchase Year: ", games[key][10])
            print("Notes: ", games[key][11])
            print("-----------") 
                       
    if not found_one:
        print("NO MATCHES FOUND!") 
        
def search_by_publisher():
    found_one = False
    publisher = input("Who published the game? ")
    for key in games.keys():
        if publisher in games[key][3]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("single/multi player/either: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beat it?: ", games[key][9])
            print("Purchase Year: ", games[key][10])
            print("Notes: ", games[key][11])
            print("-----------") 
                        
    if not found_one:
        print("NO MATCHES FOUND!")

def search_by_system():
    found_one = False
    system = input("What system is it played on? ")
    for key in games.keys():
        if system in games[key][4]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("single/multi player/either: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beat it?: ", games[key][9])
            print("Purchase Year: ", games[key][10])
            print("Notes: ", games[key][11])
            print("-----------")
                       
    if not found_one:
        print("NO MATCHES FOUND!")
        
def search_by_release():
    found_one = False
    release = input("When was it released? ")
    for key in games.keys():
        if release in games[key][5]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("single/multi player/either: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beat it?: ", games[key][9])
            print("Purchase Year: ", games[key][10])
            print("Notes: ", games[key][11])
            print("-----------")
                        
    if not found_one:
        print("NO MATCHES FOUND!")
        
def search_by_rating():
    found_one = False
    rating = input("What is the rating? ")
    for key in games.keys():
        if rating in games[key][6]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("single/multi player/either: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beat it?: ", games[key][9])
            print("Purchase Year: ", games[key][10])
            print("Notes: ", games[key][11])
            print("-----------")
                       
    if not found_one:
        print("NO MATCHES FOUND!")

def search_by_players(): 
    found_one = False
    players = input("Is it single, multi player or either? ")
    for key in games.keys():
        if players in games[key][7]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/multi player/either: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beat it?: ", games[key][9])
            print("Purchase Year: ", games[key][10])
            print("Notes: ", games[key][11])
            print("-----------")
                      
    if not found_one:
        print("NO MATCHES FOUND!")
        
def search_by_price():
    found_one = False
    price = input("What was the price of the game? ")
    for key in games.keys():
        if price in games[key][8]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single/multi player/either: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beat it?: ", games[key][9])
            print("Purchase Year: ", games[key][10])
            print("Notes: ", games[key][11])
            print("-----------") 
                       
    if not found_one:
        print("NO MATCHES FOUND!")
        
def search_by_beat():
    found_one = False
    beat = input("Have you beaten it? ")
    for key in games.keys():
        if beat in games[key][9]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("single/multi player/either: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beat it?: ", games[key][9])
            print("Purchase Year: ", games[key][10])
            print("Notes: ", games[key][11])
            print("-----------")
                      
    if not found_one:
        print("NO MATCHES FOUND!")
        
def search_by_purchaseyear():
    found_one = False
    purchaseyear = input("When did ou purchase it? ")
    for key in games.keys():
        if purchaseyear in games[key][10]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("single/multi player/either: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beat it?: ", games[key][9])
            print("Purchase Year: ", games[key][10])
            print("Notes: ", games[key][11])
            print("-----------")
                       
    if not found_one:
        print("NO MATCHES FOUND!")    
    
def remove_game():
    print_all(with_keys = True)
    selected_key = input("What is the game you would like to delete? ")
    try:
        selected_key = int(selected_key)
        print_game(games[selected_key])
        confirm_deletion = input("Are you sure you want to remove? ")
        if confirm.deletion.lower() == "y":
            for keys in range(1, len(games)+1):
                if keys >= selected_key and keys != len(games):
                    games[keys] = games[keys+1]
                if keys == len(games):
                    games.pop(key)
    except:
        print("It doesn't look like you have that game in here ")
        
def save_library():
    #print("Running save library")
    datafile = open("gamelib.pickle", "wb")
    pickle.dump(games, datafile)
    datafile.close()    
    print("File saved!")
    
def quit():
    #print("Running quit")
    confirm = input("Would you like to save? Y/N ")
    if confirm.lower() == "y":
        datafile = open("gamelib.pickle", "wb")
        pickle.dump(games, datafile)
        datafile.close()    
        print("File saved! Goodbye!!")        
        exit()
    else:
        print("Okay, goodbye!")
        exit()

#Main Menu    
while True:
    print('''
    ------------------------
    It's Your Game Library!
    ------------------------
    
    Main Menu:
    1) Add/Edit Game
    2) Print All Games
    3) Search 
    4) Remove a Game
    5) Save Library
    Q) Quit 
    ''')
    
    choice = input("What would you like to do? ")
    
    if choice == "1":
        add_and_edit()
    elif choice == "2":
        print_all()
    elif choice == "3":
        search()
    elif choice == "4":
        remove_title()
    elif choice == "5":
        save_library()
    elif choice == "Q" or choice == "q":
        quit()
    else:
        print("That is not a valid option!")   