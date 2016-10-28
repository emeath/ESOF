import re
roboRegex = re.compile(r'robocop', re.I)
mo = roboRegex.search('RoboCop is part man, part machine, all cop.')
if mo != None:
	print('mo: ', mo.group())
mo = roboRegex.search('ROBOCOP is part man, part machine, all cop.')
if mo != None:
	print('mo: ', mo.group())
mo = roboRegex.search('Al, why does yout programming book talk about robocop so much?')
if mo != None:
	print('mo: ', mo.group())