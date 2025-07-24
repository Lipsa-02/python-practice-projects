v = input("Enter any value: ")

if v.isdigit():
    res = "a digit"
elif v.isalpha():
    res = "an alphabet"
else:
    res = "a special character"

print("{} is {}".format(v, res))


