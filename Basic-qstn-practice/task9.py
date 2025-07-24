#Prgram for Getting Number of 500,200 and 100 from ATM when we withdraw the amount
amount=int(input("Enter How Much Amount u withdraw:")) # amount=9300
oamt=amount
#How Many 500 Notes
no500=amount//500
#remaining amount after 500 Over
amount=amount%500
#--------------------
#How Many 200 Notes
no200=amount//200
#remaining amount after 200 Over
amount=amount%200
#How Many 100 Notes
no100=amount//100
#remaining amount after 100 Over
amount=amount%100
print("----------------------------")
print("Given Amount:{}".format(oamt)) #
print("\tNumber of 500={}".format(no500))
print("\tNumber of 200={}".format(no200))
print("\tNumber of 100={}".format(no100))