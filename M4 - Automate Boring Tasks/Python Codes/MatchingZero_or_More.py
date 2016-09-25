import re
regexObj = re.compile(r'Bat(wo)*man')
mo1 = regexObj.search('The Adventures of Batman')
mo2 = regexObj.search('The Adventures of Batwoman')
#mo3 = regexObj.search('The Adventures of Batwemen')
mo4 = regexObj.search('The Adventures of Batwowowowowoman')

print('mo1:	',	mo1.group())
print('mo2:	',	mo2.group())
#print('mo3:	',	mo3.group())
print('mo4:	',	mo4.group())