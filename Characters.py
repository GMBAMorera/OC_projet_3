from constants import OBJECT_TILES, PRIME_NUMBERS
class Character:
    def moving(self, search, new_position, adversary, labyrinth):
        """Déplace un personnage dans le labyrinthe."""
        # vérifie que la case existe et qu'elle n'applique pas de règles spéciales
        try:
            searching = search[new_position[0]*labyrinth.row_length + new_position[1]]
        except IndexError:
            return
        
        if new_position[0]<0 or new_position[1]<0 or new_position[0]>=labyrinth.column_length-1 or new_position[1]>=labyrinth.row_length-1:
            return
        elif searching == '1' or searching == '\n':
            return
        elif searching == 'K':
            end = self.fighting(adversary)
            return

        # Si il n'y a pas de problèmes, donne au personnage l'objet éventuel sur la case et la position de la case.
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

    def __init__(self):
        self.position = [0,0]
        self.objects = 1
