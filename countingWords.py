name = input("enter your details: ")
print(name)

letters = 0
words = 1

for i in name :
    letters = letters+1
    if(i == " "):
        words = words+1    

print("number of words :")
print(words)
print("numbers of letters: ")
print(letters)