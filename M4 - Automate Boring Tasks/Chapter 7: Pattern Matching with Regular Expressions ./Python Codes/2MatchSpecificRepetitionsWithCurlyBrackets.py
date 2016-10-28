import re
jokerRegex = re.compile(r'(Ha){2}')
mo = jokerRegex.search('Ha! HaHa! Batman you fool!')
print('Laughs that i\'ve found: ' + mo.group())