# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  """
  count = 0
  if n > 0 and n < 3:
    return 0
  for i in range(0,n):
    if i % 3 == 0 and n != 0:
      count = count + 1
  """
  multiple = "0"
  max = 0
  dict = {"0":0, "3":0, "6":0, "9":0}
  for i in range(0, len(n)):
    dict[n[i]] = dict[n[i]] + 1
  for key in dict:
    if dict[key] > max:
      max = dict[key]
      multiple = key
  return int(multiple)


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  """
  maxIndex = 0
  count = 0
  counts = []
  for i in range(0,len(s)-1):
    #count = 0
    if s[i] == s[i+1]:
      count = count + 1
    else:
      count = 0
    counts.append(count)
  maxIndex = counts.index(max(counts))
  return s[maxIndex]
  """
  max = 0
  list = []
  counts = {}
  for char in s:
      counts[char] = 0
  for i in range(0,len(s)-1):
    if s[i] == s[i+1]:
      counts[s[i]] = counts[s[i]] + 1
  for value in counts.values():
    if value > max:
      max = value
  for key in counts:
    if counts[key] == max:
      list.append(key)
  return list

# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  s = s.replace(" ","")
  s = s.upper()
  i = 0
  matches = 0
  for i in range(0, len(s)//2):
    if s[i] == s[len(s)-1-i]:
      matches = matches + 1
  if matches == len(s)//2:
    return True
  return False
