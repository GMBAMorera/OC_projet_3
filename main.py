import pygame
import os

class InvalidLabyrinth(Exception):
    pass

class Character:
    def __init__(self, position):
        self.position = position
        self.objects = 1


def main():
    end = 0
    search, mac_gyver = lab_choice()
    while True:
        if pygame.K_UP.get_focused():
            new_position = [mac_gyver.position[0]-1, mac_gyver.position[1]]
            moving(mac_gyver, search, new_position, end)
        
        elif pygame.K_DOWN.get_focused():
            new_position = [mac_gyver.position[0]+1, mac_gyver.position[1]]
            moving(mac_gyver, search, new_position, end)

        elif pygame.K_LEFT.get_focused():
            new_position = [mac_gyver.position[0], mac_gyver.position[1]+1]
            moving(mac_gyver, search, new_position, end)

        elif pygame.K_RIGHT.get_focused():
            new_position = [mac_gyver.position[0], mac_gyver.position[1]+1]
            moving(mac_gyver, search, new_position, end)
        
        if end == 1:
            break
    
        credit()


def moving(mac_gyver, search, new_position, end):
    if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= 15 or new_position[1] >= 15:
        return
    try:
        s = search[new_position[0]*16 + new_position[1]]
    except IndexError:
        return

    if s == '0':
        mac_gyver.position = new_position
    elif s == 'n':
        mac_gyver.position = new_position
        mac_gyver.objects *= 2
    elif s == 't':
        mac_gyver.position = new_position
        mac_gyver.objects *= 3
    elif s == 'c':
        mac_gyver.position = new_position
        mac_gyver.objects *= 5
    elif s == 'K':
        end += 1
        if mac_gyver.objects%30 == 0:
            return 'bravo! Vous avez réussi à vous échapper!'
        else:
            return 'malheureusement, votre astuce n était pas assez grande pour premettre de vous en sortir. \
                La prochaine fois peut-être...'
    elif s == '1' or s == '\n':
        return


def lab_choice():
    """fonction initialisant le labyrinthe et les positions de départ des objets et des personnages."""
    lab = input('tapez le chemin vers votre labyrinthe, puis appuyez sur Entrée:')
    with open(lab) as lab:
        #Je vérifie que le labyrinthe est ok
        search = ''
        for i in range(15):
            buff = lab.read(16)
            if not buff.endswith('\n'):
                print('un labyrinthe est un fichier texte contenant 15 lignes de 15 caractères, \
                    \ncomposé de 1 pour exprimer des murs infranchissable,\
                    \nde 0 pour exprimer des chemins que peut emprunter Mac Gyver \net de 5 cases spéciales et uniques: \n - M pour la position \
                    initiale de Mac gyver, \n - K pour celle du guardien, \n - n, t et c pour une aiguille, un tube et du chloroforme. \
                    \nAttention, le jeu ne vérifie pas qu un chemin gagnant est possible.')
                raise InvalidLabyrinth('votre labyrinthe ne comporte pas 15 lignes de 15 colonnes')
            search += buff
        if search.count('M') + search.count('K') + search.count('n') + search.count('t') + search.count('c') != 5:
            print('un labyrinthe est un fichier texte contenant 15 lignes de 15 caractères, \
                \ncomposé de 1 pour exprimer des murs infranchissable, \
                \nde 0 pour exprimer des chemins que peut emprunter Mac Gyver \net de 5 cases spéciales et uniques: \n - M pour la position \
                initiale de Mac gyver, \n - K pour celle du guardien, \n - n, t et c pour une aiguille, un tube et du chloroforme. \
                \nAttention, le jeu ne vérifie pas qu un chemin gagnant est possible.')
            raise InvalidLabyrinth('votre labyrinthe ne défini pas d emplacement initial pour chacun des objets et personnages')
        
        #Je récupère les coordonnés de départ de Mac_Gyver
        for i, s in enumerate(search):
            if s == 'M':
                mac_gyver = Character([i//16, i-16*(i//16)])
                break
        return search, mac_gyver

def credit():
    print('Dévelopement: Georges Morera \nUn grand merci à OpenClassrooms pour le défi et les images. \nMerci d avoir joué!')

if __name__ == "__main__":
    main()