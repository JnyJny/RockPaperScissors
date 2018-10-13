'''
'''

from enum import IntEnum, unique

@unique
class Outcome(IntEnum):
    LOSE : int = -1
    DRAW : int = 0
    WIN : int = 1
    

class DrawException(Exception):
    pass

class Move:
    
    @classmethod
    def moveFactory(cls, rules):
        '''
        :param rules: dictionary whose keys are names and
                      values are lists of Outcomes.
        '''
        
        return [cls(name, i, rules[name]) for i, name in enumerate(rules.keys())]
    
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
        return self.name
    
    @property
    def prompt(self):
        try:
            return self._prompt
        except AttributeError:
            pass
        self._prompt = f'[{self.name[0]}]{self.name[1:]}'
        return self._prompt

    def __eq__(self, other):
        return self.rules[other.index] == Outcome.DRAW

    def __gt__(self, other):
        return self.rules[other.index] > Outcome.DRAW

    def __lt__(self, other):
        return self.rules[other.index] < Outcome.DRAW
