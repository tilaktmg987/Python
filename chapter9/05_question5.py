# Repeat program 4 for a list of such words to be censored.

words=["tilak","donkey","banana", "apple"]

with open("chapter9_05.txt") as f:
    content=f.read()

for word in words:
    content=content.replace(word, "#"*len(word))

with open("chapter9_05.txt","w") as f:
    f.write(content)