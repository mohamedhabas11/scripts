# Write your every_other_letter function here:
def every_other_letter(word):
  every_other = ""                               #create an empty string 
  for i in range(0, len(word), 2):               # i is for index which starts in 0 (meaning first letter) until the end of Word with a +2 
    every_other += word[i]                       # incrament and adding the letters to our empty string every_other = ""
  return every_other

# Uncomment these function calls to test your tip function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 
