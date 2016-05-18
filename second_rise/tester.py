import dice
import stats
#
#
# print("Testing: dice")
# test = dice.Die(0)
# print('    test = dice.Die("b") - valid = {}'.format(test.valid))
# test = dice.Die(1-5)
# print('    test = dice.Die(1-5) - valid = {}'.format(test.valid))
# test = dice.Die(15)
# print('    test = dice.Die(15) - valid = {}'.format(test.valid))
# print('    test = dice.Die(15) - sides: {}'.format(test.sides))
# print('    test = dice.Die(15) - rolled: {}'.format(test.rolled))
#
# print('    Rolling Die...')
# test.roll()
# print('        test = dice.Die(15) - rolled: {}'.format(test.rolled))
# print('        test = dice.Die(15) - result: {}'.format(test.result))
# print('    Creating and rolling a d10...')
# test = dice.D10()
# test.roll()
# print('        test = dice.D10() - valid = {}'.format(test.valid))
# print('        test = dice.D10() - sides: {}'.format(test.sides))
# print('        test = dice.D10() - result: {}'.format(test.result))
#
# print('    Creating and rolling a d5...')
# test = dice.D5()
# test.roll()
# print('        test = dice.D5() - valid = {}'.format(test.valid))
# print('        test = dice.D5() - sides: {}'.format(test.sides))
# print('        test = dice.D5() - result: {}'.format(test.result))
#
# print('    Creating and rolling a d2...')
# test = dice.D2()
# test.roll()
# print('        test = dice.D2() - valid = {}'.format(test.valid))
# print('        test = dice.D2() - sides: {}'.format(test.sides))
# print('        test = dice.D2() - result: {}'.format(test.result))
#
# print('    Creating and rolling a d100...')
# test = dice.D100()
# test.roll()
# print('        test = dice.D100() - valid = {}'.format(test.valid))
# print('        test = dice.D100() - sides: {}'.format(test.sides))
# print('        test = dice.D100() - result: {}'.format(test.result))
#
# print('    Testing a percentile dice...')
# test = dice.Percentile()
# print('        Created but not rolled...')
# print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
# print('            test = dice.Percentile() - valid = {}'.format(test.valid))
# print('            test = dice.Percentile() - sides: {}'.format(test.sides))
# print('            test = dice.Percentile() - result: {}'.format(test.result))
# test.roll()
#
# print('        After rolling...')
# print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
# print('            test = dice.Percentile() - result: {}'.format(test.result))
#
# print('        Individual dice...')
# print('            tens (test.tens.result) - {}'.format(test.tens.result))
# print('            ones (test.ones.result) - {}'.format(test.ones.result))
#
# print('    Testing a d1000 percentile-style dice...')
# test = dice.D1000()
# print('        Created but not rolled...')
# print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
# print('            test = dice.Percentile() - valid = {}'.format(test.valid))
# print('            test = dice.Percentile() - sides: {}'.format(test.sides))
# print('            test = dice.Percentile() - result: {}'.format(test.result))
# test.roll()
#
# print('        After rolling...')
# print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
# print('            test = dice.Percentile() - result: {}'.format(test.result))
#
# print('        Changing minimum to zero...')
# test = dice.D1000()
# print('        Created but not rolled...')
# print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
# print('            test = dice.Percentile() - valid = {}'.format(test.valid))
# print('            test = dice.Percentile() - sides: {}'.format(test.sides))
# print('            test = dice.Percentile() - result: {}'.format(test.result))
# test.roll()
#
# print('        After rolling...')
# print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
# print('            test = dice.Percentile() - result: {}'.format(test.result))
#
# print('        Individual dice...')
# print('            hundreds (test.hundreds.result) - {}'
#       .format(test.hundreds.result))
# print('            tens (test.tens.result) - {}'.format(test.tens.result))
# print('            ones (test.ones.result) - {}'.format(test.ones.result))
#
# print('    Testing a d10000 percentile-style dice...')
# test = dice.D10000()
# print('        Created but not rolled...')
# print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
# print('            test = dice.Percentile() - valid = {}'.format(test.valid))
# print('            test = dice.Percentile() - sides: {}'.format(test.sides))
# print('            test = dice.Percentile() - result: {}'.format(test.result))
# test.roll()
#
# print('        After rolling...')
# print('            test = dice.Percentile() - rolled: {}'.format(test.rolled))
# print('            test = dice.Percentile() - result: {}'.format(test.result))
#
# print('        Individual dice...')
# print('            thousands (test.thousands.result) - {}'
#       .format(test.thousands.result))
# print('            hundreds (test.hundreds.result) - {}'
#       .format(test.hundreds.result))
# print('            tens (test.tens.result) - {}'.format(test.tens.result))
# print('            ones (test.ones.result) - {}'.format(test.ones.result))
#
#
# print('Testing: range')
# test = dice.Range(2, 20)
# print('    Created but not rolled...')
# print('        test = dice_range.Range(2, 20) - rolled: {}'.format(test.rolled))
# print('        test = dice_range.Range(2, 20) - result: {}'.format(test.result))
# print('        test = dice_range.Range(2, 20) - dice count: {}'
#       .format(test.dice_count))
# test.roll()
#
# print('    Rolled...')
# print('        test = dice_range.Range(2, 20) - rolled: {}'.format(test.rolled))
# print('        test = dice_range.Range(2, 20) - result: {}'.format(test.result))
# print('        test = dice_range.Range(2, 20) - dice count: {}'
#       .format(test.dice_count))
# count = 1
# for die in test.dice:
#     print('        test = dice_range.Range(2,20) - die {}: {}'
#           .format(count, die.result))
#     count += 1
#
# test = dice.Range(4, 27)
# print('    Creating a range with more dice but a low max, not yet rolled...')
# print('        test = dice_range.Range(4, 27) - rolled: {}'.format(test.rolled))
# print('        test = dice_range.Range(4, 27) - result: {}'.format(test.result))
# print('        test = dice_range.Range(4, 27) - dice count: {}'
#       .format(test.dice_count))
# test.roll()
# print('    Rolled...')
# print('        test = dice_range.Range(4, 27) - rolled: {}'.format(test.rolled))
# print('        test = dice_range.Range(4, 27) - result: {}'.format(test.result))
# print('        test = dice_range.Range(4, 27) - dice count: {}'
#       .format(test.dice_count))
# count = 1
# for die in test.dice:
#     print('        test = dice_range.Range(4, 27) - die {}: {}'
#           .format(count, die.result))
#     count += 1
#
# test = dice.Range(12, 18, 2)
# print('    Creating a range with a minimum higher than the dice count, '
#       'not yet rolled...')
# print('        test = dice_range.Range(12, 18, 2) - rolled: {}'
#       .format(test.rolled))
# print('        test = dice_range.Range(12, 18, 2) - result: {}'
#       .format(test.result))
# print('        test = dice_range.Range(12, 18, 2) - dice count: {}'
#       .format(test.dice_count))
# test.roll()
# print('    Rolled...')
# print('        test = dice_range.Range(12, 18, 2) - rolled: {}'
#       .format(test.rolled))
# print('        test = dice_range.Range(12, 18, 2) - result: {}'
#       .format(test.result))
# print('        test = dice_range.Range(12, 18, 2) - dice count: {}'
#       .format(test.dice_count))
# count = 1
# for die in test.dice:
#     print('        test = dice_range.Range(12, 18, 2) - die {}: {}'
#           .format(count, die.result))
#     count += 1
#
# test = dice.Range(1, 6)
# print('    Creating a range with a low maximum and a single die, '
#       'not yet rolled...')
# print('        test = dice_range.Range(1, 6) - rolled: {}'.format(test.rolled))
# print('        test = dice_range.Range(1, 6) - result: {}'.format(test.result))
# print('        test = dice_range.Range(1, 6) - dice count: {}'
#       .format(test.dice_count))
# test.roll()
# print('    Rolled...')
# print('        test = dice_range.Range(1, 6) - rolled: {}'.format(test.rolled))
# print('        test = dice_range.Range(1, 6) - result: {}'.format(test.result))
# print('        test = dice_range.Range(1, 6) - dice count: {}'
#       .format(test.dice_count))
# count = 1
# for die in test.dice:
#     print('        test = dice_range.Range(1, 6) - die {}: {}'
#           .format(count, die.result))
#     count += 1
#
# print('Testing dice_set...')
# test = dice.DiceSet(dice=[dice.D10(),
#                           dice.D10(),
#                           dice.D10(),
#                           dice.D5(),
#                           dice.D5(),
#                           dice.D2()])
# print('    Created...')
# print('        test = dice_set.DiceSet() - rolled: {}'.format(test.rolled))
# print('        test = dice_set.DiceSet() - valid = {}'.format(test.valid))
# print('        test = dice_set.DiceSet() - result: {}'.format(test.result))
# print('        test = dice_set.DiceSet() - dice count: {}'
#       .format(test.dice_count))
# count = 1
# for die in test.dice:
#     print('        Die {} ({}-sider): {}'
#           .format(count, die.sides, die.result))
#     count += 1
# test.roll()
# print('    Rolled...')
# print('        Rolled: {}'.format(test.rolled))
# print('        Valid = {}'.format(test.valid))
# print('        Result: {}'.format(test.result))
# print('        Dice count: {}'.format(test.dice_count))
# count = 1
# for die in test.dice:
#     print('        Die {} ({}-sider): {}'
#           .format(count, die.sides, die.result))
#     count += 1
# # test.build_stats()
#
# print('    A smaller dice set (2d10)...')
# test = dice.DiceSet(dice=[dice.D10(), dice.D10()])
# test.roll()
# print('        Rolled: {}'.format(test.rolled))
# print('        Valid = {}'.format(test.valid))
# print('        Result: {}'.format(test.result))
# print('        Dice count: {}'.format(test.dice_count))
# count = 1
# for die in test.dice:
#     print('        Die {} ({}-sider): {}'
#           .format(count, die.sides, die.result))
#     count += 1
# # test.build_stats()
#
# print('    Classic D&D dice (3d6)...')
# test = dice.DiceSet(dice=[dice.Die(6), dice.Die(6), dice.Die(6)])
# test.roll()
# print('        Rolled: {}'.format(test.rolled))
# print('        Valid = {}'.format(test.valid))
# print('        Result: {}'.format(test.result))
# print('        Dice count: {}'.format(test.dice_count))
# count = 1
# for die in test.dice:
#     print('        Die {} ({}-sider): {}'
#           .format(count, die.sides, die.result))
#     count += 1
# # test.build_stats()
# # print(test.stats.chance_of(12))
#
# print('    A modified dice set (2d10+5)...')
# test = dice.DiceSet(modifier=5,
#                     modifier_operator=dice.MOD_OPERATORS['+'],
#                     dice = [dice.D10(), dice.D10()])
# test.roll()
# print('        Rolled: {}'.format(test.rolled))
# print('        Valid = {}'.format(test.valid))
# print('        Result: {}'.format(test.result))
# print('        Dice count: {}'.format(test.dice_count))
# count = 1
# for die in test.dice:
#     print('        Die {} ({}-sider): {}'
#           .format(count, die.sides, die.result))
#     count += 1
# # test.build_stats()
#
# print('    A weird modified dice set (3d7*3)...')
# test = dice.DiceSet(modifier=3,
#                     modifier_operator=dice.MOD_OPERATORS['*'],
#                     dice = [dice.Die(7), dice.Die(7), dice.Die(7)])
# test.roll()
# print('        Rolled: {}'.format(test.rolled))
# print('        Valid = {}'.format(test.valid))
# print('        Result: {}'.format(test.result))
# print('        Dice count: {}'.format(test.dice_count))
# count = 1
# for die in test.dice:
#     print('        Die {} ({}-sider): {}'
#           .format(count, die.sides, die.result))
#     count += 1
# # test.build_stats()
#
# print('Testing dice history...')
# test = dice.D10()
# print('    d10 rolled 5 times...')
# for i in range(1, 6):
#     test.roll()
# print('        result: {}'.format(test.result))
# print('        history: {}'.format(test.history))
# print('        d10 __str__: {}'.format(test))
# print('        verbose: {}'.format(test.__str__(True)))
# test = dice.D10000()
# print('    d10000 rolled 5 times...')
# for i in range(1, 6):
#     test.roll()
# print('        result: {}'.format(test.result))
# print('        history: {}'.format(test.history))
# print('        d10000 __str__: {}'.format(test))
# print('        verbose: {}'.format(test.__str__(True)))
# print('    Clearing history...')
# test.clear_history()
# print('        history: {}'.format(test.history))
# test = dice.Range(3, 22, 3)
# print('    range 3-22 (3D10) rolled 5 times...')
# for i in range(1, 6):
#     test.roll()
# print('        result: {}'.format(test.result))
# print('        history: {}'.format(test.history))
# print('        range 3-22 (3D10) __str__: {}'.format(test))
# print('        verbose: {}'.format(test.__str__(True)))
# print('    Clearing history...')
# test.clear_history()
# print('        history: {}'.format(test.history))
#
# print('Back to testing dice_sets...')
# print('History and __str__() this time...')
# print('    2d10+1d5 rolled 5 times...')
# test = dice.DiceSet(dice=[dice.D10(), dice.D10(), dice.D5()])
# for i in range(1, 6):
#     test.roll()
# print('        result: {}'.format(test.result))
# print('        history: {}'.format(test.history))
# print('        set 2d10 + 1d5 __str__: {}'.format(test))
# print('        verbose: {}'.format(test.__str__(True)))
# # test.build_stats()
# # print('        stats(verbose): {}'.format(test.stats.__str__(True)))
# print('    Clearing history...')
# test.clear_history()
# print('        history: {}'.format(test.history))
# print('    d10+d5+d2+d4+d10+d20+d4+d5+d10 rolled 5 times...')
# test = dice.DiceSet(dice=[dice.D10(),
#                           dice.D5(),
#                           dice.D2(),
#                           dice.Die(4),
#                           dice.D10(),
#                           dice.Die(20),
#                           dice.Die(4),
#                           dice.D5(),
#                           dice.D10()])
# for i in range(1, 6):
#     test.roll()
# print('        result: {}'.format(test.result))
# print('        history: {}'.format(test.history))
# print('        set 1d20 + 3d10 + 2d5 + 2d4+ 1d2 __str__: {}'.format(test))
# print('        verbose: {}'.format(test.__str__(True)))
# for die in test.dice:
#     print('Average for d{} is {}'.format(die.sides, die.average))
# print('Testing Diedometer...')
# test = dice.DiceSet(dice=[dice.D10(), dice.D10(), dice.D5()])
# print('    meter = dice.set.Diedometer([die.D10(), die.D10(), die.D5()]')
# meter = dice.Diedometer(test.dice)
# print('    meter: {}'.format(meter.meter))
# print('    incrementing...')
# while not meter.finished:
#     meter.increment()
#     print('        meter: {}'.format(meter.meter))
# meter.reset()
# print('    Again, this time with totals....')
# print('    meter: {}'.format(meter.meter))
# print('    incrementing...')
# while not meter.finished:
#     meter.increment()
#     print('        meter: {}: {}'.format(meter.meter, meter.result))
# meter.reset()
# print('    Again, this time with a max result of 20....')
# print('    meter: {}'.format(meter.meter))
# print('    incrementing...')
# while not meter.finished:
#     meter.increment()
#     while meter.result > 20:
#         meter.drop_die()
#     print('        meter: {}: {} (dropped: {}'.format(meter.meter,
#                                                       meter.result,
#                                                       meter.dropped_dice))
# meter.reset()
# print('    Again, this time with a max result of 12....')
# print('    meter: {}'.format(meter.meter))
# print('    incrementing...')
# while not meter.finished:
#     meter.increment()
#     while meter.result > 12:
#         meter.drop_die()
#     print('        meter: {}: {} (dropped: {}'.format(meter.meter,
#                                                       meter.result,
#                                                       meter.dropped_dice))
# print('    One last time, with a large dice set (6d10) and a low limit (35....')
# test = dice.DiceSet(dice=[dice.D10(),
#                           dice.D10(),
#                           dice.D10(),
#                           dice.D10(),
#                           dice.D10(),
#                           dice.D10()])
# meter = dice.Diedometer(test.dice)
# print('    meter: {}'.format(meter.meter))
# print('    incrementing...')
# while not meter.finished:
#     meter.increment()
#     while meter.result > 35:
#         meter.drop_die()
#     # print('        meter: {}: {} (dropped: {}'.format(meter.meter,
#     #                                                   meter.result,
#     #                                                   meter.dropped_dice))
# print('    done...')

