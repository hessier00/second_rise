import dice
import dice_range
import dice_set

print("Testing: dice")
test = dice.Die(0)
print('    test = dice.Die("b") - valid = {}'.format(test.valid))
test = dice.Die(1-5)
print('    test = dice.Die(1-5) - valid = {}'.format(test.valid))
test = dice.Die(15)
print('    test = dice.Die(15) - valid = {}'.format(test.valid))
print('    test = dice.Die(15) - sides: {}'.format(test.sides))
print('    test = dice.Die(15) - rolled: {}'.format(test.rolled))

print('    Rolling Die...')
test.roll()
print('        test = dice.Die(15) - rolled: {}'.format(test.rolled))
print('        test = dice.Die(15) - result: {}'.format(test.result))
print('    Creating and rolling a d10...')
test = dice.D10()
test.roll()
print('        test = dice.D10() - valid = {}'.format(test.valid))
print('        test = dice.D10() - sides: {}'.format(test.sides))
print('        test = dice.D10() - result: {}'.format(test.result))

print('    Creating and rolling a d5...')
test = dice.D5()
test.roll()
print('        test = dice.D5() - valid = {}'.format(test.valid))
print('        test = dice.D5() - sides: {}'.format(test.sides))
print('        test = dice.D5() - result: {}'.format(test.result))

print('    Creating and rolling a d2...')
test = dice.D2()
test.roll()
print('        test = dice.D2() - valid = {}'.format(test.valid))
print('        test = dice.D2() - sides: {}'.format(test.sides))
print('        test = dice.D2() - result: {}'.format(test.result))

print('    Creating and rolling a d100...')
test = dice.D100()
test.roll()
print('        test = dice.D100() - valid = {}'.format(test.valid))
print('        test = dice.D100() - sides: {}'.format(test.sides))
print('        test = dice.D100() - result: {}'.format(test.result))

print('    Testing a percentile dice...')
test = dice.Percentile()
print('        Created but not rolled...')
print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
print('            test = dice.Percentile() - valid = {}'.format(test.valid))
print('            test = dice.Percentile() - sides: {}'.format(test.sides))
print('            test = dice.Percentile() - result: {}'.format(test.result))
print('            test = dice.Percentile() - minimum: {}'.format(test.minimum))
test.roll()

print('        After rolling...')
print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
print('            test = dice.Percentile() - result: {}'.format(test.result))
print('            test = dice.Percentile() - minimum: {}'.format(test.minimum))

print('        Individual dice...')
print('            tens (test.tens.result) - {}'.format(test.tens.result))
print('            ones (test.ones.result) - {}'.format(test.ones.result))

print('        Changing minimum to zero...')
test = dice.Percentile(0)
print('        Created but not rolled...')
print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
print('            test = dice.Percentile() - valid = {}'.format(test.valid))
print('            test = dice.Percentile() - sides: {}'.format(test.sides))
print('            test = dice.Percentile() - result: {}'.format(test.result))
print('            test = dice.Percentile() - minimum: {}'.format(test.minimum))
test.roll()

print('        After rolling...')
print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
print('            test = dice.Percentile() - result: {}'.format(test.result))
print('            test = dice.Percentile() - minimum: {}'.format(test.minimum))

print('        Individual dice...')
print('            tens (test.tens.result) - {}'.format(test.tens.result))
print('            ones (test.ones.result) - {}'.format(test.ones.result))

print('    Testing a d1000 percentile-style dice...')
test = dice.D1000()
print('        Created but not rolled...')
print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
print('            test = dice.Percentile() - valid = {}'.format(test.valid))
print('            test = dice.Percentile() - sides: {}'.format(test.sides))
print('            test = dice.Percentile() - result: {}'.format(test.result))
print('            test = dice.Percentile() - minimum: {}'.format(test.minimum))
test.roll()

print('        After rolling...')
print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
print('            test = dice.Percentile() - result: {}'.format(test.result))
print('            test = dice.Percentile() - minimum: {}'.format(test.minimum))

print('        Changing minimum to zero...')
test = dice.D1000()
print('        Created but not rolled...')
print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
print('            test = dice.Percentile() - valid = {}'.format(test.valid))
print('            test = dice.Percentile() - sides: {}'.format(test.sides))
print('            test = dice.Percentile() - result: {}'.format(test.result))
print('            test = dice.Percentile() - minimum: {}'.format(test.minimum))
test.roll()

print('        After rolling...')
print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
print('            test = dice.Percentile() - result: {}'.format(test.result))
print('            test = dice.Percentile() - minimum: {}'.format(test.minimum))

print('        Individual dice...')
print('            hundreds (test.hundreds.result) - {}'
      .format(test.hundreds.result))
print('            tens (test.tens.result) - {}'.format(test.tens.result))
print('            ones (test.ones.result) - {}'.format(test.ones.result))

