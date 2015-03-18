from Recipe import Recipe
from Tools import Tools
from PrimaryMethods import PrimaryMethods
from OtherMethods import OtherMethods
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
  rec = Recipe(rec)
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

def ti_get_link():
  print "Welcome to the Recipe Transformer!"
  link = raw_input("Please enter the full AllRecipes.com link of your recipe: ")
  #try:
  rec = Recipe(link)
  tools = Tools(link)
    
  ti_transform(rec, tools)
  #except:
  #  print "Oops, there was a slight issue. Try again!"
  #  ti_get_link()
  

def ti_transform(recipe, tools):
  print "What transformation would you like?"
  print "---------------"
  print "1. Change recipe to low sodium"
  print "2. Change recipe to low glycemic index"
  print "3. Change recipe to vegetarian"
  print "4. Change recipe to pescetarian"
  print "5. Change to Asian"
  print "6. Change to Italian"
  print "7. Show recipe information"
  print "---------------"
  transform_input = raw_input("Enter your selection: ")
  if transform_input == "1":
    print recipe.transform(sod_transform, "low_sod")
  elif transform_input == "2":
    print recipe.transform(gi_transform, "low_gi")
  elif transform_input == "3":
    print recipe.transform(veg_transform, "veg")
  elif transform_input == "4":
    print recipe.transform(pesc_transform, "pesc")
  elif transform_input == "5":
    print recipe.transform(asi_transform, "asi")
  elif transform_input == "6":
    print recipe.transform(ita_transform, "ita")
  elif transform_input == "7":
    print recipe.print_recipe_information()
    print tools.print_tools()
  print recipe.print_directions()
  print recipe.print_ingredient_transforms()

def main():
  rec = Recipe("http://allrecipes.com/Recipe/Easy-Garlic-Broiled-Chicken/")
  tools = Tools(rec.link)
  csv_setup()
  ti_get_link()

  #print rec.find_quantities()
  #print rec.find_quantity_values()
  #print rec.find_preparation()
  #print rec.find_descriptors()
  #print rec.find_measurements()
  #print rec.find_ingredients()
  #print rec.find_directions()
  #print rec.transform(gi_transform,'low_gi')
  #print rec.transform(sod_transform,'low_sod')
  #print rec.transform(veg_transform,'veg')
  #print rec.transform(pesc_transform,'pesc')
  #print rec.transform(ita_transform,'ita')
  #print rec.transform(asi_transform,'asi')
  print create_json("http://allrecipes.com/Recipe/Easy-Garlic-Broiled-Chicken/")

if __name__ == '__main__':
  main()

