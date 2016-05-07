import random


class Die(object):
    """ Represents a die.  The die is '.roll()'ed to determine a random value

    Attributes:
        _sides: an integer representing the number of sides on the die.
        _result: an integer representing the last rolled value of the die.

    To Do:
        Add result _future_, and undo/redo (future is what the current roll
        would become if you undo to a step back in _history.
    """
    def __init__(self, sides):
        """ Build a new die.  Ignore all 'sides' argument values other than but
        positive integers.  For invalid 'sides' arguments, set the side count to
        0, to represent an error/misconfiguration state.

        Arguments:
            sides (int): the number of sides on the die.
        """
        self._sides = 0
        self._result = 0
        if sides > 0:
            self._sides = sides
        self._history = []

    @property
    def valid(self):
        """ Check whether the die has a valid number of sides. """
        return self._sides != 0

    @property
    def rolled(self):
        """ Check whether the die has been rolled. """
        return self._result != 0

    @property
    def sides(self):
        """ Get the die's number of sides. """
        return self._sides

    @property
    def result(self):
        """ Get the die's last rolled result. """
        return self._result

    def roll(self):
        """ 'Roll' the dice and store the result. move any previous results
        to the die's history.
        """
        if self.rolled:
            self._history.append(self.result)
        self._result = random.randint(1, self._sides)

    @property
    def history(self):
        return self._history

    def clear_history(self):
        """ Clears the die' roll history. """
        self._history = []

    def __str__(self, verbose=False):
        """ Return either the die value as a string (terse) or a more
        detailed response (verbose).

        Arguments:
            verbose: a boolean value representing whether or not the return
            value should be verbose.
        """
        if not verbose:
            return str(self._result)
        return 'd{}: {}'.format(self._sides, self._result)

    def __unicode__(self, verbose=False):
        return self.__str__(verbose)


class D10(Die):
    """ Convenience sub-class of Die, creates a 10-sider.
    Results range is 1-10.
    """
    def __init__(self):
        Die.__init__(self, 10)


class D5(Die):
    """ Convenience sub-class of Die, creates a 5-sider.
    Results range is 1-5.
    """
    def __init__(self):
        Die.__init__(self, 5)


class D2(Die):
    """ Convenience sub-class of Die, creates a 2-sider.
    Results range is 1-2.
    """
    def __init__(self):
        Die.__init__(self, 2)


class D100(Die):
    """ Convenience sub-class of Die, creates a 100-sider.
    Results range is 1-100.  This is _not_ a percentile dice.
    """
    def __init__(self):
        Die.__init__(self, 100)


class Percentile(object):
    """ A compound dice construct, using two D10 objects to generate a range
    of results from either 0-99 or 1-100, using one die as the tens digit and
    one die as the ones digit.

    Attributes:
        _minimum: an integer representing the the minimum value of a roll -
        either 1 or 0.
        _dice: a list holding the individual Die objects that comprise the
        compound dice construct.

    To Do:
        Add result _future_, and undo/redo (future is what the current roll
        would become if you undo to a step back in _history.
    """
    def __init__(self, minimum=1):
        # Minimum can only be 0 or 1.  Some systems use percentile dice to
        # represent 0-99 instead of 1-100.  Using minimum = 0 allows the
        # alternate use.
        if minimum != 0:
            minimum = 1
        self._minimum = minimum
        self._dice = []
        self._dice.append(D10())
        self._dice.append(D10())
        self._history = []

    def roll(self):
        """ Rolls both d10 to generate a percentile score. """
        if self.rolled:
            self._history.append(self.result)
        for die in self._dice:
            die.roll()

    @property
    def rolled(self):
        """ Check to see if both dice have been rolled """
        answer = True
        for die in self._dice:
            if not die.rolled:
                answer = False
        return answer

    @property
    def valid(self):
        """ Check to ensure that both dice have a valid number of sides. """
        answer = True
        for die in self._dice:
            if not die.valid:
                answer = False
        return answer

    @property
    def sides(self):
        """ Return the number of sides represented by the compound dice
        construct. """
        sides = 1
        for die in self._dice:
            sides = sides * die.sides
        return sides

    @property
    def tens(self):
        """ Return the d10 used for the tens-digit. """
        return self._dice[1]

    @property
    def ones(self):
        """ Return the d10 used to represent the ones-digit. """
        return self._dice[0]

    @property
    def minimum(self):
        """ Return the "minimum" setting - 0 or 1. """
        return self._minimum

    @minimum.setter
    def minimum(self, new_minimum):
        """ Set a new minimum value for the percentile dice.  1 or 0 only. """
        if new_minimum != 0:
            new_minimum = 1
        self._minimum = new_minimum

    @property
    def result(self):
        """ Return the percentile pair's rolled result. """
        if not self.rolled:
            return 0
        # Check if an all 10s result was rolled.  On physical dice,
        # that would correspond to an all-zeros roll, which is either a maximum
        # or minimum roll, depending on whether the minimum roll is 0 or 1.
        maximum = True
        multiplier = 1
        total = 0
        for die in self._dice:
            # Check for a maximum value
            # If the individual die is _not_ a max, than the total can't be
            # either.  However, if it _is_, treat the dice as a zero value
            # for its digit.  <8> and <10> should represent an 80, not a 90.
            die_value = die.result
            if die_value != die.sides:
                maximum = False
            else:
                die_value = 0
            # Add the die to the overall total, adjusting for digit represented
            total += die_value * multiplier
            # Adjust the multiplier to represent the next digit
            multiplier *= 10
        if maximum:
            if self._minimum == 0:
                return 0
            else:
                return self.sides
        else:
            return total

    @property
    def history(self):
            return self._history

    def clear_history(self):
        """ Clears the die's roll history. """
        self._history = []

    def __str__(self, verbose=False):
        """ Return either the die value as a string (terse) or a more
        detailed response (verbose).

        Arguments:
            verbose: a boolean value representing whether or not the return
            value should be verbose.
        """
        if not verbose:
            return str(self.result)
        side_count = 1
        for die in self._dice:
            side_count *= die.sides
        return 'd{}: {}'.format(side_count, self.result)

    def __unicode__(self, verbose=False):
        return self.__str__(verbose)


class D1000(Percentile):
    """ A compound dice for generating 0-999 or 1-1000 using three d10."""
    def __init__(self):
        Percentile.__init__(self)
        self._dice.append(D10())

    @property
    def hundreds(self):
        """ Return the d10 used for the hundreds-digit. """
        return self._dice[2]


class D10000(D1000):
    """ A compound dice for generating 0-9999 or 1-10000 using four d10."""
    def __init__(self):
        D1000.__init__(self)
        self._dice.append(D10())

    @property
    def thousands(self):
        """ Return the d10 used for the hundreds-digit. """
        return self._dice[3]
