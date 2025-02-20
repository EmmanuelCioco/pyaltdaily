from django.template.defaultfilters import wordcount, capfirst

try:
    createdfile = open('creativity.txt', 'x')
except FileExistsError:
    createdfile = open('creativity.txt', 'w+')
createdfile.write('this is the plan for the entire year\n')
createdfile.write('It feels so nice having being here\n'
                  ' I feel obliged to be hope you do so\n')
createdfile.writelines(['Hey there this is awesome\n',
                        'i want to transfer various of lines\n'
                        ,'Finally i appreciate you for being here\n'])
createdfile = open('creativity.txt', 'r')
content=createdfile.read()
wordcounter=0
for i in content:
    if i==' ' or i==capfirst(i):#supposed to count the space between them and the beginning of a new line
        wordcounter+=1
wordcounter-=4#these are for removing the counted caps letters
print(f"The number of words in the file text is {wordcounter} words")