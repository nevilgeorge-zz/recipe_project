# requester.py
import requests, re
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
		# list of directions from the webpage
		self.directions = []
		# dictionary of ingredients mapped to their quantities. Key: ingredient, Value: quantity
		self.mapping = {}
		# list of measurements retrieved from the quantities
		self.measurements = []
		# list of preparation key words
		self.preparation = []
		# list of descriptors of ingredients
		self.descriptors = []
		# GET the markup of the URL and store it as a member
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

	# return the list of instructions on the webpage
	def find_directions(self):
		elements = self.markup.select('.directLeft')[0].find_all('li')
		arr = []
		for el in elements:
			arr.append(el.text)

		self.directions = arr
		return arr

	# find measurements from quantities
	def find_measurements(self):
		quantities = self.find_quantities()
		arr = []
		for el in quantities:
			words = el.split()
			for w in words:
				if '/' not in w and not w.isdigit():
					arr.append(w)

		self.measurements = arr
		return arr

	# parse descriptors (preparation and description)
	def parse_preparation_descriptors(self):
		ingredients = self.find_ingredients()
		preparation = []
		descriptors = []
		for i in ingredients:
			words = i.split()
			match_obj = re.match('[a-z]{2,}((ed)|(nd))', i)
			if match_obj:
				match = match_obj.group()
				preparation.append(match)
			else:
				match = ''

			if len(words) == 2:
				if words[0] != match:
					descriptors.append(words[0])

			elif len(words) == 3:
				if words[0] == match:
					descriptors.append(words[1])
				elif words[1] == match:
					descriptors.append(words[0])

		self.preparation = preparation
		self.descriptors = descriptors
		
	# return preparation key words
	def find_preparation(self):
		self.parse_preparation_descriptors()
		return self.preparation

	# return descriptors
	def find_descriptors(self):
		self.parse_preparation_descriptors()
		return self.descriptors

# def main():
# 	ex = Recipe("http://allrecipes.com/Recipe/Amish-Meatloaf/Detail.aspx?soid=carousel_0_rotd&prop24=rotd")
# 	print ex.find_directions()

# if __name__ == '__main__':
# 	main()