test = dice.Die(6)
print('Testing dice stats for a single die...')
print('    Stats for a single d6...')
print('        stats dictionary: {}'.format(test.stats.stats_dict))
print('        possible combinations: {}'.format(test.stats.combo_count))
print('        average result: {}'.format(test.stats.average))
print('        stats table:\n{}\n'.format(test.stats.csv()))

test = dice.D10()
print('    Stats for a single d10...')
print('        stats dictionary: {}'.format(test.stats.stats_dict))
print('        possible combinations: {}'.format(test.stats.combo_count))
print('        average result: {}'.format(test.stats.average))
print('        stats table:\n{}\n'.format(test.stats.csv()))

test = dice.Percentile()
print('    Stats for a percentile die...')
print('        stats dictionary: {}'.format(test.stats.stats_dict))
print('        possible combinations: {}'.format(test.stats.combo_count))
print('        average result: {}'.format(test.stats.average))

test = dice.D1000()
print('    Stats for a D1000...')
print('        stats dictionary: {}'.format(test.stats.stats_dict))
print('        possible combinations: {}'.format(test.stats.combo_count))
print('        average result: {}'.format(test.stats.average))

test = dice.DiceSet(dice=[dice.D10(),dice.D10()])
print('    Stats for 2D10...')
print('        stats dictionary: {}'.format(test.stats.stats_dict))
print('        possible combinations: {}'.format(test.stats.combo_count))
print('        average result: {}'.format(test.stats.average))
print('        stats table:\n{}\n'.format(test.stats.csv()))

