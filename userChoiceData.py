## It has got total five function each ask user to enter value in strinf format
## input1 - ask user to enter D/d or B/b in string format
## value1 - ask user to enter byte number in string format
## value2 - ask user to enter byte number in string format
## value3 - ask user to enter decimal number in string format
## value4 - ask user to enter decimal number in string format

def input1():
    print("How you wanna proceed ??...")
    a = input("For decimal format - press D/d.. For binary format press - b/B:")
    return a

def value1():
    b = input("Enter first 8-digit byte number:")
    return b

def value2():
    b = input("Enter second 8-digit byte number:")
    return b

def value3():
    k = input ("Enter first decimal number:")
    return k

def value4():
    k = input ("Enter second decimal number:")
    return k
