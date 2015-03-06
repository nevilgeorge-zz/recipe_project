# Recipe Transformer for EECS 337

## Let's write good code
We didn't end up with neat code at the end of our last project. Let's try to change that by following these style guidelines:

- Place all essential logic/code in main.py. What is not "essential" to our project should be in a separate file/module.
- Create a new file for each class you write. Import them into the main.py script by adding ```from <<filename>> import <<classname>>``` to the top of the script.
- Class names should start with a capital letter (obviously)
- If your file is a module that you will later be importing to another file, the file name should also start with a capital letter.

__Add more to this style guide if you'd like!__


## Getting Started

- Install BeautifulSoup4 by running ```pip install beautifulsoup4``` (assuming you have pip installed, otherwise install it first)
- Install the requests module by running ```pip install requests```
- Code