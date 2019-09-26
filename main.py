import pygame
import os
from characters import Character
from labyrinths import Labyrinth
from constants import LAB, FLOOR, MAC, KEEP, NEEDLE, TUBE, CHLOROFORME, PIXEL_ROW, PIXEL_COLUMN

class Engine:
    def init(self):
        self.backgrounds = pygame.image.load(FLOOR)
        self.mac_pic = pygame.image.load(MAC)
        self.keep_pic = pygame.image.load(KEEP)
        self.need_pic = pygame.image.load(NEEDLE)
        self.tube_pic = pygame.image.load(TUBE)
        self.chlor_pic = pygame.image.load(CHLOROFORME)


    def main(self):
        lab = Labyrinth(LAB)
        MAC_GYVER = Character()

        self.display(MAC_GYVER, lab)

        new_position = [0,0]
        end = 0
        while True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                new_position = [MAC_GYVER.position[0]-1, MAC_GYVER.position[1]]
                end = MAC_GYVER.moving(new_position, lab)
            elif keys[pygame.K_DOWN]:
                new_position = [MAC_GYVER.position[0]+1, MAC_GYVER.position[1]]
                end = MAC_GYVER.moving(new_position, lab)
            elif keys[pygame.K_LEFT]:
                new_position = [MAC_GYVER.position[0], MAC_GYVER.position[1]-1]
                end = MAC_GYVER.moving(new_position, lab)
            elif keys[pygame.K_RIGHT]:
                new_position = [MAC_GYVER.position[0], MAC_GYVER.position[1]+1]
                end = MAC_GYVER.moving(new_position, lab)
            elif keys[pygame.K_ESCAPE]:
                end == 1
            
            if end == 1:
                break
        
        self.credit()

    def credit(self):
        print('Dévelopement: Georges Morera \nUn grand merci à OpenClassrooms pour le défi et les images. \nMerci d avoir joué!')
    
    def display(self, hero, lab):
        """"affiche le jeu."""
        # Charge le fond du labyrinthe et place Mac Gyver et le gardien
        window = pygame.display.set_mode((lab.row_length*PIXEL_ROW,
                                          lab.column_length*PIXEL_COLUMN))
        for l, line in enumerate(lab.lab):
            for c, s in enumerate(line):
                pos = (l, c)
                if s == '0':
                    window.blit(self.backgrounds, pos, (0,40,20,20))
                elif s == '1':
                    window.blit(self.backgrounds, pos, (100,320,20,20))
                elif s == 'K':
                    window.blit(self.mac_pic, pos)
                elif s == 'M':
                    hero.position = pos
                    window.blit(self.keep_pic, pos)
                elif s == 'n':
                    window.blit(self.need_pic, pos)
                elif s == 't':
                    window.blit(self.tube_pic, pos)
                elif s == 'c':
                    window.blit(self.chlor_pic, pos)
        pygame.display.flip()
    

if __name__ == "__main__":
    pygame.init()
    new_game = Engine()
    new_game.main()