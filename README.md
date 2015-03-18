# Recipe Transformer for EECS 337
## by Pete Huang, Frank Avino, Nevil George, Brendan Frick


## Let's write good code
We didn't end up with neat code at the end of our last project. Let's try to change that by following these style guidelines:

- Place all essential logic/code in main.py. What is not "essential" to our project should be in a separate file/module.
- Create a new file for each class you write. Import them into the main.py script by adding ```from <<filename>> import <<classname>>``` to the top of the script.
- When installing a module/package, only include the functions that you need in the script using ```from <<filename>> import <<classname>>```
- Class names should start with a capital letter (obviously)
- If your file is a module that you will later be importing to another file, the file name should also start with a capital letter
- Feel free to contribute directly to this repo. Ideally, create a new branch and then merge with master when you have your feature working corectly

__Add more to this style guide if you'd like!__

## Module requirements
Please install the following libraries before running the program (use your favorite package installer, we used pip):

- beautifulsoup4
- requests
- re
- fuzzywuzzy

## Getting started
#### Running our system
run "python main.py" to run our recipe parser.
in "main.py", in the "main()" function, the function "ti_get_link()" will open our text interface to create transformations of a recipe.

#### Running the autograder
run "python autograder.py text url.txt", where url.txt is a text file containing the url of the AllRecipes recipe you would like to evaluate. If you want to use the autograder instead of the text interface, you will need to comment out the "ti_get_link()" function call in the "main()" function of "main.py". If "ti_get_link()" is not commented out, the text interface will run instead of the autograder.
