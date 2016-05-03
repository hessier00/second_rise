import dice
import operator

class DiceSet(object):
    """ Contains a set of dice, to be rolled together and their results
    totaled. The total can then be modified.

    Attributes:
        _dice: a list containing the Die instances included in the dice set.
        _modifier: an integer representing the modifier value to be applied to
        the dice set's total.
        _modifier_operation: a string representing the type of mathematical
        operation to perform with the modiifier and the dice set's roll result.

    To Do:
        add roll history
        add result probabilities
        add parsing of standard dice notation

    """

    # Class Constants
    OPERATORS = {'PLUS': operator.add,
                 'MINUS': operator.sub,
                 'MULTIPLIED_BY': operator.mul,
                 'DIVIDED_BY': operator.truediv,
                 '+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv}

    def __init__(self, notation=""):
        self._dice = []
        self._modifier = 0
        self._modifier_operation = self.OPERATORS['PLUS']

    @property
    def dice(self):
        return self._dice

    @property
    def modifier(self):
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        if modifier > 0:
            self._modifier = int(modifier)

    @property
    def modifier_operation(self):
        return self._modifier_operation

    @modifier_operation.setter
    def modifier_operation(self, modifier_operation):
        if modifier_operation in self.OPERATORS.values():
            self._modifier_operation = modifier_operation

    def add_die(self, die):
        # if isinstance(die, dice.Die):
        self._dice.append(die)

    def roll(self):
        for die in self._dice:
            die.roll()

    @property
    def result(self):
        total = 0
        for die in self._dice:
            total += die.result
        return total

    @property
    def rolled(self):
        for die in self._dice:
            return die.rolled

    @property
    def valid(self):
        for die in self._dice:
            return die.valid

    @property
    def dice_count(self):
        """ Return the number of dice included in the dice set.
        """
        return len(self._dice)







