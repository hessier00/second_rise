import dice

print("Testing: dice")
test = dice.Die("b")
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