from os import close
import random

x = "1234567890"

password = ''

def master():
    global x
    global password
    for i in range(2):
        password = password + random.choice(x)
    
    f = open('1.txt', 'r')
    t = 0
    for x in f:
        t+=1
    f.close()
    t-=1
    t = int(t/3)
    if(t < 10):
        password = password + ("0" + str(t))
    else:
        password = password + str(t)
    
    return (password)