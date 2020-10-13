import re
str = "We need weed"
for i in re.finditer("weed",str):
  loctup = i.span()
  print(i)

str2 = "Sat, hat , mat , pat"
allstr = re.findall("[Shmp]at",str2)
for j in allstr:
  print(j)

