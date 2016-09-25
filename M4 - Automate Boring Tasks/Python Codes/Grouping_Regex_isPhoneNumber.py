import re
regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = regex.search('My number is 415-555-4242. ')
# print('Number found: ' + mo.group() + '\n')
# print('Area code: ' + mo.group(1) + '\n')
# print('Following: ' + mo.group(2) + '\n')

# print('Number found: ' 	+ mo.group(	))
# print('Area code: ' 	+ mo.group(1))
# print('Following: ' 	+ mo.group(2))

#	>>>mo.groups()
#	('415','555-4242')
#	... area, main = '415', '555-4242' ...


areaCode, mainNumber = mo.groups()
print('Area code: ', 	 areaCode)
print('Main number: ', 	 mainNumber)