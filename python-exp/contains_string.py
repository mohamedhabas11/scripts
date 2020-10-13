def contains(big_string, little_string):
  return little_string in big_string # its like for but in reverse
				     # for little_string in big_string :
				     #   if ( little_string == part_big_string)
                                     # return (the logical operators result)




def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

