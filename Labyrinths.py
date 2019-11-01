from random import randrange
from constants import OBJECT_TILES
from Exceptions import InvalidLabyrinth

class Labyrinth:


    def __init__(self, lab):
        self.path_to_array(lab)
        self.column_length = len(self.lab)
        self.row_length = len(self.lab[0])
        self.compare()
        self.haystacking()


    def haystacking(self):
        """Put the needle and other objects into the labyrinth."""
        temp = self.array_to_list()

        for obj in OBJECT_TILES[2:]:
            # Choose a floor tile
            loc = temp.count('0')
            loc = randrange(loc)
            # Et put it the object
            for i, _ in enumerate(temp):
                if temp[:i+1].count('0') == loc:
                    temp[i] = obj
                    break
        self.list_to_array(temp)


    def compare(self):
        """Check if the labyrinth will function."""
        # Check if the labyrinth is a rectangel
        for line in self.lab:
            if len(line) != self.row_length:
                raise InvalidLabyrinth(
                    'toutes les lignes de votre labyrinthe \
                        doivent avoir la même taille')

        # Check if all the good letters have been used
        temp = self.array_to_list()
        count = temp.count
        if count('K') != 1 or count('M') != 1:
            raise InvalidLabyrinth("Il doit y avoir exactement un \
                                    gardien et un mac_gyver!")
        if not count('0') + count('1') + count('\n') == len(temp) - 2:
            raise InvalidLabyrinth('seuls les charactères 0,1,K et M \
                                    doivent être utilisé pour le labyrinthe')

    def path_to_array(self, lab):
        """Transform a folder to a labyrinth to an array."""
        with open(lab) as lab:
            self.lab = lab.readlines()
        # delete all new lines typo
        for i, line in enumerate(self.lab):
            if line.endswith('\n'):
                self.lab[i] = line[:-1]


    def array_to_list(self):
        """Transform a labyrinth-array to a labyrinth-list."""
        # Plac new line typo in order to easily cut the list again latter
        return list('\n'.join(self.lab))


    def list_to_array(self, temp):
        """Transform a labyrinth-list to a labyrinth-array."""
        self.lab = (''.join(temp)).split()
