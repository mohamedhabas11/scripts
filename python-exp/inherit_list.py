class SortedList(list): # define class and use built in type() list []
  def append(self, value): # function inherits type list and sets up value 
    super().append(value)  # override object  and append as if you do a list 
    self.sort()            # self = value and we are using method in list object
