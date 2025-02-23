#asigning a string down below
string="todaytodayrayan"
#creating a list from the string
list1=[]
for i in string:
    #assigning each character into an element in the new list and adding it to the list
    list1.append(i)
#From here stay with me keenly
#k is asigned as 0 we will use and will be key important to
k=0
for i in list1:
    count = 0
    #the counter for each element in the  list will begin as 0
    for j in list1:
        #this inner for loop checks if the element is repeated a couple of times
        if j == list1[k]:
            #this if statement aim is to count how many times the element has appeared
           count += 1
    k += 1
    #this k here is an increament for the element that is checked above in the if statement
    counter=count
    print("'"+i+"'"+":"+str(counter))