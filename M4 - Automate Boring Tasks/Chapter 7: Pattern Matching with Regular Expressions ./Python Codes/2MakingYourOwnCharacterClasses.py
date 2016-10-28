import re
regex = re.compile(r'[a-zA-Z0-9]{7,}')
mo = regex.findall('..,.;,.,.,;. matheus martins JERONimo ;;asd;aasda;.;,,²¹²³')
print('Here\'s what i\'ve found:	', mo)