print('    Testing a d10000 percentile-style dice...')
test = dice.D10000()
print('        Created but not rolled...')
print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
print('            test = dice.Percentile() - valid = {}'.format(test.valid))
print('            test = dice.Percentile() - sides: {}'.format(test.sides))
print('            test = dice.Percentile() - result: {}'.format(test.result))
print('            test = dice.Percentile() - minimum: {}'.format(test.minimum))
test.roll()

print('        After rolling...')
print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
print('            test = dice.Percentile() - result: {}'.format(test.result))
print('            test = dice.Percentile() - minimum: {}'.format(test.minimum))

print('        Changing minimum to zero...')
test = dice.D10000()
print('        Created but not rolled...')
print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
print('            test = dice.Percentile() - valid = {}'.format(test.valid))
print('            test = dice.Percentile() - sides: {}'.format(test.sides))
print('            test = dice.Percentile() - result: {}'.format(test.result))
print('            test = dice.Percentile() - minimum: {}'.format(test.minimum))
test.roll()

print('        After rolling...')
print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
print('            test = dice.Percentile() - result: {}'.format(test.result))
print('            test = dice.Percentile() - minimum: {}'.format(test.minimum))

print('        Individual dice...')
print('            thousands (test.thousands.result) - {}'
      .format(test.thousands.result))
print('            hundreds (test.hundreds.result) - {}'
      .format(test.hundreds.result))
print('            tens (test.tens.result) - {}'.format(test.tens.result))
print('            ones (test.ones.result) - {}'.format(test.ones.result))


print('Testing: range')
test = dice_range.Range(2, 20)
print('    Created but not rolled...')
print('        test = dice_range.Range(2, 20) - rolled: {}'.format(test.rolled))
print('        test = dice_range.Range(2, 20) - result: {}'.format(test.result))
print('        test = dice_range.Range(2, 20) - dice count: {}'
      .format(test.dice_count))
test.roll()

print('    Rolled...')
print('        test = dice_range.Range(2, 20) - rolled: {}'.format(test.rolled))
print('        test = dice_range.Range(2, 20) - result: {}'.format(test.result))
print('        test = dice_range.Range(2, 20) - dice count: {}'
      .format(test.dice_count))
count = 1
for die in test.dice:
    print('        test = dice_range.Range(2,20) - die {}: {}'
          .format(count, die.result))
    count += 1

test = dice_range.Range(4, 27)
print('    Creating a range with more dice but a low max, not yet rolled...')
print('        test = dice_range.Range(4, 27) - rolled: {}'.format(test.rolled))
print('        test = dice_range.Range(4, 27) - result: {}'.format(test.result))
print('        test = dice_range.Range(4, 27) - dice count: {}'
      .format(test.dice_count))
test.roll()
print('    Rolled...')
print('        test = dice_range.Range(4, 27) - rolled: {}'.format(test.rolled))
print('        test = dice_range.Range(4, 27) - result: {}'.format(test.result))
print('        test = dice_range.Range(4, 27) - dice count: {}'
      .format(test.dice_count))
count = 1
for die in test.dice:
    print('        test = dice_range.Range(4, 27) - die {}: {}'
          .format(count, die.result))
    count += 1

test = dice_range.Range(12, 18, 2)
print('    Creating a range with a minimum higher than the dice count, '
      'not yet rolled...')
print('        test = dice_range.Range(12, 18, 2) - rolled: {}'.format(test.rolled))
print('        test = dice_range.Range(12, 18, 2) - result: {}'.format(test.result))
print('        test = dice_range.Range(12, 18, 2) - dice count: {}'
      .format(test.dice_count))
test.roll()
print('    Rolled...')
print('        test = dice_range.Range(12, 18, 2) - rolled: {}'.format(test.rolled))
print('        test = dice_range.Range(12, 18, 2) - result: {}'.format(test.result))
print('        test = dice_range.Range(12, 18, 2) - dice count: {}'
      .format(test.dice_count))
count = 1
for die in test.dice:
    print('        test = dice_range.Range(12, 18, 2) - die {}: {}'
          .format(count, die.result))
    count += 1

test = dice_range.Range(1, 6)
print('    Creating a range with a low maximum and a single die, '
      'not yet rolled...')
print('        test = dice_range.Range(1, 6) - rolled: {}'.format(test.rolled))
print('        test = dice_range.Range(1, 6) - result: {}'.format(test.result))
print('        test = dice_range.Range(1, 6) - dice count: {}'
      .format(test.dice_count))
test.roll()
print('    Rolled...')
print('        test = dice_range.Range(1, 6) - rolled: {}'.format(test.rolled))
print('        test = dice_range.Range(1, 6) - result: {}'.format(test.result))
print('        test = dice_range.Range(1, 6) - dice count: {}'
      .format(test.dice_count))
