import re
wholeStringIsNum = re.compile(r'^\d+$')
mo = wholeStringIsNum.search('1234567890')
if mo != None:
	print(mo)
else:
	print('Not Found!')

mo = wholeStringIsNum.search('12345zxcvb67890')
if mo != None:
	print(mo)
else:
	print('Not Found!')

mo = wholeStringIsNum.search('12 34567890')
if mo != None:
	print(mo)
else:
	print('Not Found!')