#!/usr/bin/env python3

expect = [0, 1]
result = []
result_split = []
dics = []

for i in range(2, 101):
    expect.append(expect[i - 1] + expect[i - 2])
with open('out', 'r') as f:
    tmp = f.readline()
    while (tmp):
        result.append(tmp)
        tmp = f.readline()
    f.close()
for r in result:
    if (r.find('Reading') != -1):
        result_split.append(r.split(' '))
        k = int(result_split[-1][5].split(',')[0])
        f0 = int(result_split[-1][9].split('.')[0])
        dics.append((k, f0))
for i in dics:
    fib = i[1] 
    if (expect[i[0]] != fib):
        print('f(%s) fail' % str(i[0]))
        print('input: %s' %(fib))
        print('expected: %s' %(expect[i[0]]))
        exit()