count = 1
for die in test.dice:
    print('        test = dice_range.Range(1, 6) - die {}: {}'
          .format(count, die.result))
    count += 1

print('Testing dice_set...')
test = dice_set.DiceSet()
print('    Created but no dice added...')
print('        test = dice_set.DiceSet() - rolled: {}'.format(test.rolled))
print('        test = dice_set.DiceSet() - valid = {}'.format(test.valid))
print('        test = dice_set.DiceSet() - result: {}'.format(test.result))
print('        test = dice_set.DiceSet() - dice count: {}'
      .format(test.dice_count))
test.add_die(dice.D10())
test.add_die(dice.D10())
test.add_die(dice.D10())
test.add_die(dice.D5())
test.add_die(dice.D5())
test.add_die(dice.D2())
print('    3d10, 2d5, 1d2 added, but not rolled...')
print('        Rolled: {}'.format(test.rolled))
print('        Valid = {}'.format(test.valid))
print('        Result: {}'.format(test.result))
print('        Dice count: {}'.format(test.dice_count))
count = 1
for die in test.dice:
    print('        Die {} ({}-sider): {}'
          .format(count, die.sides, die.result))
    count += 1
test.roll()
print('    Rolled...')
print('        Rolled: {}'.format(test.rolled))
print('        Valid = {}'.format(test.valid))
print('        Result: {}'.format(test.result))
print('        Dice count: {}'.format(test.dice_count))
count = 1
for die in test.dice:
    print('        Die {} ({}-sider): {}'
          .format(count, die.sides, die.result))
    count += 1
test.build_stats()
print('    A smaller dice set (2d10)...')
test = dice_set.DiceSet()
test.add_die(dice.D10())
test.add_die(dice.D10())
test.roll()
print('        Rolled: {}'.format(test.rolled))
print('        Valid = {}'.format(test.valid))
print('        Result: {}'.format(test.result))
print('        Dice count: {}'.format(test.dice_count))
count = 1
for die in test.dice:
    print('        Die {} ({}-sider): {}'
          .format(count, die.sides, die.result))
    count += 1
test.build_stats()
print('    Classic D&D dice (3d6)...')
test = dice_set.DiceSet()
test.add_die(dice.Die(6))
test.add_die(dice.Die(6))
test.add_die(dice.Die(6))
test.roll()
print('        Rolled: {}'.format(test.rolled))
print('        Valid = {}'.format(test.valid))
print('        Result: {}'.format(test.result))
print('        Dice count: {}'.format(test.dice_count))
count = 1
for die in test.dice:
    print('        Die {} ({}-sider): {}'
          .format(count, die.sides, die.result))
    count += 1
test.build_stats()
print(test.stats.chance_of(12))
print('    A modified dice set (2d10+5)...')
test = dice_set.DiceSet()
test.add_die(dice.D10())
test.add_die(dice.D10())
test.modifier = 5
test.modifier_operation = dice_set.MOD_OPERATORS['PLUS']
test.roll()
print('        Rolled: {}'.format(test.rolled))
print('        Valid = {}'.format(test.valid))
print('        Result: {}'.format(test.result))
print('        Dice count: {}'.format(test.dice_count))
count = 1
for die in test.dice:
    print('        Die {} ({}-sider): {}'
          .format(count, die.sides, die.result))
    count += 1
test.build_stats()
print('    A weird modified dice set (3d7*3)...')
test = dice_set.DiceSet()
test.add_die(dice.Die(7))
test.add_die(dice.Die(7))
test.add_die(dice.Die(7))
test.modifier = 3
test.modifier_operation = dice_set.MOD_OPERATORS['*']
test.roll()
print('        Rolled: {}'.format(test.rolled))
print('        Valid = {}'.format(test.valid))
print('        Result: {}'.format(test.result))
print('        Dice count: {}'.format(test.dice_count))
count = 1
for die in test.dice:
    print('        Die {} ({}-sider): {}'
          .format(count, die.sides, die.result))
    count += 1
test.build_stats()

print('Testing dice history...')
test=dice.D10()
print('    d10 rolled 5 times')
for i in range(1, 6):
    test.roll()
print('        result: {}'.format(test.result))
print('        history: {}'.format(test.history))
print('        d10 __str__: {}'.format(test))
print('        verbose: {}'.format(test.__str__(True)))
test=dice.D10000()
print('    d10000 rolled 5 times')
for i in range(1, 6):
    test.roll()
print('        result: {}'.format(test.result))
print('        history: {}'.format(test.history))
print('        d10000 __str__: {}'.format(test))
print('        verbose: {}'.format(test.__str__(True)))
print('    Clearing history...')
test.clear_history()
print('        history: {}'.format(test.history))
