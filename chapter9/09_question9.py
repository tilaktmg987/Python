# Write a program to find out whether a file is identical & matches the content of
# another file.

with open("this.txt")as f:
    content=f.readlines()

with open("this_copy.txt")as f:
    A_content=f.readlines()

if(content==A_content):
    print("yes the contents are same")
else:
    print("no the contents are not same")