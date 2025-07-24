#program for accepting a digit and display it's name
dicobj={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
dig=int(input("enter any digit:"))#1,2,3,4,5,6,7,8,9
res=dicobj.get(dig) if dicobj.get(dig)!= None else "+ve NUMBER " if dig>0\
    else "-VE NUMBER "
print("{} is {} ".format(dig,res))