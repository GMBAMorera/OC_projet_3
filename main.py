import pygame
import os
from Characters import Character
from Labyrinths import Labyrinths
from constants import KEEPER, MAC_GYVER

class Engine:

    def main(self):
        end = 0
        chosen_lab = input('quel labyrinthe voulez-vous essayer? ')
        labyrinth = Labyrinths(chosen_lab)
        search = labyrinth.choosing_lab(MAC_GYVER, KEEPER)
        new_position = None
        while True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                new_position = [MAC_GYVER.position[0]-1, MAC_GYVER.position[1]]
            elif keys[pygame.K_DOWN]:
                new_position = [MAC_GYVER.position[0]+1, MAC_GYVER.position[1]]
            elif keys[pygame.K_LEFT]:
                new_position = [MAC_GYVER.position[0], MAC_GYVER.position[1]-1]
            elif keys[pygame.K_RIGHT]:
                new_position = [MAC_GYVER.position[0], MAC_GYVER.position[1]+1]
            elif keys[pygame.K_ESCAPE]:
                break
            
            end = MAC_GYVER.moving( search, new_position, KEEPER, labyrinth)
            
            if end == 1:
                break
        
        Engine.credit(self)

    def credit(self):
        print('Dévelopement: Georges Morera \nUn grand merci à OpenClassrooms pour le défi et les images. \nMerci d avoir joué!')
    

if __name__ == "__main__":
    new_game = Engine()
    new_game.main()