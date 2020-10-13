#Write your function here
def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2): # start index from first element with the range 1 - len(lst) with and incemental 2
    new_lst.append(lst[index]) # join lists with new_list.append(joined_lists[index]) 
  return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
