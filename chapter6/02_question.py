# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.


sub1=int(input("enter first subject marks:"))
sub2=int(input("enter second subject marks:"))
sub3=int(input("enter third subject marks:"))

total=sub1+sub2+sub3
percentage=total/3

if(sub1>=33 and sub2>=33 and sub3>=33 and percentage>=40):
    print("pass")
else:
    print("fail")