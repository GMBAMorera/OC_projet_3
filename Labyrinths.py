import pygame
from random import randrange
from constants import PIXEL_ROW, PIXEL_COLUMN
from exceptions import InvalidLabyrinth

class Labyrinth:
    def choosing_lab(self, hero, adversary):
        """fonction initialisant le labyrinthe et les positions de départ des objets et des personnages."""
        backgrounds =  pygame.image.load('ressource/floor-tiles-20x20.png')
        mac_pic = pygame.image.load('ressource/MacGyver-resize.png')
        keep_pic = pygame.image.load('ressource/Gardien-resize.png')
        need_pic = pygame.image.load('ressource/aiguille-resize.png')
        tube_pic = pygame.image.load('ressource/tube_plastique-resize.png')
        chlor_pic = pygame.image.load('ressource/ether-resize.png')

        if not self.lab.endswith('.txt'):
            self.lab += '.txt'

        with open(self.lab) as lab:
            #prends les infos bruts du labyrinthe
            search = lab.readlines()
            self.column_length = len(search)
            self.row_length = len(search[0])
            for s in search[:-1]:
                if len(s) != self.row_length:
                    raise InvalidLabyrinth('toutes les lignes de votre labyrinthe doivent avoir la même taille')
            if len(search[-1]) != self.row_length - 1:
                raise InvalidLabyrinth('toutes les lignes de votre labyrinthe doivent avoir la même taille')

            search = list(''.join(search))
            if (search.count('0')
               + search.count('1')
               + search.count('K')
               + search.count('M')) != (len(search)
                                            - self.column_length
                                            + 1):
                raise InvalidLabyrinth('seuls les charactères 0,1,K et M peuvent être utilisés')
            
        # Place l'aiguille, le tube et le chloroforme aléatoirement sur un bout de corridor vide du plateau
        empty_loc = search.count('0')
        n_loc = randrange(empty_loc)
        t_loc = randrange(empty_loc - 1)
        c_loc = randrange(empty_loc - 2)
        for i, _ in enumerate(search):
            if search[:i+1].count('0') == n_loc:
                search[i] = 'n'
                break
        for i, _ in enumerate(search):
            if search[:i+1].count('0') == t_loc:
                search[i] = 't'
                break
        for i, _ in enumerate(search):
            if search[:i+1].count('0') == c_loc:
                search[i] = 'c'
                break
        
        search = ''.join(search)
        # Charge le fond du labyrinthe et place Mac Gyver et le gardien
        window = pygame.display.set_mode((self.row_length*PIXEL_ROW,self.column_length*PIXEL_COLUMN))
        for i, s in enumerate(search):
            i += 1
            pos = (PIXEL_ROW*i//self.row_length, PIXEL_COLUMN*i%self.row_length)
            char_pos = [i//self.row_length, i%self.row_length]
            if s == '0':
                window.blit(backgrounds, pos, (0,40,20,20))
            elif s == '1':
                window.blit(backgrounds, pos, (100,320,20,20))
            elif s == 'K':
                adversary.position = char_pos
                window.blit(mac_pic, pos)
            elif s == 'M':
                hero.position = char_pos
                window.blit(keep_pic, pos)
            elif s == 'n':
                window.blit(need_pic, pos)
            elif s == 't':
                window.blit(tube_pic, pos)
            elif s == 'c':
                window.blit(chlor_pic, pos)
        pygame.display.flip()

        return search

    def __init__(self, lab):
        self.lab = lab
        self.row_length = None
        self.column_length = None