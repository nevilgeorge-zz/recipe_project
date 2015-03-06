from Recipe import Recipe

def main():
	ex = Recipe("http://allrecipes.com/Recipe/Spinach-Lasagna-III/Detail.aspx?soid=recs_recipe_3")
	print ex.find_mapping()

if __name__ == '__main__':
	main()