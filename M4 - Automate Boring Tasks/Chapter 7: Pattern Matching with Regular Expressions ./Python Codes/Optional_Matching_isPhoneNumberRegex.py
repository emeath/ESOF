import re
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My phone number is: 415-555-4242')
print('mo1.group(): ' + mo1.group())
mo2 = phoneRegex.search('I dont care. my phone is: 555-4242')
print('mo2.group(): ' + mo2.group())