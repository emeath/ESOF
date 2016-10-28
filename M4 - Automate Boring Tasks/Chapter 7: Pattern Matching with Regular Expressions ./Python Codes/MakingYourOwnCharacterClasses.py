import re
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('Barata tonta 123 Macaco no fi0 hu3')
print('Vowels found:			', mo)
print('Quantidade de vogais:		', len(mo))