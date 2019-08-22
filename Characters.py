from Constants import OBJECT_TILES, PRIME_NUMBERS
from Labyrinths import Labyrinths

class Character:
    def moving(self, search, new_position, adversary, labyrinth):
        """Déplace un personnage dans le labyrinthe."""
        try:
            searching = search[new_position[0]*labyrinth.row_length + new_position[1]]
        except IndexError:
            return

        if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= labyrinth.row_length or new_position[1] >= labyrinth.row_length:
            return
        elif searching == 'K':
            end = self.fighting(adversary)
            return
        elif searching == '1' or searching == '\n':
            return
        
        self.position = new_position
        self.objects *= PRIME_NUMBERS[OBJECT_TILES.index(searching)]

        return end

    def fighting(self, adversary):
        """Simule l'affrontement entre le héros et son adversaire."""
        end = 1
        if self.objects%adversary.objects == 0:
            return end, 'bravo! Vous avez réussi à vous échapper!'
        else:
            return end, 'malheureusement, votre astuce n était pas assez grande pour premettre de vous en sortir. \
                La prochaine fois peut-être...'

    def __init__(self, position):
        self.position = position
        self.objects = 1
