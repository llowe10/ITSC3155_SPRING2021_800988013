# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.

# Part A. count_char
# Define a function count_char(s, char) that takes a string and a character
# and returns the number of times the given character appears in the string
def count_char(s, char):
    count = 0
    for i in range(0,len(s)):
        if (s[i] == char ):
            count=count+1
    return count

# Part B. is_power_of
# Define a function is_power_of(i,j) that takes 2 ints i and j
# and checks if i is a power of j or not
# the function should return True indicating that i is a power of j
# otherwise return False

def is_power_of(i,j):
    if(i == j):
        return True
    it = 0
    k = abs(j)
    for it in range(it,k):
        if (i**it == j):
            return True
        it = it+1
    return False

# Part C. longest_word
# Define a function longest_word(s) that takes a string s
# where s is a sentence made up of words separated by a single space " "
# and returns the longest word in this sentence
# if 2 or more words are tied as longest then return the one that occurs LAST in the sentence
# if s is an empty string return an empty string
def longest_word(s):
    longest = ""
    if s == "":
        return ""
    else:
        words = s.split(' ')
        for i in range(0,len(words)):
            if len(words[i]) >= len(longest):
                longest = words[i]
    return longest