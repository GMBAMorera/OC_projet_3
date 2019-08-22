from Characters import Character
from constants import PRIME_NUMBERS, OBJECT_TILES
from Exceptions import InvalidLabyrinth

class Labyrinths:
    def choosing_lab(self, hero, adversary):
        """fonction initialisant le labyrinthe et les positions de départ des objets et des personnages."""
        if not self.lab.endswith('.txt'):
            self.lab += '.txt'
        with open(self.lab) as lab:
            #Je prends les dimensions du labyrinthe et le nombre d'objets que Mac Gyver doit ramasser
            self.row_length = len(lab.readlines())
            lab.seek(0)

            search = ''
            searching = None
            while searching != '':
                searching = lab.read(1)
                search += searching
                if OBJECT_TILES.count(searching) == 1 and search.count(searching)==0:
                    adversary.objects *= PRIME_NUMBERS[OBJECT_TILES.index(searching)]
            
            self.column_length = len(search)/self.row_length
            if int(self.column_length) != self.column_length:
                raise InvalidLabyrinth('La largeur de votre labyrinthe doit être régulière.')

            #Je récupère les coordonnées de départ de Mac_Gyver et du gardien
            pos = search.index('K') +1
            adversary.position = ([pos//self.row_length, pos%self.row_length])

            pos = search.index('M') + 1
            hero.position = [pos//self.row_length, pos%self.row_length]
            return search

    def __init__(self, lab):
        self.lab = lab
        self.row_length = None
        self.column_length = None