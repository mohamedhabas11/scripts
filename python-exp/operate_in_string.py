first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name): # define function and parameters
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:] # load string in a parameter and let parameter[len(paremeter)-X:] count until in reaches X in the index .)
  return temp_password

temp_password = password_generator(first_name, last_name)
