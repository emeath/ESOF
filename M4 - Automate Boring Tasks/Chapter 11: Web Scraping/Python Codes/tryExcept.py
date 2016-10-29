import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exists')
try:
	res.raise_for_status()
except Exception as exc:
	print('Houve um problema: %s' % (exc))