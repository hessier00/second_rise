import operator
import math
import dice


# Custom operator functions
def add_percent(base, mod):
    """ Modify the base value by adding a percentage of itself (the 'mod').
    So, if base is 55 and mod is 10, the goal is to add 10 percent of 55 to
    55, or 55+5.5=60.5.  Results are rounded up to the next integer if needed.
    """
    multiplier = mod * .01
    return math.ceil(base+(base*multiplier))


def sub_percent(base, mod):
    """ Modify the base value by subtracting a percentage of itself (the 'mod').
    So, if base is 55 and mod is 10, the goal is to subtract 10 percent of 35
    from 35, or 35-3.5=31.5.  Results are rounded up to the next integer if
    needed.
    """
    multiplier = mod * .01
    return math.ceil(base-(base*multiplier))

# Constants
OPERATOR_SIGNS = {operator.add: '+',
                  operator.sub: '-',
                  operator.mul:  '*',
                  operator.truediv: '/',
                  add_percent: '+',
                  sub_percent: '-'}

OPERATOR_SUFFIXES = {operator.add: '',
                     operator.sub: '',
                     operator.mul: '',
                     operator.truediv: '',
                     add_percent: '%',
                     sub_percent: '%'}

OPERATOR_PRECEDENCE = {operator.add: 1,
                       operator.sub: 2,
                       operator.mul: 5,
                       operator.truediv: 6,
                       add_percent: 3,
                       sub_percent: 4}


class Stat(object):
    """ Generates and stores one character stat.  Also manages and applies
    any assigned modifiers.

    Attributes:
        _name: a string containing the full name of the stat.
        _abbreviation: a string containing the abbreviation of the stat's name.
        _score: an integer representing the stat's base score
        _modifiers: a ModifierSet object containing all Modifiers assigned to
        the Stat.
    """
    def __init__(self, abbreviation, score, name = "", modifiers=None):
        self._abbreviation = abbreviation
        self._score = math.ceil(score)
        self._name = name
        if modifiers is None:
            self._modifiers = []
        else:
            self._modifiers = modifiers

    @property
    def abbreviation(self):
        """ Return the stat's abbreviated name. """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, new_abbrev):
        """ Set a new stat name abbreviation. """
        self._abbreviation = new_abbrev

    @property
    def name(self):
        """ Return the  stat's full name. """
        return self._name

    @name.setter
    def name(self, new_name):
        """ Set a new full name for the stat. """
        self._name = new_name

    @property
    def base_score(self):
        """ Return the stat's base score. """
        return self._score

    @base_score.setter
    def base_score(self, new_base):
        """ Set a new base score for the stat. """
        self._score = new_base

    @property
    def modifiers(self):
        """ Return the stat's set of modifiers. """
        return self._modifiers

    @property
    def score(self):
        """ Return the stat's modified score. """
        total = self.base_score
        for mod in self.modifiers:
            total = math.ceil(mod.operator(total, mod.operand))
        return total

    def __str__(self):
        """ Return a string representation of the stat and its adjusted
        score. """
        return '{}: {}'.format(self.abbreviation, self.score)

    def __unicode__(self):
        """ Return a unicode representation of the stat and its adjusted
        score. """
        return self.__str__()


class Modifier(object):
    """ Store a modifier operand and operator.

    Attributes:
        _operand: a number representing the modifier's operand.
        _operator: the operator function to use when applying the modifier's
        operand to the value being modified.  The default operator is plus.
    """
    def __init__(self,
                 source,
                 mod_operand,
                 mod_operator=dice.MOD_OPERATORS['+']):
        self._source = source
        if mod_operand < 0:
            raise ValueError
        self._operand = mod_operand
        self._operator = mod_operator

    @property
    def source(self):
        return self._source

    @property
    def operand(self):
        return self._operand

    @property
    def operator(self):
        return self._operator

    @property
    def sign(self):
        return OPERATOR_SIGNS[self.operator]

    @property
    def suffix(self):
        return OPERATOR_SUFFIXES[self.operator]

    def __str__(self):
        return '{}{}{}'.format(self.sign, self.operand, self.suffix)

    def __unicode__(self,):
        return self.__str__()


class ModifierSet(object):
    """ Store and manage a set of Modifier objects.

    Attributes:
        _modifiers: a list of Modifier objects

    To DO:
        remove modifiers from set
            -  by index
            - by source
    """
    def __init__(self, modifiers=None):
        if modifiers is None:
            self._modifiers = []
        else:
            self._modifiers = modifiers
        self._sort()

    @property
    def modifiers(self):
        return self._modifiers

    @property
    def modifier_count(self):
        return len(self._modifiers)

    def add_modifier(self, mod):
        """ Add a Modifier to the ModifierSet. """
        self._modifiers.append(mod)
        self._sort()

    def add_modifiers(self, mods):
        """ Add another ModifierSet's modifiers to the Modifier Set. """
        for modifier in mods.modifiers:
            self.add_modifier(modifier)
        self._sort()

    def __iter__(self):
        """ Return an iterator for the ModifierSet. """
        self._iteration_index = 0
        return self

    def __next__(self):
        """ Return the next modifier in the set. """
        self._iteration_index += 1
        if self._iteration_index <= self.modifier_count:
            return self.modifiers[self._iteration_index - 1]
        else:
            raise StopIteration

    @staticmethod
    def precedence(modifier):
        """ Return the sorting value of a Modifier.  Uses the base
        single-integer sorting value found in OPERATORS_PRECEDENCE, makes it
        in to a large number by multiplying by 100k, then subtracts the
        modifier operand from the total.  That means the highest-priority
        operation with the largest operand will get the lowest index number,
        while a modifier operand would have to be roughly 100k before it
        could cause the sort to be off.
        """
        precedence_value = OPERATOR_PRECEDENCE[modifier.operator] * 100000
        precedence_mod = modifier.operand
        return precedence_value - precedence_mod

    def _sort(self):
        """ Sort the Modifiers in the ModifierSet. """
        self._modifiers = sorted(self._modifiers, key=self.precedence)

    def __str__(self):
        output = ""
        for modifier in self._modifiers:
            output += modifier.__str__()
        return output

    def __unicode__(self):
        output = ""
        for modifier in self._modifiers:
            output += modifier.__unicode__()
        return output
