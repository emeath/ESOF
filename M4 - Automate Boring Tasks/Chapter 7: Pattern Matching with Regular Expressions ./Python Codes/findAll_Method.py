import re
Regex = re.compile(r'\d{3}-\d{3}-\d{4}')
moFirst = Regex.search('Cell: 415-555-9999 Work: 212-555-0000') # <- will only show the first occurrence
print('search method	->	moFirst.group(): ' + moFirst.group())

moAll = Regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print('Complete list 	->	moAll:	', moAll) # findall returns a list
#print('First: ', moAll(1)) 	#nao da certo
#print('Second: ', moAll(2))	#nao da certo
print('moAll[0] 	->	First:	', moAll[0])
print('moAll[1] 	->	Second:	', moAll[1])