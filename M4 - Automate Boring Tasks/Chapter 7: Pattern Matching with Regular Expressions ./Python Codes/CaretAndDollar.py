import re
beginWithHello = re.compile(r'^Hello')
mo = beginWithHello.search('Hello World! I\'m a python program!')
if mo != None:
	print('mo: ', mo)

mo = beginWithHello.search('I\'m a python program! Hello Sir!')
if mo != None:
	print('mo: ', mo)
else:
	print(None, 'Did\'nt match!')	