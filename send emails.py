import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
print(type(conn))
fromEmail = 'joker91186@gmail.com'
print(conn.ehlo())
print(conn.starttls())
# App Password in Gmail for the below password
pw = 'xxx'
print(conn.login(fromEmail, pw))

conn.sendmail(fromEmail, 'joker91186@gmail.com', '''Subject: another email test

Hello,

Test message from Python smptlib.

best,
JC''')
# disconnects from SMTP server
conn.quit()