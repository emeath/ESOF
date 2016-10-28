import re
atRegex = re.compile(r'.at')
mo = atRegex.findall('The car in the hat sat on the flat mat at night')
if mo != None:
	print('mo: ', mo)

atRegex2 = re.compile(r'..at')
mo = atRegex2.findall('The car in the hat sat on the flat mat at night')
if mo != None:
	print('mo: ', mo)