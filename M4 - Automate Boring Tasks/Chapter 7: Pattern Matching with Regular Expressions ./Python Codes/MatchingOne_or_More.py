import re
batRegex = re.compile(r'Bat(wo\+)+man')
mo1 = batRegex.search('The Adventures of Batman')
if mo1 == None:
	print(mo1==None)
mo2 = batRegex.search('The Adventures of Batwo+man')
print('mo2.group() = ' + mo2.group())
mo3 = batRegex.search('The Adventures of Batwo+wo+wo+wo+man')
print('mo3.group() = ' + mo3.group())