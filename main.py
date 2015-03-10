from Recipe import Recipe
from Tools import Tools
def main():
	rec = Recipe("http://allrecipes.com/Recipe/Delicious-Ham-and-Potato-Soup/Detail.aspx?soid=recs_recipe_1")
	tools = Tools("http://allrecipes.com/Recipe/Delicious-Ham-and-Potato-Soup/Detail.aspx?soid=recs_recipe_1")
	print rec.find_ingredients()
	print rec.find_preparation()
	print rec.find_descriptors()
	print tools.find_tools()
if __name__ == '__main__':
	main()
