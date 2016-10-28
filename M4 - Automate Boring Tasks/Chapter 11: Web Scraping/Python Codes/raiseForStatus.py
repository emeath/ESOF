import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()