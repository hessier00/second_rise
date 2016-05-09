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
        Add result _future_, and undo/redo (future is what the current roll
        would become if you undo to a step back in _history.
        add parsing of standard dice notation
        add parameter for a list of Die objects

        handle modified results less than 0 (or 1?)
    """

    def __init__(self, notation=""):
        self._dice = []
        self._modifier = 0
        self._modifier_operation = MOD_OPERATORS['PLUS']
        self._stats = None
        self._history = []
        # Automatically build_stats if dice populated at construction time.
        if self._dice:
            self.build_stats()

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
        """ Roll all the dice in the set, saving any previous results as
        history.
        """
        if self.rolled:
            self._history.append(self.result)
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
        if not self._dice:
            return False
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

    @property
    def stats(self):
        """ Return the dice set's stats dictionary. """
        return self._stats

    @property
    def history(self):
        return self._history

    def clear_history(self):
        """ Clears the die's roll history. """
        self._history = []

    def describe_dice(self):
        """ Generate a string description of the dice in the set using
        standard dice notation, i.e. '3d10+4d6+3d5' """
        if not self.valid:
            return ""
        dice_counts = {}
        for die in self._dice:
            if die.sides not in dice_counts.keys():
                dice_counts[die.sides] = 1
            else:
                dice_counts[die.sides] += 1
        dice_list = []
        for die_type in dice_counts:
            dice_list.append([die_type, dice_counts[die_type]])
            dice_list.sort(reverse=True)
        description = '{}d{}'.format(dice_list[0][1], dice_list[0][0])
        for die_type in dice_list[1:]:
            description += '+{}d{}'.format(die_type[1], die_type[0])
        return description

    def __str__(self, verbose=False):
        """ Return either the die value as a string (terse) or a more
        detailed response (verbose).

        Arguments:
            verbose: a boolean value representing whether or not the return
            value should be verbose.
        """
        if not verbose:
            return str(self.result)
        return '{}: {}'.format(self.describe_dice(), self.result)

    def __unicode__(self, verbose=False):
        return self.__str__(verbose)


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
        improve sorting
        combine _generate_combos and build_dict to be more memory friendly -
        use "odometer" concept.
    """

    def __init__(self, dice, mod_op=MOD_OPERATORS['PLUS'], modifier=0):
        self._stats_dict = {}
        self._combinations = []
        self._combo_count = 0
        self._average = 0
        self._generate_combos(dice)
        self._build_dict(mod_op, modifier)
        self._calculate_average()

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
            row[0] = mod_op(sum(row[1:]), modifier)
            if row[0] not in self._stats_dict.keys():
                self._stats_dict[row[0]] = {'count': 1, 'chance': 0.0}
            else:
                self._stats_dict[row[0]]['count'] += 1
        for key in self._stats_dict:
            self._stats_dict[key]['chance'] = \
                self._stats_dict[key]['count'] / self._combo_count

    def _calculate_average(self):
        """ Calculate the average roll result for the dice_set and store it. """
        if not self._stats_dict:
            return
        total = 0
        for result in self._stats_dict:
            total += (result * self._stats_dict[result]['count'])
        average = total / self._combo_count
        #print('Average: {}'.format(average))
        self._average = average

    @property
    def combo_count(self):
        return self._combo_count

    @property
    def average(self):
        return self._average

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

    def __str__(self, verbose=False):
        """ Return a human-readable version of of the stats dictionary."""
        output = 'Roll-result average: {}'.format(self._average)
        if verbose:
            output += '\nDice combinations: {}\n'.format(self._combo_count)
            for key in self._stats_dict:
                output += ('{}: {} - {:.2%}\n'
                           .format(key,
                                   self._stats_dict[key]['count'],
                                   self._stats_dict[key]['chance']))
        return output

    def __unicode__(self, verbose=False):
        self.__str__(verbose)


class Diedometer(object):
    """ Holds a set of dice and can iterate through possible
    combinations of those dice in the same way an odometer iterates
    through all combinations of side of its dials.

    Attributes:
        _dice: a list of Die objects containing the dice assigned to the
        diedomoeter.
        _maximums: a list of the maximum values of each die assigned to the
        diedomoter.
        _meter: a list of integer values used to represent a set of die
        states (die 1 = 3, die 2 = 6, etc.).
        _dropped_dice_count: an integer representing the number of dice
        dropped out of the count when totalling the meter's current state.
        The die dropped will always be the die (or one of the dice) with the
        lowest value.

    To Do:
        minimums
        maximums and drop dice
    """

    def __init__(self, dice):
        self._dice = dice
        self._meter = []
        self._maximums = []
        self._dropped_dice_count = 0
        for die in self._dice:
            self._meter.append(1)
            self._maximums.append(die.sides)

    @property
    def finished(self):
        return self._meter == self._maximums

    @property
    def dice(self):
        return self._dice

    @property
    def dice_count(self):
        return len(self._meter)

    @property
    def meter(self):
        return self._meter

    @property
    def dropped_dice(self):
        return sorted(self._meter)[:self._dropped_dice_count]

    @property
    def dropped_dice_count(self):
        return self._dropped_dice_count

    def drop_die(self):
        """ Record that one more die should be dropped. """
        self._dropped_dice_count += 1

    def reset(self):
        """ Reset the diedometer back to the starting point. """
        self._meter = []
        for die in self._dice:
            self._meter.append(1)

    def increment(self):
        """ Increment the diedometer, rolling over digits and incrementing
        the one next to them as necessary. """
        if not self.finished:
            self._dropped_dice_count = 0
            rolled_over = True
            for i in reversed(range(0, self.dice_count)):
                if rolled_over:
                    if self._meter[i] == self._maximums[i]:
                        self._meter[i] = 1
                    else:
                        self._meter[i] += 1
                        rolled_over = False

    @property
    def result(self):
        """ Return the total value for the meter's current state, adjusting
        for any dropped dice. """
        sorted_dice = sorted(self._meter)
        total = 0
        for die in sorted_dice[self._dropped_dice_count:]:
            total += die
        return total






