
import random

from itertools import combinations

class DrawException(Exception):
    pass

class Move:
    
    @classmethod
    def moveFactory(cls, names, rules):
        '''
        :param names: list of strings
        :param rules: dictionary whose keys are names and
                      values are lists of integers
        '''
        if len(rules) != len(names):
            raise ValueError('Names and rule keys must match')
        
        return [cls(name, i, rules[name]) for i, name in enumerate(names)]
    
    def __init__(self, name, index, rules):

        self.name = name
        self.rules = rules
        self.index = index

    def __repr__(self):
        return ''.join([self.__class__.__name__,
                        f'(name={self.name}, ',
                        f'index={self.index}, ',
                        f'rules={self.rules})'])

    def __str__(self):
        if len(self.name) >= 2:
            return f'[{self.name[0]}]{self.name[1:]}'
        else:
            return self.name

    def __eq__(self, other):
        return self.rules[other.index] == 0

    def __gt__(self, other):
        return self.rules[other.index] > 0

    def __lt__(self, other):
        return self.rules[other.index] < 0


def rps_move_factory():
    moves = ['rock', 'paper', 'scissors']
    rules = { 'rock': [ 0, -1, 1],
              'paper': [1, 0, -1],
              'scissors': [-1, 1, 0] }

    return Move.moveFactory(moves, rules)
    

def rplss_move_factory():
    moves = ['rock', 'paper', 'lizard', 'spock', 'scissors']
    rules = { 'rock': [0, -1, 1, -1, 1],
              'paper': [1, 0, -1, 1, 0],
              'lizard': [-1, 1, 0, 1, -1],
              'spock': [1, -1, -1, 0, 1],
              'scissors': [-1, 1, 1, -1, 0] }
    return Move.moveFactory(moves, rules)
    

class Player:
    
    def __init__(self, name, robot=False):
        self.name = name
        self.robot = robot
        self.move = None

    def __str__(self):
        return f'{self.name:20s}: move {self.move.name!s}'


    def prompt(self, moves):
        s = ', '.join([str(m) for m in moves])
        return f'{s}? '
        
    def take_turn(self, moves):
        
        if self.robot:
            self.move = random.choice(moves)
            return self.move
            
        while True:
            name = input(self.prompt(moves))
            name.lower()
            for move in moves:
                if name[0] == move.name.lower()[0]:
                    self.move = move
                    return self.move
            else:
                print(f'Invalid move: {name}')

class Round:
    ''' 
    
    '''

    def __init__(self, players):

        if len(players) == 0:
            raise ValueError('Rounds need players!')
        self.winners = players[:]
        self.losers = []
        self.draws = 0

    def __str__(self):

        s = []

        if len(self.winners) > 1:
            for w in self.winners:
                s.append(f'Draw {w!s}')
        else:
            s.append(f' Win {self.winners[0]!s}')
            
        for loser in self.losers:
            s.append(f'     {loser!s}')        
        return '\n'.join(s)


    def _resolve(self, player_a, player_b):
        ''' 
        '''

        if player_a.move > player_b.move:
            return player_a, player_b
        
        if player_a.move < player_b.move:
            return player_b, player_a
        
        raise DrawException()


    def play(self, moves):
        '''
        Returns True if there is a single winner, else False
        '''
        
        if len(self.winners) == 1:
            return True

        for player in self.winners:
            player.take_turn(moves)

        winners = []

        for p0, p1 in combinations(self.winners, 2):
            try:
                w, l = self._resolve(p0, p1)
                winners.append(w)
                self.losers.append(l)
            except DrawException:
                winners.append(p0)
                winners.append(p1)

        self.winners = winners

        return len(self.winners) == 1
    
    

class Game:
    
    @classmethod
    def playerVsComputer(cls, playername, moves, n_rounds=3):
        players = [Player(playername), Player('computer', robot=True)]
        return cls(players, moves, n_rounds)

    @classmethod
    def computerVsComputer(cls, moves, n_robots=2, n_rounds=3):
        players = [Player(f'computer-{i}', robot=True) for i in range(0,n_robots)]
        return cls(players, moves, n_rounds)
    
    def __init__(self, players, moves, n_rounds):
        self.players = players
        self.moves = moves
        self.rounds = [Round(players)] * n_rounds
        self.allbots = all(player.robot for player in players)

    def __str__(self):
        s = []
        for i, round in enumerate(self.rounds,1):
            s.append(f'Round {i:3d}')
            s.append(str(round))
        return '\n'.join(s)
        

    def play(self):
        '''
        '''
        for i, round in enumerate(self.rounds, 1):
            print(f'Round {i}')
            while round.play(self.moves) == False:
                round.draws += 1
                print('draw..')
            print(round)


class RockPaperScissors(Game):

    @classmethod
    def playerVsComputer(cls, playername, n_rounds=3):
        players = [Player(playername), Player('computer', robot=True)]
        return cls(players, rps_move_factory(), n_rounds)
    
    @classmethod
    def computerVsComputer(cls, n_robots=2, n_rounds=3):
        players = [Player(f'computer-{i}', robot=True) for i in range(0,n_robots)]
        return cls(players, rps_move_factory(), n_rounds)
    

class Player_cjc:

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


def game_cjc(player1, player2, rounds):
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
    player1 = Player_cjc('Connor', False)
    player2 = Player_cjc('Computer', True)
    game_cjc(player1, player2, 7)


game = RockPaperScissors.playerVsComputer('Erik')


