#!/usr/bin/env python3
import sys
comb = {}#save ID and orginal salary
comb_taxed = {}#save ID and taxed salary
for arg in sys.argv[1:]:
    if arg != './calculator.py':
        list1 = arg.split(':')
        id = list1[0]
        try:
            salary = int(list1[1])
        except ValueError:
            print('pls check your input, should be numbers')
            continue
        comb[id] = salary
#print(type(comb))
#for x,y in comb.items():
#    print("{} {}".format(x,y))


def incoming(**comb):#calulate taxed salary
    for x,y in comb.items():
        base = y*0.835 - 3500#base = orignal salary - insurances- 3500
#        print("y=",y)
#        print("base=",base)
        if base <= 0:
            incoming = y
        elif 0<base<1500:
            incoming = y - base*0.03
        elif base<4500:
            incoming = y - (base*0.1 - 105)
        elif base<9000:
            incoming = y - (base*0.2 - 555)
        elif base<35000:
            incoming = y - (base*0.25 - 1005)
        elif base<55000:
            incoming = y - (base*0.3 - 2755)
        elif base<80000:
            incoming = y - (base*0.35 - 5505)
        else:
            incoming = y - (base*0.45 - 13505)
        incoming = incoming - y*0.165
#        print("incoming=",incoming)
        comb_taxed[x] = incoming

incoming(**comb)
for x,y in comb_taxed.items():
    print("{}:{:.2f}".format(x,y))
