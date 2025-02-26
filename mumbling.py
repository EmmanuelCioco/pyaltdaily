string="lalala"
count=1
str=""
for i in string:
    me=i*count
    me=me.capitalize()
    str=str+me+"-"
    count+=1
str=str[:-1]
print(str)
