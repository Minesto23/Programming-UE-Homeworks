""" 
Made by Miguel Ernesto Morales Molina 
Student-id = 15590763 
"""
import random # Import the module to create random numbers

str = input("Please my lord bless me with your words\n") # Ask to the user to input a String
lenh = len(str) # lenh storage the len of the string gave by the user

""" Method to convert the string gave by the user to ASCII code"""
def AsciiConverter(str):
   ascii = list(bytes(str, 'ascii')) # we convert the string to a list of its Ascii values
   return ascii # return the result of the function

""" Method to have the product of all the elements inside the list"""
def productlist(ascii):
    value = 1 # initializing the start of the product
    for i in ascii: # For loop to obtain the product from all the values
        value *= i
    return value

""" Method to generate a random number with a sedd"""
def randomG(lenh) -> int:
    random.seed(2)
    return random.randint(lenh,2000000)

""" Method do the xor operation to the list"""
def xor(random_number,str):
    return random_number ^ str

""" Method to covert a integer to a hexadecimal String and later trim the value
    for only the first 16 digits"""
def hashing(num):
    result = hex(num) # method return a hexadecimal string from an integer
    return result[:15]

result = hashing(xor(randomG(lenh),productlist(AsciiConverter(str)))) # we call all the methods needed to have the result

print(result) # finally we print the result
