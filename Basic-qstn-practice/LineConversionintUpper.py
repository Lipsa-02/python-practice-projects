#program for accepting a line of text and convert into upper case
line=input("Enter line of text:")
lc=""
for ch in line:
    if (ord(ch) in range(97,123)):
        lc=lc+chr(ord(ch)-32)
    if (ord(ch) in range(65,91)):
        lc=lc+ch
    if (ord(ch) in range(32,65)):
        lc=lc+ch
else:
    print("given text line:{}".format(line))
    print("upper case text:{}".format(lc))