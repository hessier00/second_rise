import dice
import operator
import copy

class DiceSet(object):
    """ Contains a set of dice, to be rolled together and their results
    totaled. The total can then be modified.

    Attributes:
        _dice: a list containing the Die instances included in the dice set.
        _modifier: an integer representing the modifier value to be applied to
        the dice set's total.
        _modifier_operation: a string representing the type of mathematical
        operation to perform with the modifier and the dice set's roll result.
        _result_table: a dice_set.ResultTable object that contains all
        possible roll combinations for the dice set.

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
        self._results_table = None

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

    def build_results_table(self):
        if self._dice:
            self._results_table = ResultTable(self._dice)
        print(self._results_table)


class ResultTable(object):
    """ Manages a 2-dimensional list[list[int]] structure containing all
    possible result combinations of all dice in the dice set, as well as the
    total generated from each combination.

    Attributes:
        _result_table: a list of lists of ints that holds all possible result
        combinations of all dice in the dice set, and the resulting totals.
    """

    def __init__(self, dice):
        self._results_table = []
        if not dice:
            return
        for i in range(1, dice[0].sides + 1):
            self._results_table.append([0,i])
        # for die in dice[1,len(dice)]:
        for die in dice[1:]:
            last_state = copy.deepcopy(self._results_table)
            self._results_table = []
            index = 0
            for result in range(1,die.sides + 1):
                self._results_table.extend(copy.deepcopy(last_state))
                for i in range(0, len(last_state)):
                     self._results_table[index].append(result)
                     index += 1

    def __str__(self):
        output = ""
        for row in self._results_table:
            output += (str(row) + '\n')
        return output


for row in self._results_table:
    row[0] = sum(row[1:])
for row in self._results_table:


