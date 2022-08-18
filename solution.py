# Hundred letters problem.

# Given a string, return the first 100 characters and full words.
# If a word would get cut off, do not include it and instead end at the last whole word.

# Ex. "a picture is worth one hundred words"
# For sake of brevity, say the space after "hundred" is character 97, and "words" is 98, 99, 100, 102, 103
# Do not include "words" in this case, because it gets cut off at the 100 index.

# Case 1: return the whole string.
case1 = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabca"

# Case 2: Return the first "word", easily spotted by the chars END.
case2 = "abcabcabcabcabcabcabcabcabcabcabcabcabcabEND       ThisPartShouldNotBeReturnedBecauseThisVeryLongWordGoesWayOver100"

# Case 3:The space after the word "algorithm" is character 99, so the word "works" would get cut off.
# This case should return up to the word "algorithm".
case3 = "I could be a passage from a story, blog, article or any other source. Make sure that the algorithm works correctly. This test case ends at the word algorithm"

# Case 4: Same as Case 3, but with more spaces.
case4 = "I could be a passage from a story, blog, article or any other source. Make sure that the algorithm                       works correctly. This test case should also end at the word algorithm."

# Case 5: A string full of blank chars.
case5 = "                    "

# Case 6: String of length 0.
case6 = ""

# Case 7: Multiple spaces.
case7 = "    some spaces    then some words   !"


# str: the string you want 100 characters from.
# Returns result as string.
def hundred_solver(str):
    print(f'\nDEBUG, original string length: {len(str)}')

    # Return if length <= 100
    if len(str) <= 100:
        return str
    
    # Other cases where length > 100.
    # Finds the proper index to slice.
    for index in range(99, -1, -1):
        if str[index] == ' ' and str[index - 1] != ' ':
            return str[0:index]
    



print(hundred_solver(case1))
print(hundred_solver(case2))
print(hundred_solver(case3))
print(hundred_solver(case4))
print(hundred_solver(case5))
print(hundred_solver(case6))
print(hundred_solver(case7))