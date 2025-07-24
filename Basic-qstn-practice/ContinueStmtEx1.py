#Program for Demonstrating continue statement.
s="PYTHON"
print("by using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("from else part of for loop")
print("-------------------------------------------")
#My Req to display   PYTHN
print("By using for Loop")
for ch in s:
    if (ch=="O"):
        continue
    print("{}".format(ch),end="")
else:
    print()
    print("i am from else part of for loop")