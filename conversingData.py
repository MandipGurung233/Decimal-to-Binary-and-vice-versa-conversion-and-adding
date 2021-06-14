## This file convert decimal number into binary and vise_versa
## decToBined - convert decimal number into binary form
## binToDeced - convert binary number into decimal form


def decToBined(out1):
    
    c = ["0","0","0","0","0","0","0","0"]
    i = 7
    while ( int(out1) > 0):
        r = int(out1) % 2
        c[i] = str(r)
        i = i - 1
        out1 = int(int(out1) / 2)
        
    d = []
    for i in range (0,len(c)):
        d.append(int(c[i]))
    return d ## in int format
    




def binToDeced(a):
    totals = 0
    i = 0
    for j in range (7,-1,-1):
        k = (a[j])*(2**i)
        totals = totals + k
        i = i + 1

    return totals ## in int format




