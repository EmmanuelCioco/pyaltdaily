import random
while True:
    userchoice=input("How many dies do you want roll ")
    list1=[]
    for i in range(userchoice):
        x=random.randint(1,7)
        list1=list1.append(x)
    for i in list1:
        print(f"you rolled {i}")
    cont=int(input("press 1 to continue press 2 to exit"))
    if cont==1:
        continue
    else:
        break