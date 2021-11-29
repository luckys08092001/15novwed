#2. Perform Following on Python Shell Window

print(5**9)

print(3//2)

print(7//3)

print(7/3)

print(6 == 6)

a = 20; a+= 30; a%=3;
print(a)


print(True * False
)

print(True & False
)

print(True and False)

print(((6>3) and (7<4) or (18==3)) and (9>3))

print(True is False)

# print(False in 'False')  --> This shows an error

print(((True == False) or (False > True)) and (False <= True))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#3. Try to get following output from two python strings

s1 = "Nice to have it"
s2 = "here"
s3 = s1 + ' ' + s2
print(s3)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#4. Given this nested list, use indexing to grab the word "hello"

a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

print(a[3][1][2][0])

#----------------------------------------------------------------------------------------------------------------------------------------------------------


#5. Try to insert above strings s1 and s2 in the list ‘a’ mentioned in que 4, in the beginning and end of it respectively

a.insert(0,s1)
a.append(s2)
print(a)

#----------------------------------------------------------------------------------------------------------------------------------------------------------


#6. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 inthe sequence. 

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]

for i in numbers:
    if(i==237):
        break
    elif(i%2==0):
        print(i)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
        

#7. Write a Python program to print out a set containing all the colours from color_list_1 which are not present in color_list_2.

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
print(color_list_1 - color_list_2)


#----------------------------------------------------------------------------------------------------------------------------------------------------------


#8. WAP to find if the given input string is Pangram or not

string = input("Enter the string")
string = set(string)
alpha = list('abcdefghijklmnopqrstuvwxyz')
i=0
for word in string:
    if(word in alpha):
        i+=1
if(i==26):
    print('String is Pangram')
else:
    print('String is not Pangram')


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#9. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
# Sample value of n is 5

n=(input('Enter a Number: '))
num1=n
num2=n*2
num3=n*3
print(int(num1)+int(num2)+int(num3))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#10. Write a python program to take input from console in following fashion 23 54 12#98 3 17 and generate the corresponding two list having integers inside(not string)

string1=eval(input("Enter string in the given fashion"))     # "23 54 12#98 3 17"
string1=string1.strip()
string1+=" "
num=""
x=[]
y=[]
flag=0
for i in string1:
    if(i!=" "):
        if(i!="#"):
            num+=i
        else:
            flag=1
            x.append(int(num))
            num=""
    
    else:
        if(flag==0):
            x.append(int(num))
            num=""
        else:
            y.append(int(num))
            num=""
print(x)
print(y)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#11. Write a program that accepts a comma separated sequence of words as input and  prints the words in a comma-separated sequence after sorting them
#alphabetically.Suppose the following input is supplied to the program: without,hello,bag,world

string2=(input("enter the words"))
string2=string2.strip()
string2+=","
word=""
l=[]
for i in string2:
    if(i!=","):
        word+=i
    else:
        l.append(word)
        word=""
l.sort()
print(l)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#12. Write a Python function to find the name of person obtained highest marks in exam from given dictionary Example dictionary
#d = {‘Student’: [‘Rahul’, ‘Kishore’, ‘Vidhya’, ‘Raakhi’],‘Marks’: [57,87,67,79]}

d={'Student' : ['Rahul','Kishore','Vidhya','Raakhi'],'Marks' : [57,87,67,79]}
maximum=0
idx=-1
for i in d['Marks']:
    idx+=1
    if(maximum<i):
        maximum=i
        pos=idx
print(d['Student'][pos])


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#13. Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:hello world! 123 Then,

string3=(input("enter the sentence"))
letters=0
digits=0
for i in string3:
    if(i.isalpha()):
        letters+=1
    if(i.isdigit()):
        digits+=1
print("LETTERS",letters)
print("DIGITS",digits)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#14. Write a python function which creates a new dictionary of students from a given Dataset of various subject to a specific subject or topic only.
#Example Data:d = {‘Name’: [‘Akash’, ‘Soniya’, ‘Vishakha’ , ‘Akshay’, ‘Rahul’, ‘Vikas’],‘Subject’: [‘Python’, ‘Java’, ‘Python’, ‘C’, ‘Python’, ‘Java’],‘Ratings’: [8.4, 7.8, 8, 9, 8.2, 5.6]}

d={'Name':['Akash','Soniya','Vishakha','Akshay','Rahul','Vikas'],
   'Subject':['Python','Java','Python','C','Python','Java'],
   'Ratings':[8.4,7.8,8,9,8.2,5.6]}
inp=input("enter subject name")
idx=-1
pos=[]
for i in d['Subject']:
    idx+=1
    if(inp==i):
        pos.append(idx)
newData={'Name':[],'Subject':[],'Ratings':[]}
for i in pos:
    newData['Name'].append(d['Name'][i])
    newData['Subject'].append(d['Subject'][i])
    newData['Ratings'].append(d['Ratings'][i])
    
print(newData)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


##16. A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot 
#movement is shown as the following:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#The numbers after the direction are steps. Please write a program to compute the 
#distance from current position after a sequence of movement and original point. 
#If the distance is a float, then just print the nearest integer.


x=0
y=0
while(True):
    string4=(input("enter the instructions"))
    if (string4 == ""):
        break
    else:
        string4=string4.split(' ')
        if string4[0]=="UP":
            y+=int(string4[1])
        elif string4[0]=="DOWN":
            y-=int(string4[1])
        elif string4[0]=="RIGHT":
            x+=int(string4[1])
        elif string4[0]=="LEFT":
            x-=int(string4[1])
dist=(((x**2)+(y**2))**(1/2))
print('DISTANCE:',int(dist))