test = dice.DiceSet(dice=[dice.D10(), dice.D10(), dice.D5(),dice.D2()])
print('    Stats for 2D10+d5+d2...')
print('        stats dictionary: {}'.format(test.stats.stats_dict))
print('        possible combinations: {}'.format(test.stats.combo_count))
print('        average result: {}'.format(test.stats.average))
print('        stats table:\n{}\n'.format(test.stats.csv()))

test = dice.DiceSet(dice=[dice.D10(), dice.D10()],
                    modifier=5,
                    modifier_operator=dice.MOD_OPERATORS['+']
                    )
print('    Stats for 2D10+5...')
print('        stats dictionary: {}'.format(test.stats.stats_dict))
print('        possible combinations: {}'.format(test.stats.combo_count))
print('        average result: {}'.format(test.stats.average))
print('        stats table:\n{}\n'.format(test.stats.csv()))

test = dice.DiceSet(dice=[dice.D10(), dice.D10()],
                    modifier=5,
                    modifier_operator=dice.MOD_OPERATORS['*']
                    )
print('    Stats for 2D10*5...')
print('        stats dictionary: {}'.format(test.stats.stats_dict))
print('        possible combinations: {}'.format(test.stats.combo_count))
print('        average result: {}'.format(test.stats.average))
print('        stats table:\n{}\n'.format(test.stats.csv()))

