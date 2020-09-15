import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
print(type(conn))
fromEmail = 'joker91186@gmail.com'
print(conn.ehlo())
print(conn.starttls())

# Needed to generate an App Password in Gmail for the below password
pw = 'xxxxxxxxxxxxxxxxxxx'
# Needed to generate an App Password in Gmail for the below password

try:
    print(conn.login(fromEmail, pw))
except:
    print('\n!!!Bad password!!!\n')

emails = {
    'Bob Shmee': 'joker91186@gmail.com',
    'Ensign Ro': 'jcm91186@gmail.com'
}

emailList = list(emails.values())
emailNames = list(emails.keys())

for i in range(0, (len(emailList))):
    print(emailList[i])
    print('Email message to: ' + emailNames[i])
    conn.sendmail(fromEmail, emailList[i], 'Subject: Pyemail test\n\nDear ' + str(emailNames[i]) + ''',

Thank you for taking part in this amazing experiment!

Best,
JC
    ''')

# disconnects from SMTP server
conn.quit()
