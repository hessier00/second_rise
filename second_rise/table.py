import dice

"""
Class To-Do:
    Tables and table rows with modifiers as well as results.  Modifier sets?

"""


class Table(object):
    """ Hold a table of dice-roll results and indicate the appropriate die to
    use when generating results form the table.

    Attributes:
        _entries: a list of TableRow items, representing the table's content
        rows.
        _minimum: an integer representing the lowest roll result with a
        matching table outcome.
        _maximum: an integer representing the highest roll result with a
        matching table outcome.
        _generator: a Generator object used to randomly produce results from
        the table.
        _name: a string representing the human-readable name of the table.
        _result: a TableRow object, representing the most recent result
        rolled on the Table.
        _history: a list of TableRow object, representing the history of
        rolls made on the Table.  Can be combined with _generator's history
        to recreate the history of both roll values and corresponding results.

    To Do:
        + Add result _future_, and undo/redo (future is what the current result
        would become if you undo to a step back in _history.
    """
    def __init__(self, entries, generator=None, name=None):
        self._entries = entries
        self._sort()
        self._minimum = self._entries[0].minimum
        self._maximum = self._entries[-1].maximum
        if generator is None:
            self._generator = dice.Die(self._maximum - self._minimum + 1)
        else:
            self._generator = generator
        if name is None:
            self._name = 'Unnamed Table'
        else:
            self._name = name
        self._result = None
        self._history = []

    @property
    def minimum(self):
        """ Return the lowest possible dice result that corresponds to a
        result in the table.
        """
        return self._minimum

    @property
    def maximum(self):
        """ Return the highest possible dice result that corresponds to a
            result in the table.
        """
        return self._maximum

    @property
    def generator(self):
        """ Return the generator (Die/DiceSet/Range, etc.) used to generate
        results on the table.
        """
        return self._generator

    @property
    def name(self):
        """ Return the table's name. """
        return self._name

    @property
    def valid(self):
        """ Verify whether or not the minimums and maximums for each row form
        a contiguous set of ranges.  A table is not valid if a roll result
        could fall in between the result ranges of two neighboring rows.
        """
        for i in range(1, len(self._entries)):
            if self._entries[i].minimum != self._entries[i-1].maximum + 1:
                return False
        return True

    @property
    def result(self):
        """ Return the most recent result rolled on the Table. """
        return self._result.result

    @property
    def result_row(self):
        """ Return the TableRow object containing most recent result rolled
        on the Table.
        """
        return self._result

    def _sort(self):
        """ Sort the table by the roll-result necessary to generate a result,
        lowest to highest.
        """
        self._entries = sorted(self._entries, key=lambda entry: entry.minimum)

    def roll(self):
        """ Generate a result from the table. """
        if self._result:
            self._history.append(self._result)
        self.generator.roll()
        for row in self._entries:
            if row.minimum <= self.generator.result <= row.maximum:
                self._result = row

    @property
    def history(self):
        """ Return the table's result history. """
        return self._history

    def clear_history(self):
        """ Clear the table's result history. To maintain synchronization,
        the table's generator's history is also cleared.
        """
        self._history = []
        self._generator.clear_history()

    def __str__(self, digits=0):
        left_col = (digits * 2) + 6
        output = '{}\n'.format(self.name)
        output += '{:<{}}Result\n'.format('Roll', left_col)
        for row in self._entries:
            output += row.__str__(digits)+'\n'
        return output

    def __unicode__(self, digits=0):
        return self.__str__(digits)


class TableRow(object):
    """ Hold one row of a table: the minimum and maximum roll that indicate
    this row, and the associated result.
    """
    def __init__(self, minimum, maximum, result):
        self._minimum = minimum
        self._maximum = maximum
        self._result = result

    @property
    def minimum(self):
        return self._minimum

    @property
    def maximum(self):
        return self._maximum

    @property
    def result(self):
        return self._result

    def __str__(self, digits=0):
        left_col = (digits * 2) + 6
        return "{:<{}}{}".format('{0:0{2}}-{1:0{2}}'.format(self.minimum,
                                                            self.maximum,
                                                            digits),
                                 left_col,
                                 self.result)

    def __unicode__(self):
        return self.__str__()


# Table Constants

