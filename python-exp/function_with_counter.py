def divisible_by_ten(nums): # declare funtion with a parameter
  count = 0 # set start value for counter
  for number in nums: # loop through exp: for element in parameter
    if (number % 10 == 0): # condition to break the loop 
      count += 1 # add to counter to keep track of printed numbers
  return count

