from constants import OBJECT_TILES, PRIME_NUMBERS
class Character:
    def __init__(self):
        self.position = (0,0)
        self.objects = 1
        self.keeper_obj = 30


    def moving(self, new_position, labyrinth):
        """Déplace un personnage dans le labyrinthe."""
        # vérifie que la case existe
        try:
            searching = labyrinth.lab[new_position[0]][new_position[1]]
        except IndexError:
            return
        # et qu'elle n'applique pas de règles spéciales        
        if (new_position[0]<0 or new_position[1]<0
            or new_position[0]>labyrinth.column_length
            or new_position[1]>labyrinth.row_length):
            return
        elif searching == '1':
            return
        elif searching == 'K':
            end = self.fighting()
            return

        # Si il n'y a pas de problèmes, donne au personnage
        # l'objet éventuel sur la case et la position de la case.
        self.position = new_position
        self.objects *= PRIME_NUMBERS[OBJECT_TILES.index(searching)]
        return end


    def fighting(self):
        """Simule l'affrontement entre le héros et son adversaire."""
        end = 1
        if self.objects%self.keeper_obj == 0:
            return end, 'bravo! Vous avez réussi à vous échapper!'
        else:
            return end, 'malheureusement, votre astuce n était pas assez \
                grande pour premettre de vous en sortir. \
                La prochaine fois peut-être...'