test = dice.DiceSet(dice=[dice.D10(), dice.D10()],
                    modifier=5,
                    modifier_operator=dice.MOD_OPERATORS['-']
                    )
print('    Stats for 2D10-5...')
print('        stats dictionary: {}'.format(test.stats.stats_dict))
print('        possible combinations: {}'.format(test.stats.combo_count))
print('        average result: {}'.format(test.stats.average))
print('        stats table:\n{}\n'.format(test.stats.csv()))

test = dice.DiceSet(dice=[dice.D10(),dice.D10(),dice.D10()])
print('    Stats for 3D10...')
print('        stats dictionary: {}'.format(test.stats.stats_dict))
print('        possible combinations: {}'.format(test.stats.combo_count))
print('        average result: {}'.format(test.stats.average))
print('        stats table:\n{}\n'.format(test.stats.csv()))

test = dice.Range(3,25)
print('    Stats for Range 3-25...')
print('        stats dictionary: {}'.format(test.stats.stats_dict))
print('        possible combinations: {}'.format(test.stats.combo_count))
print('        average result: {}'.format(test.stats.average))
print('        stats table:\n{}\n'.format(test.stats.csv()))

test = dice.Range(4,25)
print('    Stats for Range 4-25...')
print('        stats dictionary: {}'.format(test.stats.stats_dict))
print('        possible combinations: {}'.format(test.stats.combo_count))
print('        average result: {}'.format(test.stats.average))
print('        stats table:\n{}\n'.format(test.stats.csv()))

