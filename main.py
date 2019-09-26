import pygame
import os
from characters import Character
from labyrinths import Labyrinth
from constants import LAB, FLOOR, MAC, KEEP, NEEDLE, TUBE, CHLOROFORME, PIXEL_ROW, PIXEL_COLUMN

class Engine:
    def main(self):
        self.labyrinth = Labyrinth(LAB)
        self.mg = Character()

        self.display()
        end = 0
        while True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.displace('UP')
            elif keys[pygame.K_DOWN]:
                self.displace('DOWN')
            elif keys[pygame.K_LEFT]:
                self.displace('LEFT')
            elif keys[pygame.K_RIGHT]:
                self.displace('RIGHT')
            elif keys[pygame.K_ESCAPE]:
                end = 1

            if end == 1:
                break
        
        self.credit()


    def credit(self):
        print('Dévelopement: Georges Morera \nUn grand merci à OpenClassrooms pour le défi et les images. \nMerci d avoir joué!')


    def display(self):
        """"affiche le jeu."""
        self.backgrounds = pygame.image.load(FLOOR)
        self.mac_pic = pygame.image.load(MAC)
        self.keep_pic = pygame.image.load(KEEP)
        self.need_pic = pygame.image.load(NEEDLE)
        self.tube_pic = pygame.image.load(TUBE)
        self.chlor_pic = pygame.image.load(CHLOROFORME)

        # Charge le fond du labyrinthe et place Mac Gyver et le gardien
        self.window = pygame.display.set_mode((self.labyrinth.row_length*PIXEL_ROW,
                                          self.labyrinth.column_length*PIXEL_COLUMN))
        for c, line in enumerate(self.labyrinth.lab):
            for l, s in enumerate(line):
                pos = (l*PIXEL_ROW, c*PIXEL_COLUMN)
                if s == '0':
                    self.window.blit(self.backgrounds, pos, (0,40,20,20))
                elif s == '1':
                    self.window.blit(self.backgrounds, pos, (100,320,20,20))
                elif s == 'K':
                    self.window.blit(self.mac_pic, pos)
                elif s == 'M':
                    self.mg.position = (l, c)
                    self.window.blit(self.keep_pic, pos)
                elif s == 'n':
                    self.window.blit(self.need_pic, pos)
                elif s == 't':
                    self.window.blit(self.tube_pic, pos)
                elif s == 'c':
                    self.window.blit(self.chlor_pic, pos)
        pygame.display.flip()

    
    def displace(self, move):
        """Déplace mac_gyver d'une case."""
        pos = (self.mg.position[0]*PIXEL_ROW, self.mg.position[1]*PIXEL_COLUMN)
        self.window.blit(self.backgrounds, pos, (0,40,20,20))
        if move == 'UP':
            new_position = (self.mg.position[0]-1, self.mg.position[1])
        elif move == 'DOWN':
            new_position = (self.mg.position[0]+1, self.mg.position[1])
        elif move == 'LEFT':
            new_position = (self.mg.position[0], self.mg.position[1]-1)
        elif move == 'RIGHT':
            new_position = (self.mg.position[0], self.mg.position[1]+1)
        
        end = self.mg.moving(new_position, self.labyrinth.lab)
        pos = (self.mg.position[0]*PIXEL_ROW, self.mg.position[1]*PIXEL_COLUMN)
        self.window.blit(self.mac_pic, pos)
        pygame.display.flip()
        return end


    

if __name__ == "__main__":
    pygame.init()
    new_game = Engine()
    new_game.main()