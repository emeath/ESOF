import re
bat_chatoRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_chatoRegex.search('Batmobile lost a wheel. What a pitty')
print('Batman, Batmobile, Batcopter or Batbat? ',  mo.group())