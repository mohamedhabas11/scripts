letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  uniques = 0 # acts like a counter
  for letter in letters: # loop through letters 
    if letter in word:   # use in to mimic find() behavior because this is a list and it will give an error 
      uniques += 1       # add if matches
  return uniques

# Uncomment these function calls to test your tip function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
