from Recipe import Recipe
from Tools import Tools
from PrimaryMethods import PrimaryMethods
from OtherMethods import OtherMethods
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

  # get primary methods
  primethods = PrimaryMethods(rec.link)
  result["primary cooking method"] = primethods.find_methods()
  
  # get other methods
  othermethods = OtherMethods(rec.link)
  if result["primary cooking method"] in othermethods.find_methods():
    othermethodslist = othermethods.find_methods()
    othermethodslist.remove(result["primary cooking method"])
    result["cooking methods"] = othermethodslist
  else:
    result["cooking methods"] = othermethods.find_methods()

  # get tools
  tool = Tools(rec.link)
  result["cooking tools"] = tool.find_tools()
  return result


def main():
  rec = Recipe("http://allrecipes.com/Recipe/Chef-Johns-Lasagna/Detail.aspx?evt19=1&referringHubId=17245")
  tools = Tools(rec.link)
  csv_setup()
  # print len(rec.find_quantities())
  # print len(rec.find_quantity_values())
  # print len(rec.find_preparation())
  # print len(rec.find_descriptors())
  # print len(rec.find_measurements())
  print create_json(rec)

if __name__ == '__main__':
  main()

