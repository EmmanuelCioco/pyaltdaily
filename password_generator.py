import random
capital_letters=["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
small=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
char=('"!","@","#" ,"$" ,"%" ,"^" ,"&" ,"*" ,"(" ,")" ,"-" ,"_" ,"=" ,"+"  ,"|" ,"["  ,"]" ,"{" ,"}" ,";" ,":" ,"/" ,"?" ,"." ,">"')
characters=[]
for i in char:
    characters.append(i)
numbers=[1,2,3,4,5,6,7,8,9,0]
print("Welcome to password generator\n"
      "Choose an option\n"
      "1.Generate a password without special character\n"
      "2.Generate a normal password")
user_choice=int(input("your choice(1,2):  "))
print("how many characters do you want")
numb=int(input("enter the length of the password:  "))
if user_choice==1:
    def generate(numb):
        password=""
        for i in range(numb):
            X = random.choice(capital_letters)
            Y = random.choice(small)
            #Z = random.choice(characters)
            a = X + Y
            b=random.choice(a)
            password+=str(b)
        print(password)
    generate(numb)
else:
    def generate(numb):
        password=""
        for i in range(numb):
            X = random.choice(capital_letters)
            Y = random.choice(small)
            Z = random.choice(characters)
            a = X + Y +Z
            b=random.choice(a)
            password+=str(b)
        print(password)
    generate(numb)