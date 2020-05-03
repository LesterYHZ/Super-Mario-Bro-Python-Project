"""
Main Program
"""

import pygame 
from Source import Tools, Setup 
from Source.State import Main_Menu, Load_Screen, Level

def main():

    state_dict = {
        "Main_Menu": Main_Menu.MainMenu(),
        "Load_Screen": Load_Screen.LoadScreen(),
        "Level": Level.Level()
    }

    game = Tools.Game(state_dict,"Main_Menu")
    # state = Main_Menu.MainMenu()
    # state = Load_Screen.LoadScreen()
    # state = Level.Level()
    game.run() 

if __name__ == "__main__":
    main() 
