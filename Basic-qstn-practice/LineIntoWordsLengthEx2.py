#Proigram for accepting a Line of Text and
# display them in the form of words with length and place them Dict
line=input("enter line if text:")
print("Given line={}".format(line))
words=line.split()
print("given line into words")
d={}
for word in words:
    d[word]=len(word)
else:
    for w,wl in d.items():
        print("\t {}--->{}".format(w,wl))