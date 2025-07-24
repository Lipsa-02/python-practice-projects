#program to accept any word or value and decide whether it is palindrome or not
value=input("enter  value:")
if value==value[::-1]:
    print("{} is palindrome".format(value))
if value!=value[::-1]:
    print("{} is not palindrome".format(value))