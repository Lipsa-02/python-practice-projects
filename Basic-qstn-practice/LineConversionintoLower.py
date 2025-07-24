#program for accepting a line of text and converting into lowercase
line=input("enter your line of text:")
lc=""
for ch in line:
    if (ord(ch) in range(65,91)):
        lc=lc+chr(ord(ch)+32)
    if (ord(ch) in range(97,123)):
        lc=lc+ch
    if(ord(ch) in range(32,65)):
        lc=lc+ch
else:
    print("given line={}".format(line))
    print("Lower case data={}".format(lc))