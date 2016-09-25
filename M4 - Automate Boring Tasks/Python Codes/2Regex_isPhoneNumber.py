import re

#tel_obj = re.compile(r'\d \d\d\d\d-\d\d\d\d')
tel_obj = re.compile(r'\d \d{4}-\d{4}')
MatchingObject = tel_obj.search('Meu nome eh Matheus Martins Jeronimo. Moro atualmente em Uberlandia. Meu numero de celular eh: 9 9104-2406 porem pode me contactar em 3662-0750')
print('Numero encontrado: ' + MatchingObject.group())
