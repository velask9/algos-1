# Compress

# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string where consecutive occurrences of 
# the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

# You can assume that the input only contains alphabetic characters.


def compress(s):
    count = 1
    compressed = ""

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += str(count) + s[i - 1]
            count = 1

    compressed += str(count) + s[-1]
    return compressed

#_________________________________________________________OR

#Two pointer solution
#i = 0 -> end (tracks the letter)
#j = 0 -> end (tracks occerances)

#def compress(s):
    #initialize a list to store result
    #result = []
    # i, j = 0

    #While loop to iterate thru string
    #while j < len(s):
        #if s[i] == s[j]:
           # j+= 1
        #else:
            #letter_count = j -i

            #if letter_count == 1:
                #result.append(s[i])
            #else:
                #result.append(str(letter_count))
                #result.append(s[i])
            #i = j

    #retun  ''.join(result)


# TEST CASES
#print(compress('ccaaatsss')) # -> '2c3at3s'
#print(compress('ssssbbz'))# -> '4s2bz'
#print(compress('ppoppppp')) # -> '2po5p'
#print(compress('nnneeeeeeeeeeeezz')) # -> '3n12e2z'
#print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'));  # -> '127y'
