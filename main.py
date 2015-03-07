from Recipe import Recipe

def main():
	rec = Recipe("http://allrecipes.com/Recipe/Delicious-Ham-and-Potato-Soup/Detail.aspx?soid=recs_recipe_1")
	print rec.find_ingredients()
	print rec.find_preparation()
	print rec.find_descriptors()

if __name__ == '__main__':
	main()