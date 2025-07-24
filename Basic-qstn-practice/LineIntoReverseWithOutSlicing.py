#Program for accepting a Line of Text and d Reverse It without using Extended Slicing
line=input("enter line of text:")
rs=""
for i in range(len(line)-1,-1,-1):
    rs=rs+line[i]
else:
    print("given line:{}".format(line))
    print("reversed line text:{}".format(rs))