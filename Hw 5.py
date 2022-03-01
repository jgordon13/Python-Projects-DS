# Author: Julia Gordon
# Date: 2/23/2022
# Homework 5 
# Create an implementation of the Caesar cipher (ROT13) with Python. 
# The Caesar cipher is a simple shift cipher that relies on transposing all the letters in  
# the alphabet using an integer key between 0 and 26. Using a key of 0 or 26 will 
# always yield the same output due to modular arithmetic. The letter is shifted for as 
# many values as the value of the key. 
#
# function just using rot13: 
#def rot13(s):
#    output = "" #just an empty string for an output
#    chars = 'abcdefghijklmnopqrstuvwxyz' # string of characters we are using
#    encode = chars[13:] + chars[:13] #shift by 13 to encode
#    for c in s: #for the character within the string
#        if c in chars: # if the character is in the string of character we can use 
#                output = output + encode[chars.find(c)] # then we want add it to the output string after running it throught the encoder for that specific character
#        else:
#            output = output + c # this is so if we have a space for a punctuation it will remain, will work without this line.
#    return output
#print(rot13('hello'))
#print('--------')

chars = 'abcdefghijklmnopqrstuvwxyz' # string of characters we are using
#function to encrypt (the same as above just changing the name)
def encrypt(s):
    if s.isalpha(): 
        output = "" #just an empty string for an output
        encode = chars[13:] + chars[:13] #shift by 13 to encode
        for c in s.lower(): #for the character within the string
            if c in chars: # if the character is in the string of character we can use 
                output = output + encode[chars.find(c)] # then we want add it to the output string after running it throught the encoder for that specific character
            else:
                output = output + c # this is so if we have a space for a punctuation it will remain, will work without this line.
        return output
    else :
        return('The text should only contain alphabet letters ')
#print(encrypt('Testnow')) # here is where we put what we want to encrypt

#function to decrypt (very similar as above but list of characters are changed to 13 over)
def decrypt(s):
    if s.isalpha():
        output = "" #just an empty string for an output
        encode = chars[13:] + chars[:13] #shift by 13 to decode 
        for c in s.lower() : #for the character within the string
            if c in chars: # if the character is in the string of character we can use 
                output = output + encode[chars.find(c)] # then we want add it to the output string after running it throught the encoder for that specific character
            else:
                output = output + c # this is so if we have a space for a punctuation it will remain, will work without this line.
        return output
    else:
        return('The text should only contain alphabet letters ')
#print(decrypt('uryyb')) # here is where we put what we want to decrypt

val = input('enter your plain text ')
print(encrypt(val))

# might want to add a try/catch block later