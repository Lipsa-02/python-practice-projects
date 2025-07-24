#Proigram for accepting a Line of Text and display them in the form of words
line=input("enter line of text:")
print("given line is:{}".format(line))
word=line.split()
print("given line into words")
for word in word:
    print("{}".format(word))