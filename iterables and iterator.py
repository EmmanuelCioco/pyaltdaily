#this is 4th feb 2025
# an iterable is an object that is capable of returning its members one at a time, permitting it to be iterated
# over in a for-loop
# an iterator is an object that contains a countable number
list1=[1,2,3]
def for_loop():#this is a proof that a list is an itterable object in the loop below
    for items in list1:
        print(items)
for_loop()
def foor_loooop():# this fuctions profs that the list 1 is not an iterator for one
    # object can not be passed over another in other words next value of the list element
    # cannot be easily accessed with calling with the next function
    # the eror got is TypeError: 'int' object is not an iterator
    for items in list1:
        print(next(items))
#we can make the list an iterator
list2=iter(list1)
def four_loop():#this is a proof that a list is an itterable object in the loop below
    while True:
        try:
            print(next(list2))
        except StopIteration:
               break
four_loop()
