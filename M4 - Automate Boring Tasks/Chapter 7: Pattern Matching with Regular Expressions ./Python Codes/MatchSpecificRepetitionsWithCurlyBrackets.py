import re
jokerRegex = re.compile(r'Ha')
mo = jokerRegex.search('Ha! Batman! Whhy so Serious?')
print('Laughs that i\'ve found: ' + mo.group())
