def printRhombus(a, b=1, *symbols):
    m = int((a - 1) / 2)
    for sym in symbols:
        for i in range(0,m+1):
            print(" "*(m-i),end="")
            for i1 in range(i,i+1):
                if i1==0:
                    print(sym)
                else:
                    if b+b<2*i1+1:
                        print(sym*b,end="")
                        print(" "*(2*(i1-b)+1),end="")
                        print(sym*b)
                    else:
                        print(sym*(2*i1+1))

        for j in range(0,m):
            print(" "*(j+1),end="")
            for j1 in range(j,j+1):
                if j1==m-1:
                    print(sym)
                else:
                    if b+b<2*(m-j1)-1:
                        print(sym*b,end="")
                        print(" "*(2*(m-j1-b)-1),end="")
                        print(sym*b)
                    else:
                        print(sym*(2*(m-j1)-1))
        print("")

printRhombus(11, 3, "&","?")

