#Program for Finding Number of Occurences of Every Letter of Word OR Line
s=input("enter the word/line:")
d=dict()
for ch in s:
    if ch not in d:
        d[ch]=1
    else:
        d[ch]=d[ch]+1 #OR d[ch]=d.get(ch)+1
else:
    for k,v in d.items():
        print("{}-->{}".format(k,v))