import pygame
import os
from characters import Character
from labyrinths import Labyrinth
from constants import *


def full_load(image_dict):
    """Take one picture dictionary
    and make it a loaded picture dictionary."""
    for tile in image_dict:
        # The picture must be in the 'ressource' folder
        image = '/'.join(['ressource', image_dict[tile]])
        # load the picture
        image_dict[tile] = pygame.image.load(image)
    return image_dict

class Engine:
    def __init__(self):
        self.init_dict()
        # Build labyrinth and Mac Gyver
        self.labyrinth = Labyrinth(LAB)
        self.mg = Character()
        # Load window game
        row = self.labyrinth.row_length*PIXEL
        column = max(300, self.labyrinth.column_length*PIXEL)
        self.window = pygame.display.set_mode((row + 100, column))
        # Position of the inventory objects
        self.pos_inv = {'n':(row,0), 't':(row, 100), 'c':(row, 200)}


    def init_dict(self):
        """ Build two picture dictionary."""
        # Picture of the tiles
        self.tiles = {
            '0':FLOOR, '1':WALL, 'K':KEEP, 'M':MAC,
            'n':NEEDLE, 't':TUBE, 'c':CHLOROFORME
        }
        self.tiles = full_load(self.tiles)
        # Picture of the objects inside the inventory
        self.inventory ={'I':INVENTORY, 't':BIGTUB, 'n':BIGNEED, 'c':BIGCHLOR}
        self.inventory = full_load(self.inventory)


    def main(self):
        """Launch the game.""" 
        self.display()

        while True:
            # Deal with the differents button
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


    def credit(self):
        """ Display credits."""
        pygame.init()
        self.window = pygame.display.set_mode(
                                    (self.labyrinth.row_length*PIXEL+100,
                                     self.labyrinth.column_length*PIXEL))
        while True:
            # Load credits picture
            cred = '/'.join(['ressource', CREDIT])
            self.window.blit(pygame.image.load(cred), (0,0))
            pygame.display.flip()
            # If enter is pressed, launch the game again
            # If escape is pressed, exit the game
            keys = pygame.key.get_pressed()
            pygame.event.get()
            if keys[pygame.K_ESCAPE]:
                return 1
            if keys[pygame.K_RETURN]:
                return 0



    def display(self):
        """"Display the game."""
        for l, line in enumerate(self.labyrinth.lab):
            for c, search in enumerate(line):
                # Display each tile of the labyrinth
                pos = (c*PIXEL, l*PIXEL)
                self.window.blit(self.tiles[search], pos)
                if search == "M":
                # define postion of mac gyver
                    self.mg.position = (l,c)
        # Display inventory
        self.window.blit(self.inventory['I'], (300, 0))
        pygame.display.flip()

    
    def displace(self, move):
        """Move mac Gyver on the screen."""
        # Place a floor tile on the old mac gyver position
        pos = (self.mg.position[1]*PIXEL, self.mg.position[0]*PIXEL)
        self.window.blit(self.tiles['0'], pos)
        
        new_position = self.compute_coordinate(move)
        
        # Place mac_gyver on his new position
        end, tile = self.moving(new_position)
        pos = (self.mg.position[1]*PIXEL, self.mg.position[0]*PIXEL)
        self.window.blit(self.tiles['M'], pos)

        # If an object is taken, place it inside the inventory
        if tile == 'n' or tile == 't' or tile == 'c':
            self.window.blit(self.inventory[tile], self.pos_inv[tile])
        pygame.display.flip()
        pygame.time.delay(DELAY)
        return end

    def compute_coordinate(self, move):
        """Compute coordinate of Mac Gyver new position."""
        if move == 'UP':
            new_position = (self.mg.position[0]-1, self.mg.position[1])
        elif move == 'DOWN':
            new_position = (self.mg.position[0]+1, self.mg.position[1])
        elif move == 'LEFT':
            new_position = (self.mg.position[0], self.mg.position[1]-1)
        elif move == 'RIGHT':
            new_position = (self.mg.position[0], self.mg.position[1]+1)
        return new_position
        

    def moving(self, new_pos):
        """Check if Mac Gyver new position is ok."""
        end = 0
        searching = self.is_tile(new_pos)
        
        if searching == '1':
            # Is it reachable?
            pass
        elif searching == 'K':
            # Does it contains the keeper?
            self.fighting(new_pos)
            end = 1 
        else:
            # If there is no problem, give to mac_gyver
            # the position and an eventual object.
            self.mg.position = new_pos
            self.mg.objects *= PRIME_NUMBERS[OBJECT_TILES.index(searching)]
            # Then erase the object inside the labyrinth
            row = self.labyrinth.lab[new_pos[0]]
            self.labyrinth.lab[new_pos[0]] = ''.join((row[:new_pos[1]],
                                                      '0',
                                                      row[new_pos[1]+1:]))
        return end, searching


    def is_tile(self, new_pos):
        """Check if the tile is actually inside the labyrinth."""
        try:
            return self.labyrinth.lab[new_pos[0]][new_pos[1]]
        except IndexError:
            return '1'

    
    def fighting(self, new_position):
        """Play the fight between Mc Gyver and the Keeper."""
        # Check if Mac Gyver have all the objects
        if self.mg.objects == self.mg.keeper_obj:
            # If yes, change Mac_Gyver position and launch the good end
            self.position = new_position
            end = '/'.join(['ressource', GOOD_END])
            self.window.blit(pygame.image.load(end), (0,0))
        else:
            # If not, launch the bad end
            end = '/'.join(['ressource', BAD_END])
            self.window.blit(pygame.image.load(end), (0,0))
        pygame.display.flip()
        pygame.time.delay(END_DELAY)

if __name__ == "__main__":
    while True:
        pygame.init()
        new_game = Engine()
        new_game.main()
        end = new_game.credit()
        if end == 1:
            break