# Paired Parentheses

# Write a function, paired_parens, that takes in a string as an argument.
# The function should return a boolean indicating whether or not the string has well-formed parentheses.
# You may assume the string contains only alphabetic characters, '(', or ')'.


def paired_parens(string):
    count = 0
    for s in string:
        if s == "(":
            count += 1
        elif s == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0


# def paired_parens(string):
#     stack = []
#     for char in string:
#         if char == '(':
#             stack.append(char)
#         elif char == ')':
#             if len(stack) == 0:
#                 return False
#             stack.pop()
#
#     return len(stack) == 0


#def paired_parens():
    #create a counter variable
    #count = 0
    #parse string (for loop)
    #for char in string:
      #if character is an opening '(' -> increment counter
      # if char == '(':
      #     count += 1
      #if character is a closing ')'
        #elif char == ')':
            #if count > 0:  -> decrement counter ONLY if counter  > 0
                #count -= 1
            #else:
      # otherwise return false (mismatch of parenthesis
            #return False

     #






# # TEST CASES
# print(paired_parens("(david)((abby))")) # -> True
# print(paired_parens("()rose(jeff")) # -> False
# print(paired_parens(")(")) # -> False
# print(paired_parens("()")) # -> True
# print(paired_parens("(((potato())))")) # -> True
# print(paired_parens("(())(water)()")) # -> True
