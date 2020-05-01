"""
Main Program
"""

import pygame 
from Source import Tools, Setup 

def main():
    game = Tools.Game()
    game.run(Setup.GRAPHICS) 

if __name__ == "__main__":
    main() 
