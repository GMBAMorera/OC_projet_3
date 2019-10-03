from random import randrange
from constants import OBJECT_TILES
from exceptions import InvalidLabyrinth

class Labyrinth:


    def __init__(self, lab):
        self.path_to_array(lab)
        self.column_length = len(self.lab)
        self.row_length = len(self.lab[0])
        self.compare()
        self.haystacking()


    def haystacking(self):
        """Place l'aiguille et les autre objets dans le labyrinthe."""
        self.array_to_list()
        for obj in OBJECT_TILES[2:]:
            # Choisit un corridor
            loc = self.lab.count('0')
            loc = randrange(loc)
            # Et vient y placer l'objet choisi
            for i, _ in enumerate(self.lab):
                if self.lab[:i+1].count('0') == loc:
                    self.lab[i] = obj
                    break
        self.list_to_array()


    def compare(self):
        """Raffine les informations brutes du fichier labyrinthe
           et vérifie sa compatibilité."""
        # Vérifie que le fichier est bien rectangle
        for line in self.lab:
            if len(line) != self.row_length:
                raise InvalidLabyrinth(
                    'toutes les lignes de votre labyrinthe \
                        doivent avoir la même taille')

        # Vérifie que le compte de lettre est exact
        self.array_to_list()
        count = self.lab.count
        if count('K') != 1 or count('M') != 1:
            raise InvalidLabyrinth("Il doit y avoir exactement un \
                                    gardien et un mac_gyver!")
        if not count('0') + count('1') + count('\n') == len(self.lab) - 2:
            raise InvalidLabyrinth('seuls les charactères 0,1,K et M \
                                    doivent être utilisé pour le labyrinthe')
        self.list_to_array()

    def path_to_array(self, lab):
        """Récupère le labyrinthe dans un fichier le transforme en tableau."""
        with open(lab) as lab:
            # récupère les données brutes du fichier, ligne par ligne
            self.lab = lab.readlines()
        # Et retire les retour à la ligne
        for i, line in enumerate(self.lab):
            if line.endswith('\n'):
                self.lab[i] = line[:-1]


    def array_to_list(self):
        """Transforme un labyrinthe exprimé en tableau
           en une liste de charactères."""
        # Place des retour à la ligne
        # pour redécouper plus facilement ensuite et concatène les lignes
        self.lab = list('\n'.join(self.lab))


    def list_to_array(self):
        """Transforme un labyrinthe exprimé en liste de charactères
           en un labyrinthe exprimé en tableau."""
        self.lab = (''.join(self.lab)).split()
