#write aprogram to accept percentage from the user and disply the grade according to the fallowing  criteria
#>90 grade A
#>80and<=90 gradeB
#>60 and <=80 gradeC
#below 60 grade D

marks=float(input("enter the percentage"))
if marks>90:
    print("grade A")
if marks>80<=90:
    print("grade B")
if marks>60<=80:
    print("grade C")
else:
    print("grade D")

