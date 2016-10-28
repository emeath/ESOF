import re
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
if mo != None:
	print('mo:	', mo)
print('')

mo = namesRegex.sub('****', 'Agent Alice gave the secret documents to Agent Bob.')
if mo != None:
	print('mo:	', mo)
print('')

mo = namesRegex.sub('----', 'Agent Alice gave the secret documents to Agent Bob.')
if mo != None:
	print('mo:	', mo)
print('')

