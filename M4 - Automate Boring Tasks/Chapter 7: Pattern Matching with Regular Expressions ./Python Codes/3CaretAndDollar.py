import re
allRegex = re.compile(r'^Hello World!$')
mo = allRegex.search('Hello World!')
if mo != None:
	print('(1) mo: ', mo)
else:
	print('(1) Not Found!')

mo = allRegex.search('This is a Hello World! message')
if mo != None:
	print('(2) mo: ', mo)
else:
	print('(2) Not Found!')