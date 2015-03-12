# requester.py
import requests, re
from bs4 import BeautifulSoup
import csv

class OtherMethods:

	# constructor takes in a link of a recipe from allRecipes.com
	def __init__(self, link):
		# web URL of the allRecipes link we are using in this instance of the Recipe
		self.link = link
		#list of tools
		self.methods = []
		# GET the markup of the URL and store it as a member
		r = requests.get(link)
		self.markup = BeautifulSoup(r.text)

	# find all methods used in directions, and return a list of all the tools (in order)
	def find_methods(self):
		elements = self.markup.select('.directions')
		arr = []
		for el in elements:
		    arr.append(el.text.lower())
		self.methods=arr

		all_methods = []

		#build a list of all secondary methods in our recipe
		#in our main python file, we will remove the primary cooking method from our OtherMethods list
		with open('OtherMethods.csv') as inputfile:
			results = list(csv.reader(inputfile))
			for method in results:
				methodtext = ''.join(method)
				if methodtext in ''.join(self.methods):
					if methodtext:
						all_methods.append(methodtext)

		return all_methods