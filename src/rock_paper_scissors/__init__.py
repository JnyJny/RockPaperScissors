'''Rock Paper Scissor Game
'''

from .move import Move, Outcome
from .player import Player
from .game import Game


# A rule dictionary is structured as follows:
#
# 1. The key is the name of a valid move
#
# 2. The value is a list that has as many entries as the rules dict
#    has keys. 
#
# 3. Each column in the list corresponds to a dict key, in effect
#    defining a square matrix. 
#    e.g.
#
#    Rules = { 'A', [ A,  B, C, D],
#              'B', [ A,  B, C, D],
#              'C', [ A,  B, C, D],
#              'D', [ A,  B, C, D], }
#
# 4. The value in the the matrix is the outcome for move X versus move Y
#

class RockPaperScissors(Game):
    '''Traditional Rock/Paper/Scissors
    Rules:
     Rock  beats Scissors
     Paper beats Rock
     Scissors beats Paper
    '''
    _rules = { 'rock': [ Outcome.DRAW, Outcome.LOSE, Outcome.WIN],
               'paper': [ Outcome.WIN, Outcome.DRAW, Outcome.LOSE],
               'scissors': [Outcome.LOSE, Outcome.WIN, Outcome.DRAW] }    


class RockPaperLizardSpockScissors(Game):
    ''' Rock/Paper/Lizard/Spock/Scissors
    Rules:
     Rock beats Lizard & Scissors
     Paper beats Rock & Spock
     Lizard beats Paper & Spock
     Spock beats Rock & Scissors
     Scissors beats Lizard & Paper
    '''



    
    _rules = { 'rock': [Outcome.DRAW, Outcome.LOSE, Outcome.WIN, Outcome.LOSE, Outcome.WIN],
               'paper': [Outcome.WIN, Outcome.DRAW, Outcome.LOSE, Outcome.WIN, Outcome.DRAW],
               'lizard': [Outcome.LOSE, Outcome.WIN, Outcome.DRAW, Outcome.WIN, Outcome.LOSE],
               'spock': [Outcome.WIN, Outcome.LOSE, Outcome.LOSE, Outcome.DRAW, Outcome.WIN],
               'scissors': [Outcome.LOSE, Outcome.WIN, Outcome.WIN, Outcome.LOSE, Outcome.DRAW] } 


__all__ = [ 'RockPaperScissors',
            'RockPaperLizardSpockScissors',]
            
