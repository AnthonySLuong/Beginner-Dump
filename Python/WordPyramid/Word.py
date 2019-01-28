phrase = input("Enter your phrase: ")

for x in range(len(phrase)):
    if phrase[x] != ' ':
        print(phrase[0:x])
for x in range(len(phrase)):
    if phrase[len(phrase)-1-x] != ' ':
        print(phrase[0:len(phrase)-x])
