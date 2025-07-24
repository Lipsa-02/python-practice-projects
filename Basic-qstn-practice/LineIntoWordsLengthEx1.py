#Proigram for accepting a Line of Text and
# display them in the form of words with length and place them Dict
line=input("enter the line of text:")
print("the given line is{}".format(line))
word=line.split()
for word in word:
    print("given line in word is:{}-->{}".format(word,len(word)))
