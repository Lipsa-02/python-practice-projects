#program to convert temperature
#Fahrenheit to celsius
f=float(input("enter temperature:"))
c=(f-32)*(5/9)
print("temperature in celsius({})={}".format(f,c))
print("*"*50)
#fahrenheit to kelvin
f=float(input("enter temperature:"))
k=(f-32)*(5/9)+273.15
print("temperature in kelvin({})={}".format(f,k))
print("="*50)
#celsius to fahrenheit
c=float(input("enter temperature:"))
f=c*(9/5)+32
print("temperature in fahrenheit({})={}".format(c,f))
print("*"*50)
#celsius to kelvin
c=float(input("enter temperature:"))
k=c+273.15
print("temperature in kelvin({})={}".format(c,k))
print("="*50)
#kelvin to fahrenheit
k=float(input("enter temperature:"))
f=(k-273.15) *(9/5) + 32
print("temperature in fahrenheit({})={}".format(k,f))
print("*"*50)
#kelvin to celsius
k=float(input("enter temperature:"))
c=(k-273.15)
print("temperature in celsius({})={}".format(k,c))
print("="*50)
