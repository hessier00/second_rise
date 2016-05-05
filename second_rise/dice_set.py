import dice
import operator
import copy

# Constants
MOD_OPERATORS = {'PLUS': operator.add,
                 'MINUS': operator.sub,
                 'MULTIPLIED_BY': operator.mul,
                 'DIVIDED_BY': operator.truediv,
                 '+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv}


class DiceSet(object):
    """ Contains a set of dice, to be rolled together and their results
    totaled. The total can then be modified.

    Attributes:
        _dice: a list containing the Die instances included in the dice set.
        _modifier: an integer representing the modifier value to be applied to
        the dice set's total.
        _modifier_operation: a string representing the type of mathematical
        operation to perform with the modifier and the dice set's roll result.
        _stats: a dictionary containing frequency and chance of the
        occurrence of each possible total that can result from rolling the
        dice set.

    To Do:
        add roll history
        add parsing of standard dice notation
        add parameter for a list of Die objects
        Automatically build_stats if dice populated at construction time.
        add verbose (table) and terse (die notation only) version of __str__()
        handle modified results less than 0 (or 1?)
    """

    def __init__(self, notation=""):
        self._dice = []
        self._modifier = 0
        self._modifier_operation = MOD_OPERATORS['PLUS']
        self._stats = None

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
        if modifier_operation in MOD_OPERATORS.values():
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
        total = self._modifier_operation(total, self._modifier)
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
        """ Return the number of dice included in the dice set. """
        return len(self._dice)

    def build_stats(self):
        """ Generate the dice set's stats dictionary. """
        if self._dice:
            self._stats = SetStats(self._dice,
                                   self._modifier_operation,
                                   self._modifier)
        print(self._stats.csv())

    @property
    def stats(self):
        """ Return the dice set's stats dictionary. Will result in an error
        if the dice set has not been populated with dice and build_stats()
        has not been run.

        To Do:
            Return a safe-default SetStats object if the stats have not yet
            been generated.  Maybe.
        """
        return self._stats


class SetStats(object):
    """ Calculate and store stats about the possible results of a dice set.

    Attributes:
        _stats_dict: a dictionary containing the possible roll
        results for the dice_set, along with their frequency and
        combinations of all dice in the dice set.
        _combinations: a list of lists, each sub list containing one possible
        set of results for the dice set, along with the total result for that
        roll combination.
        _combo_count: an integer containing the total number of possible
        roll combinations

    To Do:
        add verbose (table) and terse (die notation only) version of __str__()
    """

    def __init__(self, dice, mod_op=MOD_OPERATORS['PLUS'], modifier=0):
        self._stats_dict = {}
        self._combinations = []
        self._generate_combos(dice)
        self._build_dict(mod_op, modifier)

    def _generate_combos(self, dice):
        """ Generate all combinations of dice rolls possible for the dice
        set.  Makes a list of the possible rolls for the first die, expands
        the list with duplicates of the initial data until the list has
        a number of copies of the first die's possible results equal to the
        number of sides of the next die, adds each of the second die's possible
        results to a set of the first die's results, producing a list of all
        possible combinations, then repeat the process for each remaining die.
        Deep copy must be used, or referential loops result, causing
        erroneous output.

        Arguments:
            dice: a list of dice.Die objects
        """
        if not dice:
            return
        # Make sure the list is clear
        self._combinations = []
        # Build the first die's results seed
        for i in range(1, dice[0].sides + 1):
            self._combinations.append([0, i])
        # Generate the full list
        for die in dice[1:]:
            last_state = copy.deepcopy(self._combinations)
            self._combinations = []
            index = 0
            for result in range(1, die.sides + 1):
                self._combinations.extend(copy.deepcopy(last_state))
                for i in range(0, len(last_state)):
                    self._combinations[index].append(result)
                    index += 1
            self._combo_count = index

    def _build_dict(self, mod_op, modifier):
        """ Generate aggregate data based on the list of all possible
        combinations.  Specifically, the count of occurrences of each possible
        result total for the dice set, along with the chance of it occurring.

        Arguments:
            mod_op: an operator object that indicates which mathematical
            operator should be used to apply the dice set's modifier.
            modifier: an integer representing the value used to modify the
            results of the dice set.
        """
        if not self._combinations:
            return
        for row in self._combinations:
            # print(str(row))
            row[0] = mod_op(sum(row[1:]), modifier)
            if row[0] not in self._stats_dict.keys():
                self._stats_dict[row[0]] = {'count': 1, 'chance': 0.0}
            else:
                self._stats_dict[row[0]]['count'] += 1
        for key in self._stats_dict:
            self._stats_dict[key]['chance'] = \
                self._stats_dict[key]['count'] / self._combo_count

    def chance_of(self, result):
        """ Return the chance of rolling a particular result with the dice
        set.

        Arguments:
            result: an int representing the result for which the chance of
            rolling it has been requested.
        """
        if not self._stats_dict:
            return 0
        return self._stats_dict[result]['chance']

    def csv(self):
        """ Return a version of of the stats dictionary suitable for
        outputting to a CSV file.
        """
        output = 'Result, Count, Chance\n'
        for key in self._stats_dict:
            output += ('{}, {}, {:.8f}\n'
                       .format(key,
                               self._stats_dict[key]['count'],
                               self._stats_dict[key]['chance']))
        return output

    def __str__(self):
        """ Return a human-readable version of of the stats dictionary."""
        output = 'Dice combinations: {}\n'.format(self._combo_count)
        for key in self._stats_dict:
            output += ('{}: {} - {:.2%}\n'
                       .format(key,
                               self._stats_dict[key]['count'],
                               self._stats_dict[key]['chance']))
        return output

    def __unicode__(self):
        self.__str__()
