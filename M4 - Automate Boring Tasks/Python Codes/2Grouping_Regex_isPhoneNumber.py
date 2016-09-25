import re
phoneRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phoneRegex.search('My phone number is (415) 555-4242')
areaPar, mainNumber = mo.groups()
print('area: ',	areaPar)
print('main number: ',	mainNumber)