# Primary Attribute Table
table_rows = [TableRow(1, 1, 1),
              TableRow(2, 3, 2),
              TableRow(4, 7, 3),
              TableRow(8, 14, 4),
              TableRow(15, 25, 5),
              TableRow(26, 41, 6),
              TableRow(42, 59, 7),
              TableRow(60, 79, 8),
              TableRow(80, 101, 9),
              TableRow(102, 126, 10),
              TableRow(127, 153, 11),
              TableRow(154, 182, 12),
              TableRow(183, 215, 13),
              TableRow(216, 251, 14),
              TableRow(252, 291, 15),
              TableRow(292, 334, 16),
              TableRow(335, 381, 17),
              TableRow(382, 432, 18),
              TableRow(433, 488, 19),
              TableRow(489, 548, 20),
              TableRow(549, 612, 21),
              TableRow(613, 682, 22),
              TableRow(683, 757, 23),
              TableRow(758, 837, 24),
              TableRow(838, 923, 25),
              TableRow(924, 1014, 26),
              TableRow(1015, 1112, 27),
              TableRow(1113, 1215, 28),
              TableRow(1216, 1324, 29),
              TableRow(1325, 1439, 30),
              TableRow(1440, 1560, 31),
              TableRow(1561, 1687, 32),
              TableRow(1688, 1820, 33),
              TableRow(1821, 1959, 34),
              TableRow(1960, 2103, 35),
              TableRow(2104, 2254, 36),
              TableRow(2255, 2410, 37),
              TableRow(2411, 2571, 38),
              TableRow(2572, 2738, 39),
              TableRow(2739, 2909, 40),
              TableRow(2910, 3085, 41),
              TableRow(3086, 3266, 42),
              TableRow(3267, 3450, 43),
              TableRow(3451, 3637, 44),
              TableRow(3638, 3847, 45),
              TableRow(3848, 4080, 46),
              TableRow(4081, 4316, 47),
              TableRow(4317, 4563, 48),
              TableRow(4564, 4826, 49),
              TableRow(4827, 5175, 50),
              TableRow(5176, 5438, 51),
              TableRow(5439, 5684, 52),
              TableRow(5685, 5921, 53),
              TableRow(5922, 6153, 54),
              TableRow(6154, 6363, 55),
              TableRow(6364, 6551, 56),
              TableRow(6552, 6735, 57),
              TableRow(6736, 6915, 58),
              TableRow(6916, 7091, 59),
              TableRow(7092, 7262, 60),
              TableRow(7263, 7429, 61),
              TableRow(7430, 7591, 62),
              TableRow(7592, 7747, 63),
              TableRow(7748, 7897, 64),
              TableRow(7898, 8042, 65),
              TableRow(8043, 8181, 66),
              TableRow(8182, 8314, 67),
              TableRow(8315, 8441, 68),
              TableRow(8442, 8562, 69),
              TableRow(8563, 8677, 70),
              TableRow(8678, 8786, 71),
              TableRow(8787, 8889, 72),
              TableRow(8890, 8986, 73),
              TableRow(8987, 9078, 74),
              TableRow(9079, 9163, 75),
              TableRow(9164, 9243, 76),
              TableRow(9244, 9318, 77),
              TableRow(9319, 9388, 78),
              TableRow(9389, 9453, 79),
              TableRow(9454, 9513, 80),
              TableRow(9514, 9568, 81),
              TableRow(9569, 9619, 82),
              TableRow(9620, 9666, 83),
              TableRow(9667, 9710, 84),
              TableRow(9711, 9749, 85),
              TableRow(9750, 9785, 86),
              TableRow(9786, 9818, 87),
              TableRow(9819, 9848, 88),
              TableRow(9849, 9875, 89),
              TableRow(9876, 9899, 90),
              TableRow(9900, 9921, 91),
              TableRow(9922, 9941, 92),
              TableRow(9942, 9959, 93),
              TableRow(9960, 9975, 94),
              TableRow(9976, 9986, 95),
              TableRow(9987, 9993, 96),
              TableRow(9994, 9997, 97),
              TableRow(9998, 9999, 98),
              TableRow(10000, 10000, 99)]
primary_attribute_table = Table(table_rows,
                                dice.D10000(),
                                'Primary Attribute Table')