test = dice.Range(3,10,1)
print('    Stats for Range 3-10 (1 die)...')
print('        stats dictionary: {}'.format(test.stats.stats_dict))
print('        possible combinations: {}'.format(test.stats.combo_count))
print('        average result: {}'.format(test.stats.average))
print('        stats table:\n{}\n'.format(test.stats.csv()))

print('Testing Modifiers...')
print('   Creating new modifier 5 (default operator: +)...')
source = "nothing"
test = stats.Modifier(source, 5)
print('       stats.Modifier(5) __str__(): {}\n'.format(test.__str__()))
print('   Creating new modifier +15 ...')
test = stats.Modifier(source, 15, dice.MOD_OPERATORS['+'])
print('       stats.Modifier(5) __str__(): {}\n'.format(test.__str__()))
print('   Creating new modifier -7 ...')
test = stats.Modifier(source, 7, dice.MOD_OPERATORS['-'])
print('       stats.Modifier(5) __str__(): {}\n'.format(test.__str__()))
print('   Creating new modifier *1.2 ...')
test = stats.Modifier(source, 1.2, dice.MOD_OPERATORS['*'])
print('       stats.Modifier(5) __str__(): {}\n'.format(test.__str__()))
print('   Creating new modifier /1.1 ...')
test = stats.Modifier(source, 1.1, dice.MOD_OPERATORS['/'])
print('       stats.Modifier(5) __str__(): {}\n'.format(test.__str__()))

