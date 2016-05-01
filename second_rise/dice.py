import random

class Die(object):
    """ Represents a die.  The die is '.roll()'ed to determine a random value

    Attributes:
        sides: an integer representing the number of sides on the die.
        result: an integer representing the last rolled value of the die.

    To Do:
        Add result history.
    """
    _sides = 0
    _result = 0

    def __init__(self, sides):
        """ Build a new die.  Ignore all 'sides' argument values other than but
        positive integers.  For invalid 'sides' arguments, set the side count to
        0, to represent an error/misconfiguration state.

        Arguments:
            sides (int): the number of sides on the die.
        """
        if isinstance(sides, int):
            if sides > 0:
                self._sides = sides

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
        """ 'Roll' the dice and store the result. """
        self._result = random.randint(1,self._sides)


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
    """
    def __init__(self, minimum=1):
        # Minimum can only be 0 or 1.  Some systems use percentile dice to
        # represent 0-99 instead of 1-100.  Using minimum = 0 allows the
        # alternate use.
        if minimum != 0:
            minimum = 1
        self._minimum=minimum
        self._dice = []
        self._dice[0] = D10()
        self._dice[1] = D10()

    def roll(self):
        """ Rolls both d10 to generate a percentile score. """
        for die in self._dice:
            die.roll()

    @property
    def rolled(self):
        """ Check to see if both dice have been rolled """
        answer = True
        for die in self._dice:
            if not die.roller:
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
        max = True
        multiplier = 1
        total = 0
        for die in self._dice:
            # Check for a maximum value
            if die.result != die.sides:
                max == False
            # Add the die to the overall total, adjusting for digit represented
            total += die.result * multiplier
            # Adjust the multiplier to represent the next digit
            multiplier *= 10
        if max and self._minimum == 0:
            return 0
        else:
            return total

 # class D1000(Percentile):
#     """ A compound dice for generating 0-999 or 1-1000 using three d10."""
#     def __init__(self):
#         Percentile.__init__(self)
#         self._hundreds = D10()
#










