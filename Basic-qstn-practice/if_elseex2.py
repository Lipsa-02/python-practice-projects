#program for accepting Value and Decide whether It is Palindrome or Not
s=input("enter value:")
if (s==s[::-1]):
    print("{} is palindrome".format(s))
else:
    print("not palindrome")
