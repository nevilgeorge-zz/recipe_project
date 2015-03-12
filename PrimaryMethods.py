# requester.py
import requests, re
from bs4 import BeautifulSoup
import csv
from nltk import tokenize
import operator

class PrimaryMethods:

	# constructor takes in a link of a recipe from allRecipes.com
	def __init__(self, link):
		# web URL of the allRecipes link we are using in this instance of the Recipe
		self.link = link
		#list of methods
		self.methods = []
		# GET the markup of the URL and store it as a member
		r = requests.get(link)
		self.markup = BeautifulSoup(r.text)

	# find all primary methods used in directions, and return a list of all the methods
	def find_methods(self):
		elements = self.markup.select('.directions')
		arr = []
		for el in elements:
		    arr.append(el.text.lower())
		self.methods=arr

		all_methods = []

		methodpreptimes = {}

		#build a list of all primary methods in our recipe
		with open('PrimaryMethods.csv') as inputfile:
			results = list(csv.reader(inputfile))
			for method in results:
				methodtext = ''.join(method)
				if methodtext in ''.join(self.methods):
					if methodtext:
						all_methods.append(methodtext)
		hourscookingtime = {}
		minutescookingtime = {}

		for primethod in all_methods:
			#all_methods contains all of the traditionally primary cooking steps that are part of our recipe.
			#now, we must determine which of these steps can be considered "primary"
			#I think there are two criteria for a cooking method being a primary method: high heat (frying), unique location (grilling), or longest time spent on the method

			#Therefore, our first criterion for a primary method is whether or not one of our methods contains high heat

			if primethod in ['fry', 'stir-fry', 'stir fry', 'stirfry']:
				return primethod

			#If no method contains extra high heat like frying or stir-frying, let's say that grilling must be the next most likely primary method, since grilling always takes place in a separate location
			#from the kitchen and is often the centerpiece of a recipe involving it (a grill is often used for meat, which is the main part of a lot of recipes)
			elif primethod in ['grill', 'grilled', 'bbq', 'barbecue']:
				return primethod

			#If we have no frying or grilling, let's try to find the method that takes the longest time to complete

			#each cooking time will likely have a method associated with it
			#the method with the max key in the hours or minutes dictionary will be our primary method (if hours dictionary keys empty, then we use minutes dictionary)

			listOfDirections = []
			
			mydirections = self.markup.ol.find_all('li')

			#create listOfDirections, a list of each sentence in our directions
			for i in range(0, len(mydirections)):
				for j in range(0, len(mydirections[i].string.split('.'))):
					listOfDirections.append(mydirections[i].string.split('.')[j])


			#for each sentence in our directions list, find all the cooking time lengths, and pair them with our primary methods.
			for sentence in listOfDirections:
				if 'hour' or 'hours' in sentence:
					if primethod in sentence:
						hourscookingtime[primethod] = [int(lng) for lng in sentence.split() if lng.isdigit()]
						#print 'added hours for ' + primethod
				elif 'minute' or 'minutes' in sentence:
					if primethod in sentence:
						minutescookingtime[primethod] = [int(lng) for lng in sentence.split() if lng.isdigit()]
						#print 'added minutes for ' +  primethod

				#I omitted finding times in seconds because I don't feel a recipe's primary method can usually be defined by a method that takes seconds to complete

		#now we will return the cooking method with the highest time value associated with it
		#if we recorded hours, return the method associated with the highest number of hours
		if hourscookingtime:
			#print "max hours"
			return max(hourscookingtime, key = hourscookingtime.get)
			#if we recorded minutes but not hours, return the method associated with the highest number of minutes
		elif minutescookingtime:
			#print "max minutes"
			return max(minutescookingtime, key = minutescookingtime.get)
		else:
			#if we can't find a maximum hour or minute, we simply return one of the methods in our primary methods list, since high heat, grilling, and maximum time aren't criteria that apply to this recipe
			return all_methods[0]