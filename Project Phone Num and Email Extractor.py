import re, pyperclip

# Phone num regular expression
phoneRegex = re.compile(r'''
# 555-5555, 818-555-5533, (503)822-3415, x12312, etx12312, etx.123123, 123123
(
((\d\d\d) | (\(\d\d\d\)))?
(\s|-)?
\d\d\d
(\s|-)
\d\d\d\d
(\s)?
(((ext(\.)?\s)|x)
    (\d{2,7}))?
)    
''', re.VERBOSE)

# Email regular expression
emailRegex = re.compile(r'''
# something.+_@something.+_

[a-zA-Z0-9+_.]+
@
[a-zA-Z0-9+_.]+

''', re.VERBOSE)

# Get text from clipboard
text = pyperclip.paste()

#Extract email/phoneNumber from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Each entry should be its own line.
results = '\n'.join(extractedEmail) + '\n' + '\n'.join(allPhoneNumbers)
pyperclip.copy(results)