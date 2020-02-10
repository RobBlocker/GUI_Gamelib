#!/usr/bin/python3
# pi_make.py
# Rob Blocker
# 2/04/2020


import pickle 

games = {1: ['FPS', 'Halo 3', 'Bungee', 'Microsoft', 'Xbox 360', '2007',
             '7', 'either', '30.00', 'Yes', '1/15/2008', 'This game blows chunks!'],
         2: ['Sandbox', 'Minecraft', 'Mojang', 'Mojang', 'ps4', '2011',
             '10', 'either', '40.00', 'N/A', '7/21/2018', 'creativity comes out in this'],
         3: ['Sports', 'NHL19', 'EA Vancouver', 'EA Sports', 'ps4', '2018', '7',
             'either', '60.00', 'No', '11/17/2019', 'Same as last year'],
         4: ['RPG', 'Fallout New Vegas', 'Bethesda Game Studios', 
             'Bethesda Softworks', 'Xbox One', '2010', '8', 'Single', '40.00', 
             'Yes', '2/23/2017', 'pretty good'],
         5: ['FPS', 'B02', 'Treyarch', 'Activision', 'ps3', '2012', 
             '9', 'either', '70.00', 'Yes', '11/12/2012', 'My favorite FPS!'] }

data_file = open("gamelib.pickle", "wb")
pickle.dump(games, data_file)
data_file.close()

games = {}
datafile = open("gamelib.pickle", "rb")
games = pickle.load(datafile)
datafile.close()

