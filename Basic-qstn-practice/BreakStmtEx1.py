#Program for Demonstrating the Need of break Keyword
s="PYTHON"
print("by using for loop")
for ch in s:
    print(ch)
else:
    print("i am from else part of for loop")
#My Req today is to display PYTH without using Indexing and Slicing.
print("-"*50)
for ch in s:
    if(ch=="O"):

        break
    print("{}".format(ch))
else:
    print("i am from else part of for loop")
print("other statement in program")