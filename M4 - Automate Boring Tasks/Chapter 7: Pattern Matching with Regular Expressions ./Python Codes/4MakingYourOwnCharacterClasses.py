import re
notVowelRegex = re.compile(r'[^aeiouAEIOU]')
ListRegexFindall = notVowelRegex.findall('Robocop eats baby food. BABY FOOD!')
print('Here\'s Jhonny! ', ListRegexFindall)