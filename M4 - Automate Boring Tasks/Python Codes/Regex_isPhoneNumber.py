import re
Regex_PhoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = Regex_PhoneNumber.search('My expensive number is: 415-555-4242. Note o 42. A resposta de Tudo!')
print('Phone number found: ',  mo.group()) 
# r -> raw_strings
