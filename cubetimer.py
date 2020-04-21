#cubetimer
v = '1.1.6'
import time, random
data_sessions = ''
current = []
current_formatted = ''
others_formatted = ''
n = ''
u = 0
w = 0
x = 0
z = 0
best_five = 0
best_twelve = 0
best_solve = 999.99
worst_solve = 0.0
with open('cubedata', 'r') as y:
    data = y.read()
solves = data.split(':')[0]
session = input('cubetimer {}\ntotal solves: {}\nenter session (previous or new): '.format(v, solves))
for i in data.split(':')[1:]:
    i = i.split('/')
    data_sessions = data_sessions + i[0] + ' '
if session in data_sessions:
    print('retrieving session...')
    current = data.split(session)[1].split(':')[0][1:].split()
    print('successful\n{}'.format(session))
    for i in current:
        if float(i) > worst_solve:
            worst_solve = float(i)
        if float(i) < best_solve:
            best_solve = float(i)
    for i in current:
        x += float(i)
        z += 1.0
    try:
        session_avg = x/z
    except:
        session_avg = 0.00
    x = 0
    z = 0
    for i in current[-5:]:
        x += float(i)
    current_five = x/5
    x = 0
    for i in current[-12:]:
        x += float(i)
    current_twelve = x/12
    x = 0
    if current_five > best_five:
        best_five = current_five
    if current_twelve > best_twelve:
        best_twelve = current_twelve
    print('overall avg: {:.2f}\nbest 5 of load: {:.2f}\nbest 12 of load: {:.2f}\ncurrent 5: {:.2f}\ncurrent 12: {:.2f}\nbest solve: {:.2f}\nworst solve: {:.2f}'.format(session_avg, best_five, best_twelve, current_five, current_twelve, best_solve, worst_solve))
else:
    print('creating session...')
    with open('cubedata', 'a') as y:
        y.write(':{}/'.format(session))
    print('successful')
def scramble(session):
    last = '0'
    scramble = ''
    if session == '2x2':
        moves = ['F', 'R', 'U', 'F\'', 'R\'', 'U\'', 'F2', 'R2', 'U2']
        for i in moves:
            index = random.randint(0, 8)
            while last[0] == moves[index][0]:
                index = random.randint(0, 8)
            scramble = scramble + moves[index] + ' '
            last = moves[index]
    if session == '3x3':
        moves = ['F', 'R', 'U', 'F\'', 'R\'', 'U\'', 'F2', 'R2', 'U2', 'B', 'L', 'D', 'B\'', 'L\'', 'D\'', 'B2', 'L2', 'D2']
        for i in moves:
            index = random.randint(0, 17)
            while last[0] == moves[index][0]:
                index = random.randint(0, 17)
            scramble = scramble + moves[index] + ' '
            last = moves[index]
    return scramble[:-1]
print('ready to time\ntype exit to save and quit, enter to start\nno inspection')
n = input('{}: '.format(scramble(session)))
while n != 'exit':
    start = time.time()
    n = input()
    end = time.time()
    timed = end - start
    timed = '{:.2f}'.format(timed)
    print(timed)
    current.append(timed)
    if float(timed) > worst_solve:
        worst_solve = float(timed)
        print('new worst solve')
    if float(timed) < best_solve:
        best_solve = float(timed)
        print('new best solve')
    w += 1
    if (w % 5) == 0:
        for i in current[-5:]:
            x += float(i)
        current_five = x/5
        x = 0
        print('new avg 5: {:.2f}'.format(current_five))
        if current_five > best_five:
            print('also session record for 5')
            best_five = current_five
    if (w % 12) == 0:
        for i in current[-12:]:
            x += float(i)
        current_five = x/12
        x = 0
        print('new avg 12: {:.2f}'.format(current_twelve))
        if current_twelve > best_twelve:
            print('also session record for 12')
            best_twelve = current_twelve
    for i in current:
        x += float(i)
        z += 1.0
    session_avg = x/z
    x = 0
    z = 0
    print('avg: {:.2f}'.format(session_avg))
    n = input('{}: '.format(scramble(session)))
print('writing to cubedata...')
separate = data.split(':')
total = int(separate[0]) + w
for i in current:
    current_formatted = current_formatted + i + ' '
for i in separate:
    if session in i:
        pulled = i
        del separate[u]
    u += 1
for i in separate[1:]:
    others_formatted = others_formatted + i
write = '{}:{}/{}:{}'.format(total, session, current_formatted, others_formatted)
with open('cubedata', 'w') as y:
    y.write(write)
print('finished')
#change 5 and 12 avgs to 3of and 10of