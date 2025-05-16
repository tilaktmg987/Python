# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

with open("poems.txt","r") as f:
    contain=f.read()
    if("twinkle" in contain):
        print("yes it is in")
    else:
        print("no it is not there")