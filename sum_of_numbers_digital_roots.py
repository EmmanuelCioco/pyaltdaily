#adding the numbers completely to a single number
def sum_of_digits():
    number1=124567
    #First of all i assign a number called variable one alot of variable conversion from sring to interge and vice verser
    number=str(number1)
    #we convert the number to a string value
    #we declare the sum zero as no calculation has been performed
    sum=0
    for i in number:
        #this for loop its main purpose is to run the first sum of the assigned number
        sum=sum+int(i)
    #from here we already know what the sum is so we assign another variable called sum1
    # which will check if the sum is a single digit
    sum1=str(sum)
    if len(sum1) > 1:
        #if sum has more than one digit it go to this root
        # a need is there to find a new sum of the digit hence
        # the starting sum will be declared as zero again
        sum = 0
        def recuring(sum1):#note that at this point the keyword argument sum1 is very important
            #this function is for the unknown number of times that the code below will be repeated
            sum = 0
            for i in sum1:
                #Actually this for loop will repeat the order of the first for loop
                sum = sum + int(i)
            #once again the loop is about to repeat
            #at this point it is important to declare sum1 variable again
            sum1=str(sum)
            if len(sum1) > 1:
                #this validation checking  is important as the first one
                #the next line of code is call the calling of the function this is some sort such as recurring
                #the main thing here is making sure that the keyword argument is placed purposefully
                recuring(sum1)
            else:
                #this will be possible if only one digit is remaining
                print(sum)
                #the print statement will come after all recurring has taken place
        recuring(sum1)
        #note that the above calling of the function is actually the first time
    else:
        print(sum)
sum_of_digits()