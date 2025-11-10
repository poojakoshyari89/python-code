#write a python to assign your name to a variable and print it.
name="Pooja"
print("My name is:",'Pooja')
print("-----------------------------------------------")


#Assign vallues of different data types(int,float,string,boolean)to variables and print their types.
a=10
b=5.5
c="Hello word"
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print("--------------------------------------------------------")

#take a no as input and  print wheater it is positive, -,0
num=float(input("enter a no:"))
if num>0:
    print("positive no")
elif num<0:
    print("negative no")
else:
    print("invelid no")
print("---------------------------------------------------")

#concatenate two strings and peint the result
first="Hello"
second="World"
result=first+""+second
print(result)
print("---------------------------------------")

#swap two variables using a temporary variables.
a=5
b=10
temp=a
a=b
b=temp
print("after swapping:")
print("a=",a)
print("b=",b)
print("------------------------------------")

#Write a program to calculate the square of a no
num=float(input("enter a no:"))
square=num**2
print("square of",num,"is",square)
print("-------------------------------------------------")

#convert a string into an integer and vice versa.
#string to integer
num_str="123"
num_int=int(num_str)
print("Integer:",num_int)
print("_-------------------------------------")

#integer to string
num=456
str_num=str(num)
print("String:",str_num)
print("---------------------------------------")

#assign multiple values to multiple varibles and print them.
x,y,z=10,20,30
print("x=",x)
print("y=",y)
print("z=",z)
print("-----------------------------------")

#Take input for name and age and print a message with both.


