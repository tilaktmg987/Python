# Write a program to find out the line number where python is present from ques 6.

with open("chapter9_06.txt")as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if("python" in line):
        print(f"yes python is in the list. line no:{lineno}")
        break
    lineno+=1
else:
    print("No python is not in the list.")