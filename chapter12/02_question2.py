# Write a program to print third, fifth and seventh element from a list using enumerate
# function

list=["apple","banana","graves","egg","pen","gun","ball"]

for i, item in enumerate(list):
    if i==2 or i==4 or i==6:
        print(item)