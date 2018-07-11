import re

message = 'Call me 111-111-1111 tomorrow, or at 222-222-2222 afterwards'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match_object = phoneNumRegex.search(message)
print(match_object.group())
print(phoneNumRegex.findall(message))

message = 'My number is  123-456-7890.'
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match_object = phoneNumRegex.search(message)
print(match_object.group())

message = 'My number is  (123) 456-7890.'
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
match_object = phoneNumRegex.search(message)
print(match_object.group())
print(match_object.group(0))
print(match_object.group(1))
print(match_object.group(2))

message = 'Batman\'s Batmobile lost a wheel.'
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
match_object = batRegex.search(message)
print(batRegex.findall(message))
print(match_object.group())
print(match_object.group(0))
print(match_object.group(1))

message = 'The Adventures of Batwoman'
batRegex = re.compile(r'Bat(wo)?man')
match_object = batRegex.search(message)
print(match_object.group())

message = 'My number is  123-456-7890 or 000-1234.'
phoneNumRegex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')  # ? is 0 or 1 times
match_object = phoneNumRegex.search(message)
print(phoneNumRegex.findall(message))
print(match_object.group())

message = 'The Adventures of Batwowowoman'
batRegex = re.compile(r'Bat(wo)*man')  # * is 0 or more times
match_object = batRegex.search(message)
print(match_object.group())

message = 'The Adventures of Batwowowoman'
batRegex = re.compile(r'Bat(wo)+man')  # * is 1 or more times
match_object = batRegex.search(message)
print(match_object.group())

message = 'The Adventures of +*?'
batRegex = re.compile(r'\+\*\?')
match_object = batRegex.search(message)
print(match_object.group())

message = 'HaHaHaHaHa'
haRegex = re.compile(r'(Ha){3}')
match_object = haRegex.search(message)
print(match_object.group())

message = 'My number is  123-456-7890,098-765-4321,000-0000.'
phoneNumRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
match_object = phoneNumRegex.search(message)
print(match_object.group())

message = 'HaHaHaHaHa'
haRegex = re.compile(r'(Ha){3,5}')
match_object = haRegex.search(message)
print(match_object.group())

message = '1234567890'
greedyDigitRegex = re.compile(r'(\d){3,5}')
greedy_match_object = greedyDigitRegex.search(message)
print(greedy_match_object.group())

message = '1234567890'
digitRegex = re.compile(r'(\d){3,5}?')
match_object = digitRegex.search(message)
print(match_object.group())

message = 'My number is  123-456-7890, 098-765-4321, 000-0000, or 111-111-1111.'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegexGroup = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneNumRegex.findall(message))
print(phoneNumRegexGroup.findall(message))

message = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'
xmaxRegex = re.compile(r'\d+\s\w+')
print(xmaxRegex.findall(message))

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food'))
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats baby food'))
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food'))
lowerCaseRegex = re.compile(r'[a-z]')
print(lowerCaseRegex.findall('Robocop eats Kraft food'))
agRegex = re.compile(r'[a-gA-G]')
print(agRegex.findall('Robocop eats baby food'))

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.findall('Hello World'))
print(beginsWithHelloRegex.findall('Howdy, Hello World'))

endsWithHelloRegex = re.compile(r'Hello$')
print(endsWithHelloRegex.findall('Hello World'))
print(endsWithHelloRegex.findall('Howdy, Hello'))

allDigits = re.compile(r'^\d+$')
print(allDigits.findall('123456789'))
print(allDigits.findall('123-456-789'))

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

text = 'First Name: Kyle Last Name: Galloway'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
name_match = nameRegex.findall(text)
print(name_match)
print('Your name is %s %s' % (name_match[0][0], name_match[0][1]))

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

serve = '<To serve humans> for dinner.>'
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
dotStar = re.compile(r'.*', re.DOTALL)
mo = dotStar.search(prime)
print(mo.group())

vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Al, why does your book talk about RoboCop so much?'))

vowelRegex = re.compile(r'[aeiou]', re.I)
print(vowelRegex.findall('Al, why does your book talk about RoboCop so much?'))

text = 'Agent Alice gave the secret documents to Agent Bob.'
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall(text))
print(namesRegex.sub('REDACTED', text))
print(namesRegex.sub(r'Agent \1*****', text))

text = 'My number is  123-456-7890, (098) 765-4321, 000-0000, or 111-111-1111 x1111.'
phoneNumRegex = re.compile(r'''(
                            ((\d\d\d-)          # area code (without parens, with dash)
                            | (\(\d\d\d\)\s))?  # -or- area code (with parens, no dash)
                            \d\d\d              # local code
                            -                   # dash
                            \d\d\d\d            # number
                            (\sx\d{2,4})?       # extension, (x1234, x13)
                            )''', re.VERBOSE | re.IGNORECASE | re.DOTALL)

print(phoneNumRegex.findall(text))
print(list(map(lambda tup: tup[0], phoneNumRegex.findall(text))))
