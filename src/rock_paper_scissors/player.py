'''
'''

from random import choice

class Player:
    
    def __init__(self, name, robot=False):
        self.name = name
        self.robot = robot
        self.move = None

    def __repr__(self):
        
        return ''.join([self.__class__.__name__,
                        f'(name={self.name}, ',
                        f'robot={self.robot})'])

    def __str__(self):
        return f'{self.name:10s}: move {self.move!s}'

    def prompt(self, moves):
        s = ', '.join([m.prompt for m in moves])
        return f'{s}? '
        
    def take_turn(self, moves):
        
        if self.robot:
            self.move = choice(moves)
            return self.move
            
        while True:
            name = input(self.prompt(moves))
            name.lower()
            for move in moves:
                if move.name.startswith(name):
                    self.move = move
                    return self.move
                    # NOTREACHED
            else:
                print(f'Invalid move: {name}')
