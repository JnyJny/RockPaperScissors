
import random

class Player:

    def __init__(self, name, auto):
        self.name = name
        self.auto = auto
        self.wins = 0
        self.losses = 0

    def make_move(self):
        if self.auto:
            return random.choice(Player.moves)[0]
        else:
            cmd = input('text [r]ock, [p]aper, or [s]cissors: ')
            return cmd


def game(player1, player2, rounds):
    for round in range(rounds):
        print('Round {} of {}!'.format(round + 1, rounds))
        move1 = player1.make_move()
        move2 = player2.make_move()
        while move1 == move2:
            print('draw, play again')
            move1 = player1.make_move()
            move2 = player2.make_move()
        if move1 == 'r' and move2 == 'p':
            player1.losses += 1
            player2.wins += 1
        elif move1 == 'p' and move2 == 's':
            player1.losses += 1
            player2.wins += 1
        elif move1 == 's' and move2 == 'r':
            player1.losses += 1
            player2.wins += 1
        elif move2 == 'r' and move1 == 'p':
            player1.wins += 1
            player2.losses += 1
        elif move2 == 'p' and move1 == 's':
            player1.wins += 1
            player2.losses += 1
        elif move2 == 's' and move1 == 'r':
            player1.wins += 1
            player2.losses += 1
        print('{}: {} / {}: {}'
            .format(player1.name, player1.wins, player2.name, player2.wins))

    if player1.wins < player2.wins:
        print('{} wins!'.format(player2.name))
    else:
        print('{} wins!'.format(player1.name))


def cjc_doit():
    player1 = Player('Connor', False)
    player2 = Player('Computer', True)
    game(player1, player2, 7)
