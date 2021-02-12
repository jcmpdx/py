import datetime

m = 'Mike'
j = 'JC'
d = 0
for i in range(50):
    y = datetime.datetime.now() + datetime.timedelta(days=d)
    if d % 2 == 0:
        person = j
    else:
        person = m
    if y.weekday() == 5 or y.weekday() == 6:
        pass
    else:
        print(y.strftime('%A') + ' : {}'.format(person))

    d += 1