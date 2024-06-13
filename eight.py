#write a program to check the last digit of the number is divisible by 3 or not

num=int(input("enter the number"))
lastdigit=num%10
print("the last digit of the number is", lastdigit)

if lastdigit%3==0:
    print("the last digit is divisibe by 3")
else:
    print("the last digit is not divisibe by 3")

