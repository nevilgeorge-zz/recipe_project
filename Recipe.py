# requester.py
import requests
from bs4 import BeautifulSoup

class Recipe:

	# constructor takes in a link of a recipe from allRecipes.com
	def __init__(self, link):
		# web URL of the allRecipes link we are using in this instance of the Recipe
		self.link = link
		# list of ingredients
		self.ingredients = []
		# list of the quantities of each ingredient
		self.quantities = []
		# dictionary of ingredients mapped to their quantities. Key: ingredient, Value: quantity
		self.mapping = {}
		r = requests.get(link)
		self.markup = BeautifulSoup(r.text)

	# find all ingredients in markup and return a list of all of them (in order)
	def find_ingredients(self):
		elements = self.markup.select('.ingredient-name')
		arr = []
		for el in elements:
			arr.append(el.text)

		self.ingredients = arr
		return arr

	# find all quantities in markup and return a list of all of them (in order)
	def find_quantities(self):
		elements = self.markup.select('.ingredient-amount')
		arr = []
		for el in elements:
			arr.append(el.text)

		self.quantities = arr
		return arr

	# returns a dictionary of each ingredient mapped to its associated quantity required
	def find_mapping(self):
		ingredients = self.find_ingredients()
		quantities = self.find_quantities()
		returnDict = {}
		if len(ingredients) != len(quantities):
			return {}
		for i in range(len(ingredients)):
			returnDict[ingredients[i]] = quantities[i]

		self.mapping = returnDict
		return returnDict


# def main():
# 	ex = Recipe("http://allrecipes.com/Recipe/Amish-Meatloaf/Detail.aspx?soid=carousel_0_rotd&prop24=rotd")
# 	print ex.find_mapping()

# if __name__ == '__main__':
# 	main()