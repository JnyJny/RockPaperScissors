'''
'''

from .move import DrawException
from .player import Player
from itertools import combinations


class Round:
    ''' 
    
    '''

    def __init__(self, players):

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
        self.rounds = [Round(players) for _ in range(0, n_rounds)]
        self.allbots = all(player.robot for player in players)

    def __str__(self):
        s = []
        for i, rnd in enumerate(self.rounds,1):
            s.append(f'Round {i:3d}')
            s.append(str(rnd))
        return '\n'.join(s)
        
    def play(self):
        '''
        '''
        for i, rnd in enumerate(self.rounds, 1):
            print(f'Round {i}')
            while rnd.play(self.moves) == False:
                rnd.draws += 1
                print('draw..')
            print(rnd)
    
