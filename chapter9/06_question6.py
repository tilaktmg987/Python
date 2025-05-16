# Write a program to mine a log file and find out whether it contains ‘python’.

with open("chapter9_06.txt") as f:
    content=f.read()

if("python"in content):
    print("yes python is in this text")
else:
    print("no python is in this text")