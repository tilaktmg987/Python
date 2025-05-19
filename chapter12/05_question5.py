# . Store the multiplication tables generated in problem 3 in a file named Tables.txt.


list=[1,2,3,4,5,6,7,8,9,10]
n=int(input("enter any number:"))

list1=[n*item for item in list]

with open("chapter12/table.txt ","a")as f:
    f.write(f"table of {n}={str(list1)}\n")