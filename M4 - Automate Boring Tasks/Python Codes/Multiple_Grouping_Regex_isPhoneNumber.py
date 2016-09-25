import re
heroesRegex = re.compile(r'Iron Man|Spider Man')
mo1 = heroesRegex.search('Spider Man and Iron Man are Amazing!')
mo2 = heroesRegex.search('Both Iron Man and Spider man are Awesome!')

#mo3 = mo2

print ('First Matching Object:	', 	mo1.group())
print ('Second Matching Object:	',	mo2.group())
