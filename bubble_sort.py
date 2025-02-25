array=[7,3,4,5,6,7,9,10]
c=0
while True:
    try:
        m=array[c]
        n=array[c+1]
    except IndexError:
        break
    if m>n:
        K=m
        m=n
        array[c]=m
        n=K
        array[c+1]=n
        print(array)
    c+=1
