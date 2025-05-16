# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file. 

with open("word.txt", "r") as f:
    content=f.read()
    anotherC=content.replace("donkey","#####")

with open("word.txt","w") as f:
    f.write(anotherC)