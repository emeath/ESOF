import re
noNewLineRegex = re.compile('.*')
mo = noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
if mo != None:
	print('mo: ', mo.group())

newLineRegex = re.compile('.*', re.DOTALL)
mo = newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
if mo != None:
	print('mo: ', mo.group())