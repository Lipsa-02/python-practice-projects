#Program for Demonstrating continue statement.
s="PYTHON"
print("by using while loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("i am from else part of while loop")
#My Req to display   PYTHN
print("By using while Loop")
i=0
while(i<len(s)):
    if(s[i]=="O"):
        i=i+1
        continue
    print("{}".format(s[i]),end="")
    i=i+1
else:
    print()
    print("i am from else part of while loop")