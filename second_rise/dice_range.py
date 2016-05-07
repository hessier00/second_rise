import dice


class Range(object):
    """ Represents a dice-result range, constructed from modifiers and one or
    more d10.

    Attributes:
        _minimum: an integer representing the minimum possible result allowed
        by the range.
        _maximum: an integer representing the maximum possible result allowed
        by the range.  Maximum must be higher than minimum.
        _dice: a list containing the Die.D10 objects used to generate values
        within the range.

    To Do:
        Add result _future_, and undo/redo (future is what the current roll
        would become if you undo to a step back in _history.
        Add result probability table.
    """

    def __init__(self, minimum, maximum, dice_count=0):
        # Force maximum to be greater than minimum.
        if maximum <= minimum:
            maximum = minimum + 1
        # Set default dice value to be equal to the minimum.
        if dice_count == 0:
            dice_count = minimum
        self._minimum = minimum
        self._maximum = maximum
        self._dice = []
        for i in range(0, dice_count):
            self._dice.append(dice.D10())
        self._history = []

    @property
    def minimum(self):
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        self._minimum = minimum

    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        self._maximum = maximum

    @property
    def dice_count(self):
        """ Return the number of dice assigned to generate values within
        the range.
        """
        return len(self._dice)

    @dice_count.setter
    def dice_count(self, dice_count):
        """ Change the number of dice assigned to generate values within
        the range.
        """
        self._dice = []
        for i in range(1, dice_count):
            self._dice.append(dice.D10())

    @property
    def dice(self):
        return self._dice

    @property
    def rolled(self):
        """ Check to see if both dice have been rolled """
        answer = True
        for die in self._dice:
            if not die.rolled:
                answer = False
        return answer

    def roll(self):
        """ Rolls both d10 to generate a percentile score. """
        if self.rolled:
            self._history.append(self.result)
        for die in self._dice:
            die.roll()

    def dice_sort(self):
        """ Sort the dice in self._dice by value, placing the
        highest at [0].
        """
        sorted(self._dice, key=lambda die: die.result)

    def total(self, dice_to_exclude=0):
        total = 0
        for die in self._dice[dice_to_exclude:len(self._dice)]:
            total += die.result
        return total

    @property
    def result(self):
        """ Compute the result of a roll made 'against' the range. """
        dice_to_exclude = 0
        # Total the values of the rolled dice
        total = self.total(0)
        # If the total is greater than the maximum, iteratively exclude the
        # die with the lowest value until the total is not greater than the
        # maximum.
        while total > self._maximum:
            dice_to_exclude += 1
            total = self.total(dice_to_exclude)
        # If the total is _less_ than the minimum, but not zero,
        # set it to the  minimum
        if 0 < total <= self._minimum:
            total = self.minimum
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
        return 'range {}-{} (using {}d10): {}'.format(self.minimum,
                                                      self.maximum,
                                                      self.dice_count,
                                                      self.result)

    def __unicode__(self, verbose=False):
        return self.__str__(verbose)
