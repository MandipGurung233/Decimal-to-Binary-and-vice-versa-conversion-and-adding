## addingData is for adding either decimal or byte number
## addByteNumber - add two byte umber using bit-wise operator
## addDecimalNumber - add two decimal number

def addByteNumber(a,b):
 c = [0,0,0,0,0,0,0,0]
 c_in = 0
 n = 7
 for i in range(len(a)-1,-1,-1): 
     sum = c_in ^ (a[i] ^ b[i])
     c[n] = sum
     n = n - 1
     c_out = (a[i] & b[i]) | ((a[i] ^ b[i]) & c_in)
     c_in = c_out

 return c ## return in int form



def addDecimalNumber(out5,out6):
     summed = out5 + out6
     return summed ## return in int form
