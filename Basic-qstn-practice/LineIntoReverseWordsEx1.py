#Program for accepting a Line of Text and display Word Reverse
line=input("enter line of text:")
print("given line\n{}".format(line))
word=line.split()
for index in range(len(word)):
    word[index]=word[index][::-1]
print("".join(word))