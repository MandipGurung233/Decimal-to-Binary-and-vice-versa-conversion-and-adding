## This file is for validating the entered number from the user. When user are asked to enter certain int number then they may enter string data type
## so if such cases are not handled then their may occur run-time error, hence this is the file to handle such error where there is four different function..:)



def validatingInput1 (out1): ## Asked value to user is only b,B,d,D So if user enter other than this than this function  
                             ## handle such error.....
    if out1 in [""]:
          return "Error....Empty field.."

    if out1  in ["b","D","B","d"] :
          return "Thank you for correct value.. :)"

    try:                     ## this is to handle run-time error......
          exception = int (out1)
    except:
          return "Error....Special character"
    
    if int(out1) < 0:
          return "Error....Negative value"

    for integers in out1:
        if int(integers) in [0,1,2,3,4,5,6,7,8,9]:
            return "Error....Integers value"


        

def validatingDecimal (out1): ## this function validate decimal number......

   if out1 in  [""]:
      return "Error....Empty field.."

   try:
      exception = int (out1)
   except:
      return "Error....Special character"
     
   if int(out1) < 0:
      return "Error....Negative value"
    
   if int(out1) > 255:
      return "Error....more than 255"
    
   for integers in out1:
        if int(integers) in [0,1,2,3,4,5,6,7,8,9]:
            return "Thank you for correct value.."
   




def validatingBinary (out3): ## this function validate binary number                                              

 
   if out3 in [""]:
      return ("Error...Empty field")

   try:
      exception = int (out3)
   except:
      return ("Error...Special character")

   if int(out3) < 0:
      return ("Error...Negative value")
    

   if len (out3) > 8:
      return ("Error...More than 8 digit")

   if len (out3) < 8:
      return ("Error...less than 8 digit")
   

   for integers in out3:
       if int(integers) not in [0,1]:
           return ("Error...value other than 0 and 1 found...")

   for integers in out3:
       if int(integers)  in [0,1]:
           return ("Thank you for correct value..")





def validating (u_s_e_r): ## Asked value to user is only y,Y,n,N So if user enter other than this than this function  
                          ## handle such error.....
    
    if u_s_e_r in [""]:
          return "Error...Empty field"

    if u_s_e_r  in ["Y","y","n","N"] :
          return "Thank you for correct value"

    try:
          exception = int (u_s_e_r)
    except:
          return "Error...Special character"
    
    if int(u_s_e_r) < 0:
          return "Error...Negative value"

    for digitNumeric in u_s_e_r:
        if int(digitNumeric) in [0,1,2,3,4,5,6,7,8,9]:
            return "Error....Numeric value"
        
