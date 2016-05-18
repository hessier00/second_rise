import unittest
import dice


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


class OperatorTestCase(unittest.TestCase):
    def test_operators(self):
        self.assertEqual(dice.MOD_OPERATORS['+'](25, 38), 63,
                         'Addition function failed.')
        self.assertEqual(dice.MOD_OPERATORS['PLUS'](-5, 13), 8,
                         'Addition function failed.')
        self.assertEquals(dice.MOD_OPERATORS['-'](22, 17), 5,
                          'Subtraction function failed.')
        self.assertEquals(dice.MOD_OPERATORS['MINUS'](-5, 13), -18,
                          'Subtraction function failed.')
        self.assertEquals(dice.MOD_OPERATORS['*'](3, 3), 9,
                          'Multiplication function failed.')
        self.assertEquals(dice.MOD_OPERATORS['MULTIPLIED_BY'](-2, -15), 30,
                          'Multiplication function failed.')
        self.assertEquals(dice.MOD_OPERATORS['/'](3, 3), 1,
                          'Division function failed.')
        self.assertEquals(dice.MOD_OPERATORS['DIVIDED_BY'](-12, -3), 4,
                          'Division function failed.')

if __name__ == '__main__':
    unittest.main()
