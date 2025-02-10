import temp_tenth_feb as temp
import random
list=[5,6,7,9,8]
def summing(list):
    sumi=0
    for i in list:
        sumi=sumi+i
    print(sumi)
#summing(list)
def fact(numer,f=1):

    if numer !=1:
        f=f * (numer)
        numer=numer-1
        fact(numer,f)
    else:
        print(f)
#fact(5)
def rand():
    x=random.randint(1,100)
    print(x)
#rand()
temp.convert(34)