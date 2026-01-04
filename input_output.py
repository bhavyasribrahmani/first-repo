# input statements:

# Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello , " + name + "! You are", age, "years old.")
number = input()
number2 = int(number)
print(type(number2))
a = input("what are you willing to do now : ")
b = input("all should attend the event tommorow : ")
c = int(input("all candidates: "))
print("listen every one " + a + " i think its clear " + b + " see you all in event")
t = [1,2,3,4]
print(*t)
a = int(input("give a value: "))
b = int(input("give b value: "))
print(a,b,a,b,sep=",",end='.')
c = input()
print("Hello",c,sep=",",end="!")
r = input()
print("You entered",r,sep=":")
f = input()
print("You entered:",f,sep="")
# example 2
f = float(input())
print("Value of pi:",f,sep="")
# example 3
#b = input()
x,y,z = b.split(" ")
sum = int(x) + int(y) + int(z)
print(sum)
# example 4
a = input("name:")
b = int(input("age:"))
print("Name:",a,",Age:",b,sep="")
# example 5
inp = input("Enter name and age: ")
name,age = inp.split(" ")
print("Name:",name,",Age:",age,sep=(""))
vft = input()
print("Coundown:",vft," 4 3 2 1 Blast off",sep=(""),end=("!"))
# example 7
a = input()
p,q = a.split(" ")
d = int(p) + int(q)
e = int(p) - int(q)
f = int(p)*int(q)
g = float(int(p) / int(q))
print("Addition:",d,", Subtraction:",e,", Multiplication:",f,", Division:",g,sep="")
# example 7
a,b = input().split(" ")
print("Addition:"int(a)+int(b),",Subtraction:",int(a)-int(b),",Multiplication:",a*b,",Division:",float(a/b),sep=(""))
# example 8
a = 10
b = 5
print(a>b)
# example 11
a = input("name:")
b = int(input("age:"))
print("Name:",a,",Age:",b,"years",sep=(""))
# example 11 using f - springs
x,y = input("Enter name and age:").split(",")
print(f"Name:{x},Age:{y} years")
weather = input()
if weather == "sunny":
  print("you can play with your favorite toy!")
  print("dont go out")
print("Have fun!")
weather = input("Give weather:")
if weather == "sunny":
   print("cricket!")
elif weather == "rainy":
   print("play a indoor game")
else:
   print("Robots")
print("coding is ended here!!!")
num1 = int(input("give 1st number:"))
num2 = int(input("give 2nd number:"))
operator = input("Give operator:")

if operator == "+":
    print(f"Addition of 2 numbers is {num1+num2}")
elif operator == "-":
    print(f"Subtration of 2 numbers is {num1-num2}")
elif operator == "*":
    print(f"Multiplication of 2 numbers is {num1*num2}")
elif operator == "/":
    print(f"Division of 2 numbers is {num1/num2}")
elif operator == "%":
    print(f"Percentage of 2 numbers is {num1%num2}")
elif operator == "**":
    print(f"Power value is {num1**num2}")
else:
    print("Invalid operator")
