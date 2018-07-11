import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 afterwards'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match_object = phoneNumRegex.search(message)
print(match_object.group())
print(phoneNumRegex.findall(message))
