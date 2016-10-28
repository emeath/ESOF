import re
xmasRegex = re.compile(r'\d+\s\w+\s\w+')
mo = xmasRegex.findall('8 pessoas nadam de costas 	\
						77 pessoas nadam crwal		\
						688 pessoas odeiam natacao	')

print('numbers found: ', mo)