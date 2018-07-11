#! /usr/env/python3

import pyperclip
import re

# Create regex for phone numbers
phoneRegex = re.compile(r'''
# 555-555-5555, 555-5555, (555) 555-5555, 555-5555 ext 12345, ext. 12345, x123456
(
    ((\d{3}) | (\(\d{3}\)))?    # area code (optional)
    (\s | -)                    # 1st separator
    \d{3}                       # 1st 3 digits
    -                           # separator
    \d{4}                       # last 4 digits
    ((( ext(\.)?\s)|s)          # extension word-part (optional)
    (\d{2,5}))?                 # extension (optional)
)''', re.VERBOSE)


# Create regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

    [a-zA-Z0-9_.+]+  # user name
    @               # @ symbol
    [a-zA-Z0-9_.+]+ # domain name
''', re.VERBOSE)


# Get the text off the clipboard
text = pyperclip.paste()


# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


# Copy the extracted email/phone to the clipboard
content = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(content)
