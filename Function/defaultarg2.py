#Program for Demonstrating the need of default Arguments
#aefaultargs2.py
def darg(sno,sname,marks,crs="python",cnt="India"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#main program
print("\tSNO\tSNAME\tMARKS\tCOURSE\tCOUNTRY")
darg(12,"Rs",85)
darg(100,"JV",45.67) # Function call
darg(200,"TR",46.78) # Function call
darg(300,"DR",66.78) # Function call
darg(400,"JH",46.18) # Function call
darg(500,"SR",67.89) # Function call
darg(600,"DT",22.22,cnt="USA")# Function call
darg(700,"PT",32.22,cnt="RSA",crs="HTML")