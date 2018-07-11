def isPhoneNumber(text):  # 555-555-5555
    if len(text) != 12:
        return False  # Incorrect Length
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # Wrong area code
    if text[3] != '-':
        return False  # no dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # Wrong 1st 3 digits
    if text[7] != '-':
        return False  # no 2nd dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # Wrong last 4 digits
    return True


print(isPhoneNumber('123456789'))
print(isPhoneNumber('123-456-7890'))
print(isPhoneNumber('123,456,7890'))
print(isPhoneNumber('abc-456-7890'))

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 afterwards'

foundNumber = False
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True

if not foundNumber:
    print('Could not find any phone numbers.')
