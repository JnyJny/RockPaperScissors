'''
'''

from .move import Move, DrawException
from .player import Player
from itertools import combinations


class Round:
    ''' 
    
    '''

    def __init__(self, players):
        '''
        :param players: list of Players
        '''

        if len(players) == 0:
            raise ValueError('Rounds need players!')
        self.winners = list(players)
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
        '''Returns a list of player_a and player_b sorted with the winner
        first. Raises DrawException if the resolution results in a draw.
        
        :param player_a: Player
        :param player_b: Player
        :return tuple:
        '''

        if player_a.move > player_b.move:
            return player_a, player_b
        
        if player_a.move < player_b.move:
            return player_b, player_a
        # player_a.move == player_b.move is a Draw
        raise DrawException()


    def play(self, moves):
        '''Plays one round of the game and returns True if there is a single
        winner, else False.

        :param moves: list of Move choices for this game.
        :return bool:
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
    def default_moves(cls):
        try:
            return Move.moveFactory(cls._rules)
        except AttributeError as e:
            raise AttributeError("missing class attribute '_moves'")
    
    @classmethod
    def playerVsComputer(cls, playername, n_rounds=3, moves=None):
        '''
        :param playername: string
        :param n_rounds:   optional integer
        :param moves:      optional list of Moves
        '''

        moves = moves or cls.default_moves()
        players = [Player(playername), Player('computer', robot=True)]
        return cls(players, moves, n_rounds)

    @classmethod
    def computerVsComputer(cls, n_robots=2, n_rounds=3, moves=None):
        '''
        :param n_robots: optional integer
        :param n_rounds: optional integer
        :param moves:    optional list of Moves
        '''
        moves = moves or cls.default_moves()
        players = [Player(f'computer-{i}', robot=True) for i in range(0,n_robots)]
        return cls(players, moves, n_rounds)

    def __init__(self, players, moves, n_rounds):
        '''
        :param players: list of Players
        :param moves: list of Moves
        :param n_rouns: integer number of rounds in the game
        '''
        self.players = players
        self.moves = moves
        self.rounds = [Round(players) for _ in range(0, n_rounds)]
        self.allbots = all(player.robot for player in players)

    def __str__(self):
        s = []
        for i, round in enumerate(self.rounds, 1):
            s.append(f'Round {i:3d}')
            s.append(str(round))
        return '\n'.join(s)
        
    def play(self):
        '''
        '''
        for i, round in enumerate(self.rounds, 1):
            print(f'Round {i:3d}')
            while round.play(self.moves) == False:
                round.draws += 1
                print('draw..')
            print(round)
    
