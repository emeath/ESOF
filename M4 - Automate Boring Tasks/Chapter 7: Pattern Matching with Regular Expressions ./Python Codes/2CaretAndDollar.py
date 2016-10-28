import re
endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your number is 42')
if mo != None:
	print('mo: ', mo)
else:
	print('Pattern not found!')

print('-------------------------------------------------------')
print('Second mo:')
mo = endsWithNumber.search('Yout number is forty two.')
if mo != None:
	print('mo: ', mo)
else:
	print('Pattern not found!')