vowels=['A','E','I','O','U','a','e','i','o','u']
string="Today is a great day"
number_of_vowels=0
for i in string:
    for j in vowels:
        if j==i:
            number_of_vowels+=1

print(number_of_vowels)