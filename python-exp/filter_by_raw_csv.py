import csv
list_of_cool_facts = []
with open('cool_csv.csv') as cool_csv_file :
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    list_of_cool_facts.append(row["Cool Fact"])
print (list_of_cool_facts)


