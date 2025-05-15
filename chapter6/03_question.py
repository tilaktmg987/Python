# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.


a= " Make a lot of money"
b= "buy now"
c= "subscribe this"
d= "click this"

comment=input("enter message: ")

if( (a in comment) or (b in comment) or (c in comment) or (d in comment)):
    print("this message is scam")
else:
    print("this message is not scam")