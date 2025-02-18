def inter():
    amount = 100  # Initial amount
    days = 90  # Number of days
    day=0
    import math as m
    for day in range(1, days + 1):
        day+=1
        amount*= 1.1  # Apply 1.2x growth
        amount=m.floor(amount)  # Rounding to make the interest appealing (the float numbers are insignificant)
        print(f"The amount for day {day-1} is {amount}")
        print("")
        if (day-1)%5==0:
            print("*********************************")
    print(f"The total expected amount for {days} days is {amount}")
inter()