#Program for Demonstrating the Need of break Keyword
s="MISSISSIPPI"
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("---------------------------------------")
#My Req is to display  MISS without using Indexing and Slicing
ictr=0
i=0
while(i<len(s)):
    if(s[i]=="I"):
        ictr=ictr+1
        if(ictr==2):
            break
    print(s[i])
    i=i+1