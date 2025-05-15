# Write a python function to remove a given word from a list ad strip it at the same
# time.

def remove(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

list =[ "tilak","roshan", "ravi","sahil","an"]

print(f"removed:{remove(list,"an")}")
