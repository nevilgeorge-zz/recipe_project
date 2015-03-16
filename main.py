from Recipe import Recipe
from Tools import Tools

import csv

gi_transform = {}
sod_transform = {}
veg_transform = {}
pesc_transform = {}
ita_transform = {}
asi_transform = {}

def csv_setup():

  ## Health Optios
  with open('lowgi.csv', 'rbU') as lowgi:
    reader = csv.reader(lowgi)
    for r in reader:
      gi_transform[r[0].lower()] = r[1].lower()
  with open('lowsodium.csv', 'rbU') as lowsod:
    reader = csv.reader(lowsod)
    for r in reader:
      sod_transform[r[0].lower()] = r[1].lower()

  ## Dietary Options
  with open('vegetarian.csv', 'rbU') as veg:
    reader = csv.reader(veg)
    for r in reader:
      veg_transform[r[0].lower()] = r[1].lower()
  with open('pescatarian.csv', 'rbU') as pesc:
    reader = csv.reader(pesc)
    for r in reader:
      pesc_transform[r[0].lower()] = r[1].lower()

  ## Culinary Style Options
  with open('italian.csv', 'rbU') as italian:
    reader = csv.reader(italian)
    for r in reader:
      ita_transform[r[0].lower()] = r[1].lower()
  with open('asian.csv', 'rbU') as asian:
    reader = csv.reader(asian)
    for r in reader:
      asi_transform[r[0].lower()] = r[1].lower()

def create_json(rec):
  result = {}
  result["ingredients"] = []
  names = rec.find_ingredient_names()
  quantities = rec.find_quantity_values()
  measurements = rec.find_measurements()
  preps = rec.find_preparation()
  descs = rec.find_descriptors()
  for i in range(len(names)):
    current = {}
    current["name"] = names[i]
    current["quantity"] = quantities[i]
    current["measurement"] = measurements[i]
    current["descriptor"] = descs[i]
    current["preparator"] = preps[i]
    result["ingredients"].append(current)

  result["primary cooking method"] = ""
  # get tools
  tool = Tools(rec.link)
  result["cooking tools"] = tool.find_tools()
  return result


def main():
  rec = Recipe("http://allrecipes.com/Recipe/Raisin-Cake/Detail.aspx")
  tools = Tools(rec.link)
  csv_setup()
  #print rec.find_quantities()
  #print rec.find_quantity_values()
  #print rec.find_preparation()
  #print rec.find_descriptors()
  #print rec.find_measurements()
  print rec.find_ingredients()
  #print rec.find_directions()
  #print rec.transform(gi_transform,'low_gi')
  #print rec.transform(sod_transform,'low_sod')
  #print rec.transform(veg_transform,'veg')
  #print rec.transform(pesc_transform,'pesc')
  #print rec.transform(ita_transform,'ita')
  #print rec.transform(asi_transform,'asi')
  #print create_json(rec)

if __name__ == '__main__':
  main()

