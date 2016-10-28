import re
greedyJokerRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyJokerRegex.search('HaHaHaHaHa! Joker > Batman!')
print('greedy mo1: ' + mo1.group())

nonGreedyJokerRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyJokerRegex.search('HaHaHaHaHa! Joker > Batman!')
print('greedy mo2: ' + mo2.group())