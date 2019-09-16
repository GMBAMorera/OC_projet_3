import pygame
import os
from characters import Character
from labyrinths import Labyrinth

class Engine:

    def main(self):
        chosen_lab = input('quel labyrinthe voulez-vous essayer? ')
        labyrinth = Labyrinth(chosen_lab)
        KEEPER = Character()
        MAC_GYVER = Character()
        search = labyrinth.choosing_lab(MAC_GYVER, KEEPER)

        new_position = [0,0]
        end = 0
        while True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                new_position = [MAC_GYVER.position[0]-1, MAC_GYVER.position[1]]
                end = MAC_GYVER.moving(search, new_position, KEEPER, labyrinth)
            elif keys[pygame.K_DOWN]:
                new_position = [MAC_GYVER.position[0]+1, MAC_GYVER.position[1]]
                end = MAC_GYVER.moving(search, new_position, KEEPER, labyrinth)
            elif keys[pygame.K_LEFT]:
                new_position = [MAC_GYVER.position[0], MAC_GYVER.position[1]-1]
                end = MAC_GYVER.moving(search, new_position, KEEPER, labyrinth)
            elif keys[pygame.K_RIGHT]:
                new_position = [MAC_GYVER.position[0], MAC_GYVER.position[1]+1]
                end = MAC_GYVER.moving(search, new_position, KEEPER, labyrinth)
            elif keys[pygame.K_ESCAPE]:
                end == 1
            
            if end == 1:
                break
        
        Engine.credit(self)

    def credit(self):
        print('Dévelopement: Georges Morera \nUn grand merci à OpenClassrooms pour le défi et les images. \nMerci d avoir joué!')
    

if __name__ == "__main__":
    pygame.init()
    new_game = Engine()
    new_game.main()