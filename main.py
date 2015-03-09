from Recipe import Recipe
import csv

gi_transform = {}
sod_transform = {}

def csv_setup():
  with open('lowgi.csv', 'rbU') as lowgi:
    reader = csv.reader(lowgi)
    for r in reader:
      gi_transform[r[0].lower()] = r[1].lower()
  with open('lowsodium.csv', 'rbU') as lowsod:
    reader = csv.reader(lowsod)
    for r in reader:
      sod_transform[r[0].lower()] = r[1].lower()


def main():
  rec = Recipe("http://allrecipes.com/Recipe/Raisin-Cake/Detail.aspx")
  csv_setup()
  print rec.find_ingredients()
  print rec.transform_gi(gi_transform)
  print rec.transform_sodium(sod_transform)
  print rec.find_preparation()
  print rec.find_descriptors()

if __name__ == '__main__':
  main()
