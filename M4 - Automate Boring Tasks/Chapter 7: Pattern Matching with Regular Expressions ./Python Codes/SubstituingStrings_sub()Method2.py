import re
agentNamesRegex = re.compile(r'Agent (\w)(\w*)')
mo = agentNamesRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
if mo != None:
	print('mo:	', mo)
