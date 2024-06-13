#accept the age of 4 people and disply the largest one

a=int(input("enter the age of first person"))
b=int(input("enter the age of second person"))
c=int(input("enter the age of third person"))
d=int(input("enter the age of forth person"))
if a>b>c>d:
    print("a is elder than all")
if b>a>c>d:
    print("b is elder than all")
if c>d>a>b:
    print("c is elder than all")
else:
    print("d is elder than all")
