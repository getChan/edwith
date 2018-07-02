import urllib.request, urllib.parse, urllib.error
from twurl import argument
import ssl

print(' * Calling Twitter...')
url = argument(
    'https://api.twitter.com/1.1/statuses/user_timeline.json',
    {
        'screen_name' : 'drchuck', 'count' : '2'
    })
print(url)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.SEERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data)

print('=======================')
headers = dict(connection.getheaders())
print(headers)