print('Testing ModifierSets...')
print('   Creating new set with 10 modifiers...')
test = stats.ModifierSet([stats.Modifier(source, 5),
                          stats.Modifier(source, 1.2, dice.MOD_OPERATORS['/']),
                          stats.Modifier(source, 10, dice.MOD_OPERATORS['-']),
                          stats.Modifier(source, 5, stats.add_percent),
                          stats.Modifier(source, 15, stats.add_percent),
                          stats.Modifier(source, 1.05, dice.MOD_OPERATORS['*']),
                          stats.Modifier(source, 2, dice.MOD_OPERATORS['-']),
                          stats.Modifier(source, 12, dice.MOD_OPERATORS['+']),
                          stats.Modifier(source, 1.1, dice.MOD_OPERATORS['*']),
                          stats.Modifier(source, 15, stats.sub_percent)])
print('        Sorted Descriptor of ModifierSet: {}'.format(test.__str__()))

print('\nTesting Stats...')
print("    Creating new stat using previous modifiers...")
stat_test = stats.Stat("STR",55,"Strength",test)
print('        Stat Abbreviation: {}'.format(stat_test.abbreviation))
print('        Stat Name: {}'.format(stat_test.name))
print('        Stat Base Score: {}'.format(stat_test.base_score))
print('        Stat Modified Score: {}'.format(stat_test.score))
print('        Stat Modifiers: {}'.format(stat_test.modifiers.__str__()))