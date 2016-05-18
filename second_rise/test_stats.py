import unittest
import stats
import dice


class OperatorTestCase(unittest.TestCase):
    def test_operators(self):
        self.assertEqual(stats.add_percent(55, 10), 61,
                         'Add percentage function failed.')
        self.assertEqual(stats.sub_percent(65, 15), 56,
                         'Subtract percentage function failed.')


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        source = "Place-holder"
        self.mod_default = stats.Modifier(source, 5)
        self.mod_add = stats.Modifier(source, 15, dice.MOD_OPERATORS['+'])
        self.mod_sub = stats.Modifier(source, 7, dice.MOD_OPERATORS['-'])
        self.mod_mult = stats.Modifier(source, 1.2, dice.MOD_OPERATORS['*'])
        self.mod_div = stats.Modifier(source, 1.1, dice.MOD_OPERATORS['/'])
        self.mod_add_perc = stats.Modifier(source, 10, stats.add_percent)
        self.mod_sub_perc = stats.Modifier(source, 15, stats.sub_percent)
        self.mod_set = stats.ModifierSet(modifiers = [self.mod_default,
                                                      self.mod_add,
                                                      self.mod_sub,
                                                      self.mod_mult,
                                                      self.mod_div,
                                                      self.mod_add_perc,
                                                      self.mod_sub_perc])

    def tearDown(self):
        for mod in self.mod_set.modifiers:
            mod = []
        self.mod_set = {}


class ModifierTestCase(BaseTestCase):
    def test_modifier(self):
        mods = [[self.mod_default, 5, dice.MOD_OPERATORS['+'], '+', '','+5'],
                   [self.mod_add, 15, dice.MOD_OPERATORS['+'], '+', '', '+15'],
                   [self.mod_sub, 7, dice.MOD_OPERATORS['-'], '-', '', '-7'],
                   [self.mod_mult, 1.2,
                    dice.MOD_OPERATORS['*'], '*', '', '*1.2'],
                   [self.mod_div, 1.1,
                    dice.MOD_OPERATORS['/'], '/', '', '/1.1'],
                   [self.mod_add_perc, 10, stats.add_percent, '+', '%', '+10%'],
                   [self.mod_sub_perc, 15, stats.sub_percent, '-', '%', '-15%']]
        for mod in mods:
            self.assertEqual(mod[0].operand, mod[1], 'Assigning operand failed')
            self.assertEqual(mod[0].operator, mod[2],
                             'Assigning {} operator failed'.format(mod[3]))
            self.assertEquals(mod[0].sign, mod[3],
                              'Returned incorrect operation "sign", expected '
                              '{}'.format(mod[3]))
            self.assertEquals(mod[0].suffix, mod[4],
                              'Returned incorrect modifier suffix, '
                              'expected {}.'.format(mod[4]))
            self.assertEquals(mod[0].__str__(), mod[5],
                              'Returned incorrect __str__ description, '
                              'expected {}.'.format(mod[5]))
            self.assertEquals(mod[0].__unicode__(), mod[5],
                              'Returned incorrect __unicode__ description, '
                              'expected {}'.format(mod[5]))


class ModifierSetTestCase(BaseTestCase):
    def test_modifier_set(self):
        empty_set = stats.ModifierSet()
        self.assertEquals(empty_set.modifiers, [],
                          'Modifier Set with no Modifiers assigned is not '
                          'empty.')
        self.assertEquals(empty_set.modifier_count, 0,
                         'Modifier Set with no Modifiers assigned has length '
                         '> 0.')



if __name__ == '__main__':
    unittest.main()
