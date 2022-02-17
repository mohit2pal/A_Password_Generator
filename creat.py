def crat(x, y, z):
    L1 = ("\n", x, "\n", y, "\n", z)
    # L2 = ( )
    # L3 = ( )
    f1 = open("1.txt", "a")
    f1.writelines(L1)
    # f1.writelines(L2)
    # f1.writelines(L3)
    f1.close()
