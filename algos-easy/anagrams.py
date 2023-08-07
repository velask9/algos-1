# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
  # first, check for strings ' length
  if (sorted(s1)== sorted(s2)):
    print(True)
  else:
    print(False)


#__________________________________________OR

#list - looking things up requires you to iterate through the whole list 0(n)
# Dict/object -> looking things up requires key (Instant) 0(1)

#def anagram(s1, s2):
#First, check each letter is S1 with a letter in s2
  # if len(s1) != len(s2):
      #return False

#Initialize a dict to hold the letter present in first string
    #count = {}
    #for char in s1:
     # if char not in count:
         #count[char] = 1
      #else:
          #count[char] += 1

     #print('count dict initialized:', count)
#Loop through second string and check each letter with the dict.
  #for char in s2:
      #if char not in count:
          #return False
      #else:
            #count[char] -= 1
            #if count[char]< 0:
                #return False

# # TEST CASES
anagrams('restful', 'fluster') # -> True
#anagrams('cats', 'tocs') # -> False
#anagrams('monkeyswrite', 'newyorktimes') # -> True
#anagrams('paper', 'reapa') # -> False
#anagrams('elbow', 'below') # -> True
#anagrams('tax', 'taxi') # -> False
#anagrams('taxi', 'tax') # -> False
#anagrams('night', 'thing') # -> True
#anagrams('po', 'popp') # -> False
#anagrams('pp', 'oo') # -> False
