## The code runs in modular way where code are coded in different file as function and the required functions are sequentially imported in this mainFile. In here total
## five files are present
## - userChoiceData
## - validatingData
## - conversingData
## - addingData
## - mainFiles
## Firstly functions from userChoiceData file are imported sequentially as per required and then value is passed to required function imported from  validatingData
## file for handling error after that values are converted to either decimal or binary as per required by importing required functions from conversingData file and
## then finally to addingData 

loop = False
while (not loop):
    print ("Thanks a lot for using this conversion APP !!!")
    print ("Let's convert your number right away :)...")

    loop1 = False
    while (not loop1):
     from userChoiceData import input1
     out1 = input1()
     from validatingData import validatingInput1
     out2 = validatingInput1(out1)
     print (out2)
     if out1 in ["B","D","b","d"]:
         loop1 = True

    if out1 in ["B","b"]:
        
      flag = False
      while (not flag):
        loop2 = False
        while (not loop2):
            from userChoiceData import value1
            out3 = value1() ## out3 is the first binary number in string format
            from validatingData import validatingBinary
            out4 = validatingBinary(out3)
            print (out4)
            if (out4 == "Thank you for correct value.."):
                loop2 = True
        a = []
        for i in list (out3):
            a.append (int(i))
            
        from conversingData import binToDeced
        out5 = binToDeced(a) ## out5 is the decimal form of first byte number entered in int format

        loop3 = False
        while (not loop3):
            from userChoiceData import value2
            out3 = value2() ## this is the second binary number in string format
            from validatingData import validatingBinary
            out4 = validatingBinary(out3)
            print (out4)
            if (out4 == "Thank you for correct value.."):
                loop3 = True
        b = []
        for i in list (out3):
            b.append (int(i))

        from conversingData import binToDeced
        out6 = binToDeced(b) ## out6 is the decimal form of second byte number entered in int format 
        summed = out5 + out6
        if summed < 255:
            flag = True
        elif summed == 255:
            flag = True
        else:
            print ("Error...sum of decimal form of two byte number exceeded 255")


      from addingData import addByteNumber
      out7 = addByteNumber(a,b) ## out7 is the total sum of two byte number in int format

      from addingData import addDecimalNumber
      out8 = addDecimalNumber(out5,out6) ## out8 is the total sum of two decimal number which is the converted form of two byte number entered in int format
 
      print ("Your first byte number is     ",a)
      print ("your second byte number is    ",b)
      print ("The sum of two byte number is ",out7)
      print ("Your Decimal form of first byte number is  ",out5)
      print ("Your Decimal form of second byte number is ",out6)
      print ("The total sum of of two decimal number is  ",out8)

    else:
        
        loop1 = False
        while (not loop1):

            loop2 = False
            while (not loop2):

                from userChoiceData import value3
                out1 = value3()  ## decimal number in string form
                from validatingData import validatingDecimal
                out2 = validatingDecimal(out1)
                print (out2)
                if (out2 == "Thank you for correct value.."):
                 loop2 = True

            from conversingData import decToBined
            out3 = decToBined(out1) ## binary form of first decimal number in int form
            

            loop3 = False
            while (not loop3):

                from userChoiceData import value4
                out1s = value4()  ## decimal number in string form
                from validatingData import validatingDecimal
                out2 = validatingDecimal(out1s)
                print (out2)
                if (out2 == "Thank you for correct value.."):
                 loop3 = True

            from conversingData import decToBined
            out4 = decToBined(out1s) ## binary form of second decimal number in int form
            if ( int(out1) + int(out1s) ) < 255:
               loop1 = True
            elif ( int(out1) + int(out1s) ) == 255:
               loop1 = True
            else:
               print ("Error...sum of two decimal number more than 255") 
            
        from addingData import addDecimalNumber
        out5 = addDecimalNumber(int(out1),int(out1s)) ##sum of two decimal number in int form
        from addingData import addByteNumber
        out6 = addByteNumber(out3,out4) ## sum of two byte number in int form
        print ("Your first decimal number is                 ",out1)
        print ("Your second decimal number is                ",out1s)
        print ("The  sum formed of two decimal number is     ",out5)
        print ("Byte number form of first decimal number is  ",out3)
        print ("Byte number form of second decimal number-is ",out4)
        print ("The summed form of two byte number is        ",out6)
       

    looped = False
    while (not looped):
     u_s_e_r = input("You wanna continue press y/Y or just press n/N to exit...")
     from validatingData import validating
     out__put = validating(u_s_e_r)
     print (out__put)
     if u_s_e_r in ["y","Y","n","N"]:
      looped = True
     
    if u_s_e_r in ["n","N"]:
     loop = True
     print ("THANK YOU FOR BEING WITH US :)")

   
                  
                
            

















      
      
      
