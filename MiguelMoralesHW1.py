str = input("Please Input the String\n")

def AsciiConverter(str):
   ascii = list(bytes(str, 'ascii'))
   return ascii

def productlist(ascii):
    value = 1
    for i in ascii:
        value *= i
    return value

print(productlist(AsciiConverter(str)))
