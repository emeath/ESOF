import re
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman and Robin')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman and Rowobin')
print(mo2.group())