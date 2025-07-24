#Program for Demonstrating the Need of break Keyword
s="PYTHON"
print("By Using while Loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("I am from else part of while loop")
#My Req today is to display PYTH without
# using Indexing and Slicing.
print("-------------------------------------------")
i=0
while(i<len(s)):
    if(s[i]=="O"):
        break
    print(s[i])
    i=i+1