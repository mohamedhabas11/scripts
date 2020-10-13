authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = [] #list to append the new split
for name in author_names:
  author_last_names.append(name.split()[-1]) #  it will start searching from the back and there for start with last_name and is split by the default value of split function ## leave empty for SPACES
  
print(author_last_names)
