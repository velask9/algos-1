# Decompress

# Write a function, decompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:

# <number><char>
# for example, '2c' or '3a'.

# The function should return an decompressed version of the string where each 'char' of a group 
# is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.

def decompress(s):
    #
    decompressed = ""
    count = ""

    for char in s:
        if char.isdigit():
            count += char

        else:
            decompressed += char * int(count)
            count = ""
    return decompressed

#_________________________________________________OR

#def decompress(s):
    #newString = ""
    #factor = ""
    #subString = ""

    #for char in s:
        #if char.inumeric():
            #factor += char
        #else:
            #char.isalpha()
            #subString = (char) * int(factor)
            #newString+= subString
            #factor = ""

    #return newString

# ____________________________________________OR
#def decompress(s):
    #result = []
    #i = 0; j= 0
    #numbers = '0123456789'

    #while j < len(s):
        #if s[j] in numbers:
        #j += 1

        #else:
            ##extract number from string using the difference between i and j
            #num = int(s[i:j])

            ##mulitply the number by character -> store in result list
            # result.append(num * s[j])

            ##increment j, catch i up to j

    #return ''.join(result)




# TEST CASES
print(decompress("2c3a1t")) # -> 'ccaaat'
#print(decompress("4s2b")) # -> 'ssssbb'
#print(decompress("2p1o5p")) # -> 'ppoppppp'
#print(decompress("3n12e2z")) # -> 'nnneeeeeeeeeeeezz'
#print(decompress("127y")) # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
