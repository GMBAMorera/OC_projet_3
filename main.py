import pygame
import os
from characters import Character
from labyrinths import Labyrinth
from constants import *

class Engine:
    def __init__(self):
        # Image des différentes cases
        self.tiles = {
            '0':pygame.image.load(FLOOR), '1':pygame.image.load(WALL),
            'K':pygame.image.load(KEEP), 'M':pygame.image.load(MAC),
            'n':pygame.image.load(NEEDLE), 't':pygame.image.load(TUBE),
            'c':pygame.image.load(CHLOROFORME)}
        # Image des différents objets de l'inventaire
        self.inventory = {
            'I':pygame.image.load(INVENTORY), 't':pygame.image.load(BIGTUB),
            'n':pygame.image.load(BIGNEED), 'c':pygame.image.load(BIGCHLOR)}
        # Position des différents objets de l'inventaire
        self.pos_inv = {'n':(300,0), 't':(300, 100), 'c':(300, 200)}
        # Construit le labyrinthe et Mac Gyver
        self.labyrinth = Labyrinth(LAB)
        self.mg = Character()
        # Charge la fenêtre de jeu
        self.window = pygame.display.set_mode(
                                        (self.labyrinth.row_length*PIXEL+100,
                                         self.labyrinth.column_length*PIXEL))

    def main(self):

        self.display()
        while True:
            keys = pygame.key.get_pressed()
            pygame.event.get()
            end = 0
            if keys[pygame.K_UP]:
                end = self.displace('UP')
            elif keys[pygame.K_DOWN]:
                end = self.displace('DOWN')
            elif keys[pygame.K_LEFT]:
                end = self.displace('LEFT')
            elif keys[pygame.K_RIGHT]:
                end = self.displace('RIGHT')
            elif keys[pygame.K_ESCAPE]:
                end = 1
            pygame.time.delay(DELAY)

            if end == 1:
                break
        self.credit()


    def credit(self):
        pygame.init()
        self.window = pygame.display.set_mode(
                                    (self.labyrinth.row_length*PIXEL+100,
                                     self.labyrinth.column_length*PIXEL))
        while True:
            self.window.blit(pygame.image.load(CREDIT), (0,0))
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            pygame.event.get()
            if keys[pygame.K_ESCAPE]:
                return 1
            if keys[pygame.K_RETURN]:
                return 0



    def display(self):
        """"affiche le jeu."""
        for l, line in enumerate(self.labyrinth.lab):
            for c, search in enumerate(line):
                pos = (c*PIXEL, l*PIXEL)
                self.window.blit(self.tiles[search], pos)
                if search == "M":
                    self.mg.position = (l,c)
        self.window.blit(self.inventory['I'], (300, 0))
        pygame.display.flip()

    
    def displace(self, move):
        """Déplace graphiquement mac_gyver d'une case."""
        # Place une case sur l'ancien emplacement de Mac Gyver
        pos = (self.mg.position[1]*PIXEL, self.mg.position[0]*PIXEL)
        self.window.blit(self.tiles['0'], pos)

        # Calcule les coordonnées de la nouvelle position de Mac gyver
        if move == 'UP':
            new_position = (self.mg.position[0]-1, self.mg.position[1])
        elif move == 'DOWN':
            new_position = (self.mg.position[0]+1, self.mg.position[1])
        elif move == 'LEFT':
            new_position = (self.mg.position[0], self.mg.position[1]-1)
        elif move == 'RIGHT':
            new_position = (self.mg.position[0], self.mg.position[1]+1)
        
        # Affiche le personnage et les éventuels objets récupérés
        end, tile = self.moving(new_position)
        pos = (self.mg.position[1]*PIXEL, self.mg.position[0]*PIXEL)
        self.window.blit(self.tiles['M'], pos)
        if tile == 'n' or tile == 't' or tile == 'c':
            self.window.blit(self.inventory[tile], self.pos_inv[tile])
        pygame.display.flip()
        pygame.time.delay(DELAY)
        return end


    def moving(self, np):
        """Vérifie la position d'un personnage dans le labyrinthe."""
        end = 0
        # Vérifie que la case existe
        try:
            searching = self.labyrinth.lab[np[0]][np[1]]
        except IndexError:
            return end, '0'
        
        if searching == '1':
            # Qu'elle est accessible
            return end, searching
        elif searching == 'K':
            # Ou si elle contient le gardien
            self.fighting(np)
            end = 1
            return end, searching
        else:
            # Si il n'y a pas de problèmes, donne au personnage
            # l'objet éventuel sur la case et la position de la case.
            self.mg.position = np
            self.mg.objects *= PRIME_NUMBERS[OBJECT_TILES.index(searching)]
            # Puis remplace l'éventuel objet présent par un couloir vide
            row = self.labyrinth.lab[np[0]]
            self.labyrinth.lab[np[0]] = ''.join((row[:np[1]], '0', row[np[1]+1:]))
            print(self.labyrinth.lab)
            return end, searching

    
    def fighting(self, new_position):
        """Simule l'affrontement entre le héros et son adversaire."""
        if self.mg.objects%self.mg.keeper_obj == 0:
            self.position = new_position
            self.window.blit(pygame.image.load(GOOD_END), (0,0))
        else:
            self.window.blit(pygame.image.load(BAD_END), (0,0))
        pygame.display.flip()
        pygame.time.delay(5000)

if __name__ == "__main__":
    while True:
        pygame.init()
        new_game = Engine()
        new_game.main()
        end = new_game.credit()
        if end == 1:
            break