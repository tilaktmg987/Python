# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

d= {
    "namesta": "hello",
    "kasari": "how",
    "kaha": "where"
}
user=input("enter for translation:")
print(d.get(user)) #or print(d[user])