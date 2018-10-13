'''
'''

from .move import Move, Outcome
from .player import Player
from .game import Game

class RockPaperScissors(Game):

    _rules = { 'rock': [ Outcome.DRAW, Outcome.LOSE, Outcome.WIN],
               'paper': [ Outcome.WIN, Outcome.DRAW, Outcome.LOSE],
               'scissors': [Outcome.LOSE, Outcome.WIN, Outcome.DRAW] }    

    @classmethod
    def playerVsComputer(cls, playername, n_rounds=3):
        '''
        '''

        moves = Move.moveFactory(cls._rules)
        players = [Player(playername), Player('computer', robot=True)]
        return cls(players, moves, n_rounds)
    
    @classmethod
    def computerVsComputer(cls, n_robots=2, n_rounds=3):
        '''
        '''
        players = [Player(f'computer-{i}', robot=True) for i in range(0,n_robots)]
        moves = Move.moveFactory(cls._rules)        
        return cls(players, moves, n_rounds)


class RockPaperLizardSpockScissors(Game):

    _rules = { 'rock': [Outcome.DRAW, Outcome.LOSE, Outcome.WIN, Outcome.LOSE, Outcome.WIN],
                  'paper': [Outcome.WIN, Outcome.DRAW, Outcome.LOSE, Outcome.WIN, Outcome.DRAW],
                  'lizard': [Outcome.LOSE, Outcome.WIN, Outcome.DRAW, Outcome.WIN, Outcome.LOSE],
                  'spock': [Outcome.WIN, Outcome.LOSE, Outcome.LOSE, Outcome.DRAW, Outcome.WIN],
                  'scissors': [Outcome.LOSE, Outcome.WIN, Outcome.WIN, Outcome.LOSE, Outcome.DRAW] }    

    @classmethod
    def playerVsComputer(cls, playername, n_rounds=3):

        moves = Move.moveFactory(cls._rules)
        players = [Player(playername), Player('computer', robot=True)]
        return cls(players, moves, n_rounds)
    
    @classmethod
    def computerVsComputer(cls, n_robots=2, n_rounds=3):
        
        moves = Move.moveFactory(cls._rules)
        players = [Player(f'computer-{i}', robot=True) for i in range(0,n_robots)]
        return cls(players, moves, n_rounds)


__all__ = [ 'RockPaperScissors',
            'RockPaperLizardSpockScissors',]
            
