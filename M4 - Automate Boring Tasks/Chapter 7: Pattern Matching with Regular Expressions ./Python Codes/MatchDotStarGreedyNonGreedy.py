import re
nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<To serve man> for dinner.>')
if mo != None:
	print('mo: ', mo.group())
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
if mo!=None:
	print('mo: ', mo.group())