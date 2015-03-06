from Recipe import Recipe

def main():
	ex = Recipe("http://allrecipes.com/Recipe/Amish-Meatloaf/Detail.aspx?soid=carousel_0_rotd&prop24=rotd")
	print ex.find_mapping()

if __name__ == '__main__':
	main()