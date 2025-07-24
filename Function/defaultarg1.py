#Program for Demonstrating the need of default Arguments
def darg(sno,sname,marks,crs="PYTHON"):#here crs is default argument
    print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#main program
print("\tSNO\tSNAME\tMARKS\tCOURSE")
darg(100,"RS",45.67) # Function call
darg(200,"TR",46.78) # Function call
darg(300,"DR",66.78) # Function call
darg(400,"JH",46.18) # Function call
darg(500,"SR",67.89)#function call