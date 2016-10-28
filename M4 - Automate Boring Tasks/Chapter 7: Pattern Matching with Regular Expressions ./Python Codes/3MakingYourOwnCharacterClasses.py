import re
regex = re.compile(r'[^a-zA-Z]')
mo = regex.findall('123 32 3 222 12 44 matheus 123')
print('Here\'s what i\'ve found:	', mo)