#Program for Demonstrating the Need of break Keyword
s="MISSISSIPPI"
for ch in s:
    print("\t{}".format(ch))
else:
    print("---------------------------------------")
#My Req is to display  MISS without using Indexing and Slicing
ictr=0
for i in s:
    if(i=="I"):
        ictr=ictr+1
        if(ictr==2):
            break
    print("{}".format(i))