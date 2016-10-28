import re
batRegex = re.compile(r'Batman|Tina Turner')
mo = batRegex.findall('These people are great friends: Tina Turner and Batman')
print('Friends Found: ', mo[0], 'and' , mo[1])